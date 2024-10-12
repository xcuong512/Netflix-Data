# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

print(netflix_df.head())
print(netflix_df.info())

# Filter for movies from the 1990s
netflix_df_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]
print("Movies released in the 90s:" + str(netflix_df_1990s))
print("Number of movies released in the 90s:", len(netflix_df_1990s))

# Find the most frequent movie duration
most_frequent_duration = netflix_df_1990s['duration'].mode()[0]
duration = int(most_frequent_duration)
print(f"Most frequent movie duration in the 1990s: {duration} minutes")

# Count short action movies
short_action_movies = netflix_df_1990s[(netflix_df_1990s['duration'] < 90) & (netflix_df_1990s['genre'].str.contains('Action', case = False))]
short_movie_count = len(short_action_movies)
print(f"Count of short action movies from the 1990s: {short_movie_count}")
