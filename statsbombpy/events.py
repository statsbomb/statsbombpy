from statsbombpy.config import DEFAULT_CREDS
from statsbombpy.api_client import get_competitions, get_matches, get_events


def get_shots(match_id, creds=DEFAULT_CREDS):
    pass


def get_league_shots(competition, creds=DEFAULT_CREDS):
    c = get_competitions(creds)[
        competition["country"],
        competition["division"],
        competition["season"],
        competition["gender"],
    ]
    matches = get_matches(c["competition_id"], c["season_id"], creds)
    print(competition)

if __name__ == "__main__":
    competition = {
        "country": "England",
        "division": "Premier League",
        "season": "2019/2020",
        "gender": "male",
    }
    get_shots(competition)

