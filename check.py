import warnings
from tempfile import mkdtemp

import requests as req
from requests_cache import install_cache

import statsbombpy.entities as ents
from statsbombpy.config import CACHED_CALLS_SECS, HOSTNAME, VERSIONS, DEFAULT_CREDS

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


def events(match_id: int, creds: dict) -> dict:
    url = f"{HOSTNAME}/api/{VERSIONS['events']}/events/{match_id}"
    events = get_resource(url, creds)
    return ents.events(events, match_id)

events(1234, creds=DEFAULT_CREDS)

import requests as req

import statsbombpy.entities as ents
from statsbombpy.config import OPEN_DATA_PATHS
from json.decoder import JSONDecodeError

def events(match_id: int) -> dict:
    try:
        events = req.get(OPEN_DATA_PATHS["events"].format(match_id=match_id)).json()
    except JSONDecodeError:
        raise ValueError(f"{match_id}: Match not found")
    events = ents.events(events, match_id)
    return events

events(1234)

