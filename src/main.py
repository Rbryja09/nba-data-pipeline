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
    max_attempts = 3

    for index, team in enumerate(nba_teams, start=1):
        for n in range(max_attempts):
            try:
                player_stats = commonteamroster.CommonTeamRoster(
                    season='2025-26',
                    team_id = team['id']
                )
                print(f"{index}/{team_count} API Calls Made - Curent Team: {team['full_name']}")
                break
            except Exception as e:
                print(e, f"{team['full_name']} API Call Failed. Retrying... Attempt #{n+1}/{max_attempts}") 
                if n+1 == max_attempts:
                    print(f"API Calls Exhausted for {team['full_name']} - Throwing Error")
                    raise
            finally:
                time.sleep(0.8)

        stats_dictionary = player_stats.get_data_frames()[0]
        team_list.append(stats_dictionary[['PLAYER','HEIGHT']])

    df = pd.concat(team_list,ignore_index=True)
    
    return df 


def average_nba_height():
    player_height = player_physical_stats()

    return player_height










if __name__ == '__main__':
    print(average_nba_height())

