from nba_api.stats.static import players
import pandas as pd
import numpy as np

df = pd.DataFrame(players.get_players())

filtered_for_active = df[df["is_active"]]
print(filtered_for_active.columns)


