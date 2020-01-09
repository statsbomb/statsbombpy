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
    filters: dict = {},
    fmt: str = "dataframe",
    flatten=False,
    creds: dict = DEFAULT_CREDS,
) -> dict:

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
    return events


def get_competition_events(
    competition: dict,
    filters: dict = {},
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
) -> dict:

    c = get_competitions(creds)[
        competition["country"],
        competition["division"],
        competition["season"],
        competition["gender"],
    ]
    matches = get_matches(c["competition_id"], c["season_id"], creds)

    get_events_call = partial(
        get_events, filters=filters, fmt="json", flatten=fmt == "dataframe", creds=creds
    )
    with Pool(PARALLELL_CALLS_NUM) as p:
        matches_events = p.map(get_events_call, matches)

    events = reduce_events(matches_events, fmt)
    return events
