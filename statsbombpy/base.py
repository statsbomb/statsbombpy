import pandas as pd
import requests as req

from statsbombpy import api_client
from statsbombpy.config import DEFAULT_CREDS, OPEN_DATA_SPEC


def get_competitions(fmt="dataframe", creds: dict = DEFAULT_CREDS):
    competitions = api_client.get_competitions(creds)
    if len(competitions) == 0:
        competitions = req.get(OPEN_DATA_SPEC).json()
    if fmt == "dataframe":
        if isinstance(competitions, dict):
            competitions = competitions.values()
        competitions = pd.DataFrame(competitions)
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
        for col in ["competition_stage", "stadium", "referee"]:
            matches[col] = matches[col].apply(
                lambda x: x["name"] if not pd.isna(x) else x
            )
        metadata = matches.pop('metadata')
        for k in ['data_version', 'shot_fidelity_version', 'xy_fidelity_version']:
            matches[k] = metadata.apply(lambda x: x.get(k))
    return matches


def get_lineups(match_id, fmt="dataframe", creds: dict = DEFAULT_CREDS):
    lineups = api_client.get_lineups(match_id, creds)
    if fmt == "dataframe":
        lineups_ = {}
        for l in lineups.values():
            lineup = pd.DataFrame(l["lineup"])
            lineup['country'] = lineup.country.apply(lambda c: c['name'])
            lineups_[l['team_name']] = lineup
            lineups = lineups_
    return lineups
