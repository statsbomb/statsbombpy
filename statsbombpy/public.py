import requests as req

import statsbombpy.entities as ents

from statsbombpy.config import OPEN_DATA_PATHS


def competitions():
    competitions = req.get(OPEN_DATA_PATHS["competitions"]).json()
    competitions = ents.competitions(competitions)
    return competitions


def matches(competition_id: int, season_id: int) -> dict:
    matches = req.get(
        OPEN_DATA_PATHS["matches"].format(
            competition_id=competition_id, season_id=season_id
        )
    ).json()
    matches = ents.matches(matches)
    return matches


def lineups(match_id: int):
    lineups = req.get(OPEN_DATA_PATHS["lineups"].format(match_id=match_id)).json()
    lineups = ents.lineups(lineups)
    return lineups


def events(match_id: int) -> dict:
    events = req.get(OPEN_DATA_PATHS["events"].format(match_id=match_id)).json()
    events = ents.events(events, match_id)
    return events
