import pandas as pd
import requests as req

from collections import defaultdict
from functools import partial, reduce
from multiprocessing import Pool

from statsbombpy import api_client, public
from statsbombpy.config import DEFAULT_CREDS, PARALLELL_CALLS_NUM
from statsbombpy.helpers import filter_and_group_events, is_relevant, reduce_events


def get_competitions(fmt="dataframe", creds: dict = DEFAULT_CREDS):
    if api_client.has_auth(creds) is True:
        competitions = api_client.get_competitions(creds)
    else:
        competitions = public.get_competitions()
    if fmt == "dataframe":
        if isinstance(competitions, dict):
            competitions = competitions.values()
        competitions = pd.DataFrame(competitions)
    return competitions


def get_matches(
    competition_id: int, season_id: int, fmt="dataframe", creds: dict = DEFAULT_CREDS
):
    if api_client.has_auth(creds) is True:
        matches = api_client.get_matches(competition_id, season_id, creds)
    else:
        matches = public.get_matches(competition_id, season_id)
    if fmt == "dataframe":
        matches = pd.DataFrame(matches.values())
        matches["competition"] = matches.competition.apply(
            lambda c: f"{c['country_name']} - {c['competition_name']}"
        )
        for col in ["season", "home_team", "away_team"]:
            matches[col] = matches[col].apply(lambda c: c[f"{col}_name"])
        for col in ["competition_stage", "stadium", "referee"]:
            matches[col] = matches[col].apply(
                lambda x: x["name"] if not pd.isna(x) else x
            )
        metadata = matches.pop("metadata")
        for k in ["data_version", "shot_fidelity_version", "xy_fidelity_version"]:
            matches[k] = metadata.apply(lambda x: x.get(k))
    return matches


def get_lineups(match_id, fmt="dataframe", creds: dict = DEFAULT_CREDS):
    if api_client.has_auth(creds) is True:
        lineups = api_client.get_lineups(match_id, creds)
    else:
        lineups = public.get_lineups(match_id)
    if fmt == "dataframe":
        lineups_ = {}
        for l in lineups.values():
            lineup = pd.DataFrame(l["lineup"])
            lineup["country"] = lineup.country.apply(lambda c: c["name"])
            lineups_[l["team_name"]] = lineup
            lineups = lineups_
    return lineups


def get_events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten: bool = False,
    creds: dict = DEFAULT_CREDS,
) -> (pd.DataFrame, dict):

    if api_client.has_auth(creds) is True:
        events = api_client.get_events(match_id, creds)
    else:
        events = public.get_events(match_id)
    events = filter_and_group_events(events, filters, fmt, flatten)

    if fmt == "dataframe":
        for ev_type, evs in events.items():
            events[ev_type] = pd.DataFrame(evs)
        if split is False:
            events = pd.concat([*events.values()], axis=0, ignore_index=True, sort=True)
    return events


def get_competition_events(
    competition: dict,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
) -> (pd.DataFrame, dict):

    c = get_competitions(creds)[
        competition["country"],
        competition["division"],
        competition["season"],
        competition["gender"],
    ]
    matches = get_matches(c["competition_id"], c["season_id"], creds)

    get_events_call = partial(
        get_events,
        split=True,
        filters=filters,
        fmt="json",
        flatten=fmt == "dataframe",
        creds=creds,
    )
    with Pool(PARALLELL_CALLS_NUM) as p:
        matches_events = p.map(get_events_call, matches)
    events = reduce_events(matches_events, fmt)
    if fmt == "dataframe" and split is False:
        events = pd.concat([*events.values()], axis=0, ignore_index=True, sort=True)
    return events
