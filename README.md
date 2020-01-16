# statsbombpy

#### By: StatsBomb

#### Support: support@statsbombservices.com

#### Updated January 15, 2020.

This repository is a Python package to easily stream StatsBomb data into Python using your log in credentials for the API or free data from our GitHub page. **API access is for paying customers only**


## Installation Instructions

`git clone https://github.com/statsbomb/statsbombpy.git`  
`cd statsbombpy`  
`pip install .`


## Running the tests

`nose2 -v --pretty-assert`


## Authentication

#### Environment Variables
Authentication can be done by setting environment variables named `SB_USERNAME` and `SB_PASSWORD` to your login credentials.

#### Manual Calls
Alternatively, if you don't want to use environment variables, all functions accept an argument `creds` to pass your login credentials in the format `{"user": "", "passwd": ""}`


## Open Data
StatsBomb's open data can be accessed without the need of authentication.

StatsBomb are committed to sharing new data and research publicly to enhance understanding of the game of Football. We want to actively encourage new research and analysis at all levels. Therefore we have made certain leagues of StatsBomb Data freely available for public use for research projects and genuine interest in football analytics.

StatsBomb are hoping that by making data freely available, we will extend the wider football analytics community and attract new talent to the industry. We would like to collect some basic personal information about users of our data. By [giving us your email address](https://statsbomb.com/resource-centre/), it means we will let you know when we make more data, tutorials and research available. We will store the information in accordance with our Privacy Policy and the GDPR.

#### Terms & Conditions
Whilst we are keen to share data and facilitate research, we also urge you to be responsible with the data. Please register your details on https://www.statsbomb.com/resource-centre and read our [User Agreement](doc/LICENSE.pdf) carefully.
By using this repository, you are agreeing to the user agreement. If you publish, share or distribute any research, analysis or insights based on this data, please state the data source as StatsBomb and use our logo.


## Usage

```
from statsbombpy import sb
```

```
sb.competitions()
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
sb.matches(competition_id=9, season_id=42)
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
      <th>match_week</th>
      <th>competition_stage</th>
      <th>stadium</th>
      <th>referee</th>
      <th>data_version</th>
      <th>shot_fidelity_version</th>
      <th>xy_fidelity_version</th>
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
      <td>15</td>
      <td>Regular Season</td>
      <td>VELTINS-Arena</td>
      <td>F. Zwayer</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
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
      <td>3</td>
      <td>Regular Season</td>
      <td>Commerzbank-Arena</td>
      <td>F. Willenborg</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
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
      <td>15</td>
      <td>Regular Season</td>
      <td>VOLKSWAGEN ARENA</td>
      <td>F. Brych</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
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
      <td>15</td>
      <td>Regular Season</td>
      <td>Olympiastadion Berlin</td>
      <td>F. Willenborg</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
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
      <td>17</td>
      <td>Regular Season</td>
      <td>Allianz Arena</td>
      <td>C. Dingert</td>
      <td>1.1.0</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>


```
sb.lineups(match_id=303299)["Eintracht Frankfurt"]
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
      <td>Mali</td>
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
      <td>Serbia</td>
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
      <td>France</td>
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
      <td>Austria</td>
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
      <td>Serbia</td>
    </tr>
  </tbody>
</table>


```
events = sb.events(match_id=303299)  # if you want to store all events in a given match on a single dataframe

grouped_events = sb.events(match_id=303299, split=True)
grouped_events["dribbles"]
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

events = sb.competition_events(competition=bundesliga) # if you want to store all events in a given competition on a single dataframe

grouped_events = sb.competition_events(competition=bundesliga, split=True)
grouped_events["dribbles"]
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


