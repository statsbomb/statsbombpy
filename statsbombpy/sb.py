import pandas as pd
import requests as req

from collections import defaultdict
from functools import partial, reduce
from multiprocessing import Pool

from statsbombpy import api_client, public
from statsbombpy.config import DEFAULT_CREDS, PARALLELL_CALLS_NUM
from statsbombpy.helpers import filter_and_group_events, is_relevant, reduce_events


def competitions(fmt="dataframe", creds: dict = DEFAULT_CREDS):
    if api_client.has_auth(creds) is True:
        competitions = api_client.competitions(creds)
    else:
        competitions = public.competitions()
    if fmt == "dataframe":
        if isinstance(competitions, dict):
            competitions = competitions.values()
        competitions = pd.DataFrame(competitions)
    return competitions


def matches(
    competition_id: int, season_id: int, fmt="dataframe", creds: dict = DEFAULT_CREDS
):
    if api_client.has_auth(creds) is True:
        matches = api_client.matches(competition_id, season_id, creds)
    else:
        matches = public.matches(competition_id, season_id)
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


def lineups(match_id, fmt="dataframe", creds: dict = DEFAULT_CREDS):
    if api_client.has_auth(creds) is True:
        lineups = api_client.lineups(match_id, creds)
    else:
        lineups = public.lineups(match_id)
    if fmt == "dataframe":
        lineups_ = {}
        for l in lineups.values():
            lineup = pd.DataFrame(l["lineup"])
            lineup["country"] = lineup.country.apply(lambda c: c["name"])
            lineups_[l["team_name"]] = lineup
            lineups = lineups_
    return lineups


def events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten_attrs: bool = True,
    creds: dict = DEFAULT_CREDS,
) -> (pd.DataFrame, dict):

    if api_client.has_auth(creds) is True:
        events = api_client.events(match_id, creds)
    else:
        events = public.events(match_id)

    if fmt == "dataframe":
        events = filter_and_group_events(events, filters, fmt, flatten_attrs)
        for ev_type, evs in events.items():
            events[ev_type] = pd.DataFrame(evs)
        if split is False:
            events = pd.concat([*events.values()], axis=0, ignore_index=True, sort=True)
    return events


def competition_events(
    country: str,
    division: str,
    season: str,
    gender: str = "male",
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
) -> (pd.DataFrame, dict):

    c = competitions(creds)[country, division, season, gender]

    events_call = partial(events, fmt="json", creds=creds,)
    with Pool(PARALLELL_CALLS_NUM) as p:
        matches_events = p.map(
            events_call, matches(c["competition_id"], c["season_id"], creds)
        )
        matches_events = map(
            lambda events: filter_and_group_events(
                events, filters, fmt, fmt == "dataframe"
            ),
            matches_events,
        )

    competition_events = reduce_events(matches_events, fmt)
    if fmt == "dataframe" and split is False:
        competition_events = pd.concat(
            [*competition_events.values()], axis=0, ignore_index=True, sort=True
        )
    return competition_events
