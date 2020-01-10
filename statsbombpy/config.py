import os

CACHED_CALLS_SECS = 600

CACHED_CALLS_PATH = "/tmp/statsbombpy"

DEFAULT_CREDS = {
    "user": os.environ.get("SB_USERNAME"),
    "passwd": os.environ.get("SB_PASSWORD"),
}

HOSTNAME = "https://data.statsbombservices.com"

OPEN_DATA_SPEC = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json"

PARALLELL_CALLS_NUM = 4

VERSIONS = {"competitions": "v2", "matches": "v3", "lineups": "v2", "events": "v5"}

