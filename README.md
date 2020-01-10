# statsbombpy

#### By: StatsBomb

#### Support: support@statsbombservices.com

#### Updated January 9, 2020.

This repository is a Python package to easily stream StatsBomb data into Python using your log in credentials for the API or free data from our GitHub page. **API access is for paying customers only**


## Installation Instructions

`git clone https://github.com/statsbomb/statsbombpy.git`  
`cd statsbombpy`  
`pip install .`


## Running the tests

`nose2 -v --pretty-assert`


## Authentication

### Environment Variables
Authentication can be easily done by setting environment variables named `SB_USERNAME` and `SB_PASSWORD` to your login credentials.

### Manual Calls
Alternatively, if you don't want to use environment variables, all functions accept an argument `creds`, where you can pass your login credentials `{"user": "", "passwd": ""}`


## Open Data
StatsBomb's open data can be accessed without the need of authentication.

## Basic Usage

```
from statsbombpy.base import get_competitions, get_matches, get_lineups
from statsbombpy.events import get_competition_events, get_events
```

```
get_competitions()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>competition_id</th>
      <th>season_id</th>
      <th>country_name</th>
      <th>competition_name</th>
      <th>competition_gender</th>
      <th>season_name</th>
      <th>match_updated</th>
      <th>match_available</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>42</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2019-12-29T07:47:45.981</td>
      <td>2019-12-29T07:47:45.981</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>4</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2018/2019</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>2019-12-16T23:09:16.168756</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>1</td>
      <td>Germany</td>
      <td>1. Bundesliga</td>
      <td>male</td>
      <td>2017/2018</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>2019-12-16T23:09:16.168756</td>
    </tr>
    <tr>
      <th>3</th>
      <td>78</td>
      <td>42</td>
      <td>Croatia</td>
      <td>1. HNL</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2020-01-02T10:35:49.065</td>
      <td>2020-01-02T10:35:49.065</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>42</td>
      <td>Germany</td>
      <td>2. Bundesliga</td>
      <td>male</td>
      <td>2019/2020</td>
      <td>2019-12-27T00:36:37.498</td>
      <td>2019-12-27T00:36:37.498</td>
    </tr>
  </tbody>
</table>


```
get_matches(competition_id=9, season_id=42)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>match_id</th>
      <th>match_date</th>
      <th>kick_off</th>
      <th>competition</th>
      <th>season</th>
      <th>home_team</th>
      <th>away_team</th>
      <th>home_score</th>
      <th>away_score</th>
      <th>match_status</th>
      <th>last_updated</th>
      <th>metadata</th>
      <th>match_week</th>
      <th>competition_stage</th>
      <th>stadium</th>
      <th>referee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>303299</td>
      <td>2019-12-15</td>
      <td>18:00:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Schalke 04</td>
      <td>Eintracht Frankfurt</td>
      <td>1</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-17T09:50:17.558</td>
      <td>{'data_version': '1.1.0', 'shot_fidelity_version': '2', 'xy_fidelity_version': '2'}</td>
      <td>15</td>
      <td>{'id': 1, 'name': 'Regular Season'}</td>
      <td>{'id': 370, 'name': 'VELTINS-Arena', 'country': {'id': 85, 'name': 'Germany'}}</td>
      <td>{'id': 241, 'name': 'F. Zwayer', 'country': {'id': 112, 'name': 'Italy'}}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>303223</td>
      <td>2019-09-01</td>
      <td>18:00:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Eintracht Frankfurt</td>
      <td>Fortuna Düsseldorf</td>
      <td>2</td>
      <td>1</td>
      <td>available</td>
      <td>2019-12-16T23:09:16.168756</td>
      <td>{'data_version': '1.1.0', 'shot_fidelity_version': '2', 'xy_fidelity_version': '2'}</td>
      <td>3</td>
      <td>{'id': 1, 'name': 'Regular Season'}</td>
      <td>{'id': 4850, 'name': 'Commerzbank-Arena'}</td>
      <td>{'id': 243, 'name': 'F. Willenborg', 'country': {'id': 112, 'name': 'Italy'}}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>303083</td>
      <td>2019-12-15</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Wolfsburg</td>
      <td>Borussia Mönchengladbach</td>
      <td>2</td>
      <td>1</td>
      <td>available</td>
      <td>2019-12-17T15:52:17.843</td>
      <td>{'data_version': '1.1.0', 'shot_fidelity_version': '2', 'xy_fidelity_version': '2'}</td>
      <td>15</td>
      <td>{'id': 1, 'name': 'Regular Season'}</td>
      <td>{'id': 4849, 'name': 'VOLKSWAGEN ARENA'}</td>
      <td>{'id': 226, 'name': 'F. Brych', 'country': {'id': 112, 'name': 'Italy'}}</td>
    </tr>
    <tr>
      <th>3</th>
      <td>303266</td>
      <td>2019-12-14</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Hertha Berlin</td>
      <td>Freiburg</td>
      <td>1</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-17T17:43:18.285</td>
      <td>{'data_version': '1.1.0', 'shot_fidelity_version': '2', 'xy_fidelity_version': '2'}</td>
      <td>15</td>
      <td>{'id': 1, 'name': 'Regular Season'}</td>
      <td>{'id': 367, 'name': 'Olympiastadion Berlin', 'country': {'id': 85, 'name': 'Germany'}}</td>
      <td>{'id': 243, 'name': 'F. Willenborg', 'country': {'id': 112, 'name': 'Italy'}}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>303073</td>
      <td>2019-12-21</td>
      <td>15:30:00.000</td>
      <td>Germany - 1. Bundesliga</td>
      <td>2019/2020</td>
      <td>Bayern Munich</td>
      <td>Wolfsburg</td>
      <td>2</td>
      <td>0</td>
      <td>available</td>
      <td>2019-12-23T18:02:36.454</td>
      <td>{'data_version': '1.1.0', 'shot_fidelity_version': '2', 'xy_fidelity_version': '2'}</td>
      <td>17</td>
      <td>{'id': 1, 'name': 'Regular Season'}</td>
      <td>{'id': 4867, 'name': 'Allianz Arena'}</td>
      <td>{'id': 237, 'name': 'C. Dingert', 'country': {'id': 112, 'name': 'Italy'}}</td>
    </tr>
  </tbody>
