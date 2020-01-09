import os

import requests as req

from requests_cache import install_cache

from statsbombpy.config import (
    CACHED_CALLS_SECS,
    CACHED_CALLS_PATH,
    DEFAULT_CREDS,
    HOSTNAME,
    VERSIONS,
)


install_cache(CACHED_CALLS_PATH, backend="sqlite", expire_after=CACHED_CALLS_SECS)


def get_resource(url: str, creds: dict):
    auth = req.auth.HTTPBasicAuth(creds["user"], creds["passwd"])
    resp = req.get(url, auth=auth)
    if resp.status_code != 200:
        print(f"{url} -> {resp.status_code}")
        resp = []
    else:
        resp = resp.json()
    return resp


def get_competitions(creds: dict = DEFAULT_CREDS) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['competitions']}/competitions"
    competitions = {}
    for c in get_resource(url, creds):
        competitions[
            (
                c["country_name"],
                c["competition_name"],
                c["season_name"],
                c["competition_gender"],
            )
        ] = c
    return competitions


def get_matches(
    competition_id: int, season_id: int, creds: dict = DEFAULT_CREDS
) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['matches']}/competitions/{competition_id}/seasons/{season_id}/matches"
    matches = {
        m["match_id"]: m
        for m in get_resource(url, creds)
        if m["match_status"] == "available"
    }
    return matches


def get_lineups(match_id: int, creds: dict = DEFAULT_CREDS) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['lineups']}/lineups/{match_id}"
    lineups = {l["team_id"]: l for l in get_resource(url, creds)}
    return lineups


def get_events(match_id: int, creds=DEFAULT_CREDS) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['events']}/events/{match_id}"
    events = {}
    for e in get_resource(url, creds):
        e["match_id"] = match_id
        events[e["id"]] = e
    return events
