import multiprocessing
import os
from importlib.metadata import PackageNotFoundError, version

CACHED_CALLS_SECS = 600

try:
    _VERSION = version("statsbombpy")
except PackageNotFoundError:
    _VERSION = "unknown"

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

# Fallback endpoint versions, used when the live endpoint-versions map cannot be
# fetched (e.g. no credentials or a request failure) or omits an endpoint.
VERSIONS = {
    "competitions": "v4",
    "matches": "v6",
    "lineups": "v5",
    "events": "v11",
    "360-frames": "v2",
    "player-match-stats": "v8",
    "player-season-stats": "v7",
    "team-season-stats": "v4",
    "team-match-stats": "v4",
}

# Maps the keys returned by {HOSTNAME}/api/endpoint-versions to the package's
# internal endpoint names used in VERSIONS. api_player_mapping is intentionally
# omitted as it has no corresponding endpoint in this package.
API_VERSION_KEYS = {
    "api_competitions": "competitions",
    "api_matches": "matches",
    "api_lineups": "lineups",
    "api_events": "events",
    "api_360_freeze_frames": "360-frames",
    "api_player_match_stats": "player-match-stats",
    "api_player_season_stats": "player-season-stats",
    "api_team_season_stats": "team-season-stats",
    "api_team_match_stats": "team-match-stats",
}
