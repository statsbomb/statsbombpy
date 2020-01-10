import requests as req

from config import OPEN_DATA_PATHS


def get_competitions():
    competitions = req.get(OPEN_DATA_PATHS["competitions"]).json()
    return competitions


def get_matches(competition_id: int, season_id: int) -> dict:
    pass


def get_events(competition_id: int, season_id: int) -> dict:
    pass