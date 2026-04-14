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
        
        df = player_stats.get_data_frames()[0]
    


    return team_list


def average_nba_height():
    df = common_player_stats()
    avg_height = np.mean(df['height'])    
    return avg_height


if __name__ == '__main__':
    print(player_physical_stats())


    
