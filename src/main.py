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
   

    for team in nba_teams:
    
        player_stats = commonteamroster.CommonTeamRoster(
            season='2025-26',
            team_id = team['id']
        )
        
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

   

