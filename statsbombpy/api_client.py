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


def get_resource(url, creds):
    auth = req.auth.HTTPBasicAuth(creds["user"], creds["passwd"])
    return req.get(url, auth=auth).json()


def get_competitions(creds=DEFAULT_CREDS):
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


def get_matches(competition_id, season_id, creds=DEFAULT_CREDS):
    url = f"{HOSTNAME}/api/{VERSIONS['matches']}/competitions/{competition_id}/seasons/{season_id}/matches"
    matches = {}
    for m in get_resource(url, creds):
        matches[m['id']] = m
    return matches


def get_lineups(match_id, creds=DEFAULT_CREDS):
    url = f"{HOSTNAME}/api/{VERSIONS['lineups']}/lineups/{match_id}"
    lineups = get_resource(url, creds)
    return lineups


def get_events(match_id, creds=DEFAULT_CREDS):
    url = f"{HOSTNAME}/api/{VERSIONS['events']}/events/{match_id}"
    events = get_resource(url, creds)
    return events
