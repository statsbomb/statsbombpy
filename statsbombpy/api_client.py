import os

import pandas as pd
import requests as req

from requests_cache import install_cache
from tempfile import mkdtemp

import statsbombpy.entities as ents

from statsbombpy.config import (
    CACHED_CALLS_SECS,
    HOSTNAME,
    VERSIONS,
)


install_cache(mkdtemp(), backend="sqlite", expire_after=CACHED_CALLS_SECS)


def has_auth(creds):
    if creds.get("user") in [None, ""] or creds.get("passwd") in [None, ""]:
        print("credentials were not supplied. open data access only")
        return False
    return True


def get_resource(url: str, creds: dict) -> list:
    auth = req.auth.HTTPBasicAuth(creds["user"], creds["passwd"])
    resp = req.get(url, auth=auth)
    if resp.status_code != 200:
        print(f"{url} -> {resp.status_code}")
        resp = []
    else:
        resp = resp.json()
    return resp


def competitions(creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['competitions']}/competitions"
    competitions = get_resource(url, creds)
    competitions = ents.competitions(competitions)
    return competitions


def matches(competition_id: int, season_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['matches']}/competitions/{competition_id}/seasons/{season_id}/matches"
    matches = get_resource(url, creds)
    matches = ents.matches(matches)
    return matches


def lineups(match_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['lineups']}/lineups/{match_id}"
    lineups = get_resource(url, creds)
    lineups = ents.lineups(lineups)
    return lineups


def events(match_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['events']}/events/{match_id}"
    events = get_resource(url, creds)
    events = ents.events(events, match_id)
    return events

