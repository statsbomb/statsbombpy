import warnings
from tempfile import mkdtemp

import requests as req
from requests_cache import install_cache

import statsbombpy.entities as ents
from statsbombpy.config import CACHED_CALLS_SECS, HOSTNAME, VERSIONS

install_cache(mkdtemp(), backend="sqlite", expire_after=CACHED_CALLS_SECS)


class NoAuthWarning(UserWarning):
    """Warning raised when no user credentials are provided."""

    pass


def has_auth(creds):
    if creds.get("user") in [None, ""] or creds.get("passwd") in [None, ""]:
        warnings.warn(
            "credentials were not supplied. open data access only", NoAuthWarning
        )
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
    return ents.competitions(competitions)


def matches(competition_id: int, season_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['matches']}/competitions/{competition_id}/seasons/{season_id}/matches"
    matches = get_resource(url, creds)
    return ents.matches(matches)


def lineups(match_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['lineups']}/lineups/{match_id}"
    lineups = get_resource(url, creds)
    return ents.lineups(lineups)


def events(match_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['events']}/events/{match_id}"
    events = get_resource(url, creds)
    return ents.events(events, match_id)


def frames(match_id: int, creds: dict) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['360-frames']}/360-frames/{match_id}"
    frames = get_resource(url, creds)
    return ents.frames(frames, match_id)


def player_match_stats(match_id: int, creds: dict) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['player-match-stats']}/matches/{match_id}/player-stats"
    return get_resource(url, creds)


def player_season_stats(competition_id: int, season_id: int, creds: dict) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['player-season-stats']}/competitions/{competition_id}/seasons/{season_id}/player-stats"
    return get_resource(url, creds)


def team_match_stats(match_id: int, creds: dict) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['team-match-stats']}/matches/{match_id}/team-stats"
    return get_resource(url, creds)


def team_season_stats(competition_id: int, season_id: int, creds: dict) -> list:
    url = f"{HOSTNAME}/api/{VERSIONS['team-season-stats']}/competitions/{competition_id}/seasons/{season_id}/team-stats"
    return get_resource(url, creds)
