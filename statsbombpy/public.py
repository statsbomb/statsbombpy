import requests as req

import statsbombpy.entities as ents
from statsbombpy.config import OPEN_DATA_PATHS


def competitions():
    response = req.get(OPEN_DATA_PATHS["competitions"])
    response.raise_for_status()
    competitions = response.json()
    competitions = ents.competitions(competitions)
    return competitions


def matches(competition_id: int, season_id: int) -> dict:
    response = req.get(
        OPEN_DATA_PATHS["matches"].format(
            competition_id=competition_id, season_id=season_id
        )
    )
    response.raise_for_status()

    matches = response.json()
    matches = ents.matches(matches)
    return matches


def lineups(match_id: int):
    response = req.get(OPEN_DATA_PATHS["lineups"].format(match_id=match_id))
    response.raise_for_status()
    lineups = response.json()
    lineups = ents.lineups(lineups)
    return lineups


def events(match_id: int) -> dict:
    response = req.get(OPEN_DATA_PATHS["events"].format(match_id=match_id))
    response.raise_for_status()
    events = response.json()
    events = ents.events(events, match_id)
    return events


def frames(match_id: int) -> dict:
    response = req.get(OPEN_DATA_PATHS["frames"].format(match_id=match_id))
    response.raise_for_status()
    frames = response.json()
    frames = ents.frames(frames, match_id)
    return frames
