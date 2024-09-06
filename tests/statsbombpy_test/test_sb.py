from unittest import TestCase, main

import pandas as pd
from requests.exceptions import HTTPError
from statsbombpy import sb


class TestBaseGetters(TestCase):
    def test_competitions(self):
        competitions = sb.competitions()
        self.assertIsInstance(competitions, pd.DataFrame)

        competitions = sb.competitions(fmt="json")
        self.assertIsInstance(competitions, dict)

        competitions = sb.competitions(creds={})
        self.assertIsInstance(competitions, pd.DataFrame)

    def test_matches(self):
        matches = sb.matches(competition_id=43, season_id=3)
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=43, season_id=3, fmt="json")
        self.assertIsInstance(matches, dict)

        matches = sb.matches(competition_id=43, season_id=3, creds={})
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=2, season_id=44)
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=2, season_id=44, fmt="json")
        self.assertIsInstance(matches, dict)

        matches = sb.matches(competition_id=2, season_id=44, creds={})
        self.assertIsInstance(matches, pd.DataFrame)

        matches = sb.matches(competition_id=11, season_id=1)
        self.assertEqual(
            matches.query("match_id == 9695")["away_managers"].iloc[0],
            "Ernesto Valverde Tejedor",
        )

        with self.assertRaises(HTTPError) as cm:
            matches = sb.matches(competition_id=1, season_id=1, creds={})
        self.assertEqual(cm.exception.response.status_code, 404)

    def test_lineups(self):
        lineups = sb.lineups(match_id=7562)
        self.assertIsInstance(lineups, dict)
        self.assertIsInstance([*lineups.values()][0], pd.DataFrame)

        lineups = sb.lineups(match_id=7562, fmt="json")
        self.assertIsInstance(lineups, dict)

        lineups = sb.lineups(match_id=7562, creds={})
        self.assertIsInstance(lineups, dict)

        lineups = sb.lineups(match_id=301244)
        self.assertEqual(
            lineups["Stoke City"]["country"].iloc[0],
            "England",
        )

        with self.assertRaises(HTTPError) as cm:
            lineups = sb.lineups(match_id=1, creds={})
        self.assertEqual(cm.exception.response.status_code, 404)


class TestEventGetters(TestCase):
    def test_events(self):
        events = sb.events(match_id=7562)
        self.assertIsInstance(events, pd.DataFrame)

        events = sb.events(match_id=7562, split=True)
        self.assertIsInstance(events, dict)
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = sb.events(match_id=7562, fmt="json")
        self.assertIsInstance(events, dict)

        events = sb.events(match_id=7562, creds={})
        self.assertIsInstance(events, pd.DataFrame)
        self.assertTrue("shot_statsbomb_xg" in events.columns)

        events = sb.events(match_id=7562, creds={}, flatten_attrs=False)
        self.assertIsInstance(events, pd.DataFrame)
        self.assertFalse("shot_statsbomb_xg" in events.columns)
        self.assertTrue("shot" in events.columns)

        events = sb.events(match_id=3837323, fmt="json", include_360_metrics=True)
        self.assertIsInstance(events, dict)

        events = sb.events(match_id=3837323, include_360_metrics=True)
        self.assertIsInstance(events, pd.DataFrame)
        self.assertTrue("visible_teammates" in events.columns)

        with self.assertRaises(HTTPError) as cm:
            events = sb.events(match_id=1, creds={})
        self.assertEqual(cm.exception.response.status_code, 404)

    def test_competition_events(self):
        events = sb.competition_events(
            country="Europe",
            division="Champions League",
            season="2018/2019",
            gender="male",
        )
        self.assertIsInstance(events, pd.DataFrame)

        events = sb.competition_events(
            country="Europe",
            division="Champions League",
            season="2018/2019",
            split=True,
        )
        self.assertIsInstance(events["shots"], pd.DataFrame)

        events = sb.competition_events(
            country="Europe",
            division="Champions League",
            season="2022/2023",
            fmt="json",
        )
        self.assertIsInstance(events, dict)

        events = sb.competition_events(
            country="Europe",
            division="Champions League",
            season="2022/2023",
            include_360_metrics=True,
        )
        self.assertIsInstance(events, pd.DataFrame)
        self.assertTrue("visible_teammates" in events.columns)


