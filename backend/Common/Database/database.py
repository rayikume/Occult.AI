# import pandas as pd

# df = pd.read_csv('books.csv')

# books_df_cleaned = df.copy()

# # filling categorical columns
# books_df_cleaned['authors'].fillna('unknown', inplace=True)
# books_df_cleaned['subtitle'].fillna('unknown', inplace=True)
# books_df_cleaned['categories'].fillna('unknown', inplace=True)
# books_df_cleaned['thumbnail'].fillna('no thumbnail', inplace=True)
# books_df_cleaned['description'].fillna('no description', inplace=True)

# # filling the numerical columns
# books_df_cleaned['published_year'].fillna(books_df_cleaned['published_year'].median(), inplace=True)
# books_df_cleaned['average_rating'].fillna(books_df_cleaned['average_rating'].mean(), inplace=True)
# books_df_cleaned['num_pages'].fillna(books_df_cleaned['num_pages'].median(), inplace=True)
# books_df_cleaned['ratings_count'].fillna(books_df_cleaned['ratings_count'].median(), inplace=True)

# print(books_df_cleaned)