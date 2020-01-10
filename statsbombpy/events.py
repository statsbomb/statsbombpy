from collections import defaultdict
from functools import partial, reduce
from multiprocessing import Pool

import pandas as pd

from statsbombpy.helpers import flatten_event, is_relevant, reduce_events
from statsbombpy.config import DEFAULT_CREDS, PARALLELL_CALLS_NUM
from statsbombpy.api_client import (
    get_competitions,
    get_events as query_api_events,
    get_matches,
)


def get_events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten: bool = False,
    creds: dict = DEFAULT_CREDS,
) -> (pd.DataFrame, dict):

    events = defaultdict(list)
    for ev in query_api_events(match_id, creds).values():
        ev_type = ev["type"]["name"]
        if not is_relevant(ev, filters):
            continue
        if flatten is True or fmt == "dataframe":
            ev = flatten_event(ev)
        events[ev_type].append(ev)

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