class TestFrameGetters(TestCase):
    def test_frames(self):
        frames = sb.frames(match_id=3764302)
        self.assertIsInstance(frames, pd.DataFrame)

        frames = sb.frames(match_id=3764302, fmt="json")
        self.assertIsInstance(frames, list)

        frames = sb.frames(match_id=3788741, creds={})
        self.assertIsInstance(frames, pd.DataFrame)

        frames = sb.frames(match_id=3847567, creds={})
        self.assertIsInstance(frames, pd.DataFrame)

        with self.assertRaises(HTTPError) as cm:
            frames = sb.frames(match_id=1, creds={})
        self.assertEqual(cm.exception.response.status_code, 404)

    def test_competition_frames(self):
        frames = sb.competition_frames(
            country="Europe",
            division="Champions League",
            season="2022/2023",
            gender="male",
        )
        self.assertIsInstance(frames, pd.DataFrame)
        self.assertIsInstance(frames.distance_from_edge_of_visible_area[0], float)

        frames = sb.competition_frames(
            country="Europe",
            division="Champions League",
            season="2022/2023",
            gender="male",
            fmt="json",
        )
        self.assertIsInstance(frames, list)


class TestAggregatedStatsGetters(TestCase):
    def test_player_match_stats(self):
        player_match_stats = sb.player_match_stats(match_id=7562)
        self.assertIsInstance(player_match_stats, pd.DataFrame)

        player_match_stats = sb.player_match_stats(match_id=7562, fmt="json")
        self.assertIsInstance(player_match_stats, list)

        with self.assertRaises(Exception):
            sb.player_match_stats(match_id=7562, creds={})

    def test_player_season_stats(self):
        player_season_stats = sb.player_season_stats(competition_id=43, season_id=3)
        self.assertIsInstance(player_season_stats, pd.DataFrame)

        player_season_stats = sb.player_season_stats(
            competition_id=43, season_id=3, fmt="json"
        )
        self.assertIsInstance(player_season_stats, list)

        with self.assertRaises(Exception):
            sb.player_season_stats(competition_id=43, season_id=3, creds={})

        player_season_stats = sb.player_season_stats(competition_id=2, season_id=44)
        self.assertIsInstance(player_season_stats, pd.DataFrame)

        player_season_stats = sb.player_season_stats(
            competition_id=2, season_id=44, fmt="json"
        )
        self.assertIsInstance(player_season_stats, list)

        with self.assertRaises(Exception):
            sb.player_season_stats(competition_id=2, season_id=44, creds={})

    def test_team_match_stats(self):
        team_match_stats = sb.team_match_stats(match_id=3764302)
        self.assertIsInstance(team_match_stats, pd.DataFrame)

        team_match_stats = sb.team_match_stats(match_id=3764302, fmt="json")
        self.assertIsInstance(team_match_stats, list)

        with self.assertRaises(Exception):
            sb.team_match_stats(match_id=7562, creds={})


    def test_team_season_stats(self):
        team_season_stats = sb.team_season_stats(competition_id=43, season_id=3)
        self.assertIsInstance(team_season_stats, pd.DataFrame)

        team_season_stats = sb.team_season_stats(
            competition_id=43, season_id=3, fmt="json"
        )
        self.assertIsInstance(team_season_stats, list)

        with self.assertRaises(Exception):
            sb.team_season_stats(competition_id=43, season_id=3, creds={})

        team_season_stats = sb.team_season_stats(competition_id=2, season_id=44)
        self.assertIsInstance(team_season_stats, pd.DataFrame)

        team_season_stats = sb.team_season_stats(
            competition_id=2, season_id=44, fmt="json"
        )
        self.assertIsInstance(team_season_stats, list)

        with self.assertRaises(Exception):
            sb.team_season_stats(competition_id=2, season_id=44, creds={})


if __name__ == "__main__":
    main()