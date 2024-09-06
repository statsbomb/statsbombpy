import multiprocessing
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

if "SB_CORES" in os.environ:
    MAX_CONCURRENCY = int(os.environ["SB_CORES"])
else:
    try:
        MAX_CONCURRENCY = max(multiprocessing.cpu_count() - 2, 4)
    except NotImplementedError:
        MAX_CONCURRENCY = 4

VERSIONS = {
    "competitions": "v4",
    "matches": "v6",
    "lineups": "v4",
    "events": "v8",
    "360-frames": "v2",
    "player-match-stats": "v4",
    "player-season-stats": "v4",
    "team-season-stats": "v2",
    "team-match-stats": "v1",
}
