from collections import defaultdict
from joblib import Memory

import inflect
import pandas as pd


def flatten_event(event, flatten_attrs):
    if flatten_attrs:
        ev_type = event["type"]["name"].lower().replace(" ", "_").replace("*", "")
        ev_type = ev_type if event["type"]["name"] != "Goal Keeper" else "goalkeeper"
        if ev_type in event:
            for k, v in event[ev_type].items():
                event[f"{ev_type}_{k}"] = v
            del event[ev_type]

    for k, v in event.copy().items():
        if isinstance(v, dict) and "name" in v:
            event[k] = v["name"]
            if k in ['possession_team', 'player']:
                event[f"{k}_id"] = v['id']
    return event


def filter_and_group_events(events, filters, fmt, flatten_attrs):
    events_ = defaultdict(list)
    for ev in events.values():
        ev_type = pluralize(ev["type"]["name"])
        if not is_relevant(ev, filters):
            continue
        if fmt == "dataframe":
            ev = flatten_event(ev, flatten_attrs)
        events_[ev_type].append(ev)
    return events_


def is_relevant(event, filters):
    return all(event.get("type", {}).get("name") == v for k, v in filters.items())


def reduce_events(all_events: dict, fmt: str) -> dict:
    reduced_events = defaultdict(list)
    for events in all_events:
        for ev_type, evs in events.items():
            reduced_events[ev_type] = reduced_events.get(ev_type, []) + evs
    if fmt == "dataframe":
        for ev_type, evs in reduced_events.items():
            reduced_events[ev_type] = pd.DataFrame(evs)
    return reduced_events


engine = inflect.engine()

cachedir = ".cache/"
memory = Memory(cachedir, verbose=0)


@memory.cache
def pluralize(word):
    word = engine.plural(word)
    word = word.replace("*", "")
    word = word.replace("-", "_")
    word = word.replace(" ", "_")
    word = word.lower()
    return word
