import os

CACHED_CALLS_SECS = 600

DEFAULT_CREDS = {
    "user": os.environ.get("SB_USERNAME"),
    "passwd": os.environ.get("SB_PASSWORD"),
}

HOSTNAME = "https://data.statsbombservices.com"

OPEN_DATA_PATHS = {
    "competitions": "https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json",
    "matches": "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/{competition_id}/{season_id}.json",
    "lineups": "https://raw.githubusercontent.com/statsbomb/open-data/master/data/lineups/{match_id}.json",
    "events": "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{match_id}.json",
    "frames": "https://raw.githubusercontent.com/statsbomb/open-data/master/data/three-sixty/{match_id}.json",
}

PARALLELL_CALLS_NUM = 4

VERSIONS = {
    "competitions": "v2",
    "matches": "v3",
    "lineups": "v2",
    "events": "v6",
    "360-frames": "v1",
    "player-match-stats": "v1",
    "player-season-stats": "v1",
    "team-season-stats": "v1",
}
