import pandas as pd

df = pd.read_csv('books.csv')

books_df_cleaned = df.copy()

categorical = ['authors', 'subtitle', 'categories', 'thumbnail', 'description']
numerical = ['published_year', 'average_rating', 'num_pages', 'ratings_count']

for column in categorical:
    books_df_cleaned.fillna({f'{column}': 'unknown'}, inplace=True)

for column in numerical:
    books_df_cleaned.fillna({f'{column}': -1}, inplace=True)