import pandas as pd
import datetime 

def load(debug=False, filename = 'epl2020.csv'):
    source_df = pd.read_csv(f'.\data\{filename}')
    # each game has it's distinct datetime and referee. It is possible 2 games happen at the same time so the referee will distinguish.
    home_games = source_df[source_df['h_a'] == 'h']
    away_games = source_df[source_df['h_a'] == 'a']

    games_df = pd.merge(home_games, away_games, on=['date', 'Referee.x'] , suffixes = ('_home', '_away'))
    games_df['game_id'] = games_df['date'].apply(lambda x : int(x.replace('-','').replace(' ','').replace(':','')))

    if debug:
        from explore.inspect import show_df
        show_df(games_df)
    return games_df