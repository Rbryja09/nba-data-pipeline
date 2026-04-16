import time
import numpy as np
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, commonteamroster
from nba_api.stats.static import teams

def player_nba_stats():
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='Totals',
        height_nullable=True
    )

    df = player_stats.get_data_frames()[0]
    return df.columns


def player_physical_stats():
    team_list = []
    nba_teams = teams.get_teams()
    team_count = len(nba_teams)


    for index, team in enumerate(nba_teams[0:2], start=1):
   
        try:
            player_stats = commonteamroster.CommonTeamRoster(
                season='2025-26',
                team_id = team['id']
            )
            print(f"{index}/{team_count} API Calls Made - Curent Team: {team['full_name']}")
        except Exception as e:
            print(e, f"{team['full_name']} API Call Failed") 
            break

        stats_dictionary = player_stats.get_data_frames()[0]
        team_list.append(stats_dictionary[['PLAYER','HEIGHT']])
        time.sleep(0.8)

    df = pd.concat(team_list,ignore_index=True)
    
    return df 


def average_nba_height():
    player_height = player_physical_stats()

    return player_height










if __name__ == '__main__':
    print(average_nba_height())

   


for index, team in enumerate(nba_teams, start=1):

    for n in range(1:3):
        try:
            player_stats = commonteamroster.CommonTeamRoster(
                season='2025-26',
                team_id = team['id']
            )
            print(f"{index}/{team_count} API Calls Made - Current Team: {team['full_name']}")
        finally:
            time.sleep(0.8)
        except Exception as e:
            print(e, f"{team['full_name']} API Call Failed - Retrying Attempt ({n}/3")
            continue
