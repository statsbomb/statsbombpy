import requests as req

import statsbombpy.entities as ents
from statsbombpy.config import OPEN_DATA_PATHS


def get_response(path):
    response = req.get(path)
    response.raise_for_status()
    data = response.json()
    return data


def competitions():
    competitions = get_response(OPEN_DATA_PATHS["competitions"])
    competitions = ents.competitions(competitions)
    return competitions


def matches(competition_id: int, season_id: int) -> dict:
    path = OPEN_DATA_PATHS["matches"].format(
        competition_id=competition_id, season_id=season_id
    )
    matches = get_response(path)
    matches = ents.matches(matches)
    return matches


def lineups(match_id: int):
    path = OPEN_DATA_PATHS["lineups"].format(match_id=match_id)
    lineups = get_response(path)
    lineups = ents.lineups(lineups)
    return lineups


def events(match_id: int) -> dict:
    path = OPEN_DATA_PATHS["events"].format(match_id=match_id)
    events = get_response(path)
    events = ents.events(events, match_id)
    return events


def frames(match_id: int) -> dict:
    path = OPEN_DATA_PATHS["frames"].format(match_id=match_id)
    frames = get_response(path)
    frames = ents.frames(frames, match_id)
    return frames
