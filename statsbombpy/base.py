import pandas as pd

from statsbombpy import api_client
from statsbombpy.config import DEFAULT_CREDS


def get_competitions(fmt="dataframe", creds: dict = DEFAULT_CREDS):
    competitions = api_client.get_competitions(creds)
    if fmt == "dataframe":
        competitions = pd.DataFrame(competitions.values())
    return competitions


def get_matches(
    competition_id: int, season_id: int, fmt="dataframe", creds: dict = DEFAULT_CREDS
):
    matches = api_client.get_matches(competition_id, season_id, creds)
    if fmt == "dataframe":
        matches = pd.DataFrame(matches.values())
        matches["competition"] = matches.competition.apply(
            lambda c: f"{c['country_name']} - {c['competition_name']}"
        )
        for col in ["season", "home_team", "away_team"]:
            matches[col] = matches[col].apply(lambda c: c[f"{col}_name"])
    return matches


def get_lineups(match_id, fmt="dataframe", creds: dict = DEFAULT_CREDS):
    lineups = api_client.get_lineups(match_id, creds)
    if fmt == "dataframe":
        lineups = {l["team_name"]: pd.DataFrame(l["lineup"]) for l in lineups.values()}
    return lineups