</table>

```
get_lineups(303299)["Eintracht Frankfurt"]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>player_name</th>
      <th>player_nickname</th>
      <th>birth_date</th>
      <th>player_gender</th>
      <th>player_height</th>
      <th>player_weight</th>
      <th>jersey_number</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3204</td>
      <td>Almamy Touré</td>
      <td>None</td>
      <td>1996-04-28</td>
      <td>male</td>
      <td>182.0</td>
      <td>72.0</td>
      <td>18</td>
      <td>{'id': 140, 'name': 'Mali'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5591</td>
      <td>Filip Kostić</td>
      <td>None</td>
      <td>1992-11-01</td>
      <td>male</td>
      <td>184.0</td>
      <td>82.0</td>
      <td>10</td>
      <td>{'id': 203, 'name': 'Serbia'}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7713</td>
      <td>Obite Evan N"Dicka</td>
      <td>Evan N'Dicka</td>
      <td>1999-08-20</td>
      <td>male</td>
      <td>190.0</td>
      <td>NaN</td>
      <td>2</td>
      <td>{'id': 78, 'name': 'France'}</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8307</td>
      <td>Martin Hinteregger</td>
      <td>None</td>
      <td>1992-09-07</td>
      <td>male</td>
      <td>184.0</td>
      <td>83.0</td>
      <td>13</td>
      <td>{'id': 15, 'name': 'Austria'}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8669</td>
      <td>Mijat Gaćinović</td>
      <td>None</td>
      <td>1995-02-08</td>
      <td>male</td>
      <td>175.0</td>
      <td>66.0</td>
      <td>11</td>
      <td>{'id': 203, 'name': 'Serbia'}</td>
    </tr>
  </tbody>
</table>


```
get_events(match_id=303299)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball_receipt</th>
      <th>ball_recovery</th>
      <th>block</th>
      <th>carry</th>
      <th>clearance</th>
      <th>counterpress</th>
      <th>dribble</th>
      <th>duel</th>
      <th>duration</th>
      <th>foul_committed</th>
      <th>foul_won</th>
      <th>goalkeeper</th>
      <th>id</th>
      <th>index</th>
      <th>injury_stoppage</th>
      <th>interception</th>
      <th>location</th>
      <th>match_id</th>
      <th>minute</th>
      <th>off_camera</th>
      <th>out</th>
      <th>pass</th>
      <th>period</th>
      <th>play_pattern</th>
      <th>player</th>
      <th>position</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>related_events</th>
      <th>second</th>
      <th>shot</th>
      <th>substitution</th>
      <th>team</th>
      <th>timestamp</th>
      <th>type</th>
      <th>under_pressure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.613804</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4657d086-61ba-47be-b9e0-4225dda2cba1</td>
      <td>17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[34.5, 37.3]</td>
      <td>303299</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'recipient': {'id': 20770, 'name': 'Ozan Muhammed Kabak'}, 'length': 27.502909, 'angle': 1.5853407, 'height': {'id': 1, 'name': 'Ground Pass'}, 'end_location': [34.1, 64.8], 'body_part': {'id': 40, 'name': 'Right Foot'}}</td>
      <td>1</td>
      <td>From Kick Off</td>
      <td>Omar Mascarell González</td>
      <td>Right Defensive Midfield</td>
      <td>2</td>
      <td>Schalke 04</td>
      <td>[12d711dd-171f-4a3d-97f1-79d38acfafc9]</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:00:10.828</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.520875</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>986c8b58-9d53-4822-b416-bbb32aa60e34</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[34.1, 64.8]</td>
      <td>303299</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'recipient': {'id': 20662, 'name': 'Alexander Nübel'}, 'length': 29.560953, 'angle': -2.6749194, 'height': {'id': 1, 'name': 'Ground Pass'}, 'end_location': [7.7, 51.5], 'body_part': {'id': 40, 'name': 'Right Foot'}}</td>
      <td>1</td>
      <td>From Kick Off</td>
      <td>Ozan Muhammed Kabak</td>
      <td>Right Center Back</td>
      <td>2</td>
      <td>Schalke 04</td>
      <td>[5baa0c48-fd69-4318-be89-a0134fe98cb3]</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:00:12.444</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.945589</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>f87aaab4-7e41-4c23-9f3a-27e31cb5a2e1</td>
      <td>23</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[7.8, 51.5]</td>
      <td>303299</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'recipient': {'id': 8526, 'name': 'Weston McKennie'}, 'length': 39.134254, 'angle': -1.3518503, 'height': {'id': 1, 'name': 'Ground Pass'}, 'end_location': [16.3, 13.3], 'body_part': {'id': 40, 'name': 'Right Foot'}}</td>
      <td>1</td>
      <td>From Kick Off</td>
      <td>Alexander Nübel</td>
      <td>Goalkeeper</td>
      <td>2</td>
      <td>Schalke 04</td>
      <td>[f11b171e-c645-4348-903c-6c7d0b65caa6]</td>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:00:15.740</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.378187</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c528c517-0cd5-4594-9803-ed55ef836296</td>
      <td>27</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[18.8, 4.4]</td>
      <td>303299</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'recipient': {'id': 8504, 'name': 'Bastian Oczipka'}, 'length': 10.245975, 'angle': -0.32792333, 'height': {'id': 1, 'name': 'Ground Pass'}, 'end_location': [28.5, 1.1], 'body_part': {'id': 40, 'name': 'Right Foot'}}</td>
      <td>1</td>
      <td>From Kick Off</td>
      <td>Weston McKennie</td>
      <td>Left Center Back</td>
      <td>2</td>
      <td>Schalke 04</td>
      <td>[6349045d-bbb0-4583-8ee9-b7cb36a4f1ae, b6cbb6a8-4e51-4444-bc22-6e146b6cb926]</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:00:20.439</td>
      <td>Pass</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.940027</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>65e75211-9ae0-4acc-84bd-4e7526725ba4</td>
      <td>31</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>[24.2, 2.4]</td>
      <td>303299</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'recipient': {'id': 20662, 'name': 'Alexander Nübel'}, 'length': 26.402462, 'angle': 2.3106496, 'height': {'id': 1, 'name': 'Ground Pass'}, 'end_location': [6.4, 21.9], 'body_part': {'id': 40, 'name': 'Right Foot'}}</td>
      <td>1</td>
      <td>From Kick Off</td>
      <td>Bastian Oczipka</td>
      <td>Left Back</td>
      <td>2</td>
      <td>Schalke 04</td>
      <td>[1198e2ba-47a0-401a-89e7-3871aef2f150]</td>
      <td>22</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Schalke 04</td>
      <td>00:00:22.657</td>
      <td>Pass</td>
      <td>NaN</td>
    </tr>
  </tbody>


