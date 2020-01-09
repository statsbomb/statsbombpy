from collections import defaultdict

import pandas as pd


def flatten_event(event):
    for k, v in event.items():
        if isinstance(v, dict) and "name" in v:
            event[k] = v["name"]
    return event


def is_relevant(event, filters):
    return all(event[1].get("type", {}).get("name") == v for k, v in filters.items())


def reduce_events(all_events: dict, fmt: str) -> dict:
    reduced_events = defaultdict(list)
    for events in all_events:
        for ev_type, evs in events.items():
            reduced_events[ev_type] = reduced_events.get(ev_type, []) + evs
    if fmt == "dataframe":
        for ev_type, evs in reduced_events.items():
            reduced_events[ev_type] = pd.DataFrame(evs)
    return reduced_events