</table>

```
grouped_events = get_events(match_id=303299, split=True)
grouped_events["Dribble"]
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>index</th>
      <th>period</th>
      <th>timestamp</th>
      <th>minute</th>
      <th>second</th>
      <th>type</th>
      <th>possession</th>
      <th>possession_team</th>
      <th>play_pattern</th>
      <th>team</th>
      <th>player</th>
      <th>position</th>
      <th>location</th>
      <th>duration</th>
      <th>under_pressure</th>
      <th>related_events</th>
      <th>dribble</th>
      <th>match_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b190c01f-ad24-468c-8241-f955b91d996c</td>
      <td>131</td>
      <td>1</td>
      <td>00:02:08.032</td>
      <td>2</td>
      <td>8</td>
      <td>Dribble</td>
      <td>4</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[110.2, 62.9]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[60f822df-5747-4787-b0f9-45bf5217eb8a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4d773c92-f89f-491e-b3e0-3a1d2e863148</td>
      <td>399</td>
      <td>1</td>
      <td>00:08:48.623</td>
      <td>8</td>
      <td>48</td>
      <td>Dribble</td>
      <td>18</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Amine Harit</td>
      <td>Center Attacking Midfield</td>
      <td>[88.9, 22.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[93d829df-eea7-416b-95aa-7593828cfade]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8a78dce4-998a-4e81-902c-9f3957cebc9d</td>
      <td>460</td>
      <td>1</td>
      <td>00:13:30.202</td>
      <td>13</td>
      <td>30</td>
      <td>Dribble</td>
      <td>23</td>
      <td>Schalke 04</td>
      <td>Regular Play</td>
      <td>Schalke 04</td>
      <td>Daniel Caligiuri</td>
      <td>Right Wing</td>
      <td>[99.5, 68.1]</td>
      <td>0.007309</td>
      <td>True</td>
      <td>[772c5aae-e34e-4364-8a98-7caf7636c90b]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e44d0122-2f2e-4771-820d-cc326a8b0379</td>
      <td>496</td>
      <td>1</td>
      <td>00:14:10.135</td>
      <td>14</td>
      <td>10</td>
      <td>Dribble</td>
      <td>24</td>
      <td>Schalke 04</td>
      <td>From Throw In</td>
      <td>Schalke 04</td>
      <td>Suat Serdar</td>
      <td>Left Defensive Midfield</td>
      <td>[41.2, 31.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[4de4039f-7efc-461b-b7d6-27c32ec2cd2a]</td>
      <td>{'outcome': {'id': 8, 'name': 'Complete'}}</td>
      <td>303299</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9555afbd-d838-42c9-8f80-be3cd09e4c4a</td>
      <td>793</td>
      <td>1</td>
      <td>00:20:18.409</td>
      <td>20</td>
      <td>18</td>
      <td>Dribble</td>
      <td>33</td>
      <td>Eintracht Frankfurt</td>
      <td>Regular Play</td>
      <td>Eintracht Frankfurt</td>
      <td>Timothy Chandler</td>
      <td>Right Wing Back</td>
      <td>[81.8, 75.7]</td>
      <td>0.000000</td>
      <td>True</td>
      <td>[a5c88cee-6319-4c25-91cd-8a028d8dbfbf]</td>
      <td>{'outcome': {'id': 9, 'name': 'Incomplete'}}</td>
      <td>303299</td>
    </tr>
  </tbody>
</table>

```
bundesliga = {
    "country": "Germany",
     "division": "1. Bundesliga",
     "season": "2019/2020",
     "gender": "male"
}
get_competition_events(competition=bundesliga)
get_competition_events(competition=bundesliga, split=True)
```


