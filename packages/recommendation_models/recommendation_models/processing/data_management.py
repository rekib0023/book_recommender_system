import pandas as pd
import numpy as np
import html

from recommendation_models.config import config


def load_dataset() -> pd.DataFrame:
    with open(config.DATASET_DIR / config.BOOKS_DATASET, 'r', encoding='latin-1') as f, open(config.DATASET_DIR / config.BOOKS_FIXED_DATASET, 'w') as g:
        content = html.unescape(f.read())
        g.write(content)
        
    # read the three datasets
    books = pd.read_csv(f"{config.DATASET_DIR}/{config.BOOKS_FIXED_DATASET}", skipinitialspace = True, sep=';', quotechar = '"', escapechar = '\\', encoding= 'latin-1')
    users= pd.read_csv(f"{config.DATASET_DIR}/{config.USERS_DATASET}", sep= ';', encoding= 'latin-1')
    ratings= pd.read_csv(f"{config.DATASET_DIR}/{config.RATINGS_DATASET}", sep= ';', encoding= 'latin-1')
    
    # change columns' name
    books.columns= books.columns.str.strip().str.lower().str.replace('-', '_')
    users.columns= users.columns.str.strip().str.lower().str.replace('-', '_')
    ratings.columns= ratings.columns.str.strip().str.lower().str.replace('-', '_')
    
    # data cleaning
    books.loc[(books['isbn'] == '9627982032'),'book_author'] = 'other'
    books.loc[(books['publisher'].isnull()),'publisher'] = 'no mention'
    books.drop(config.DROP_BOOKS_COLUMNS, axis= 1, inplace= True)
    users.loc[(users['age'] > 90) | (users['age'] < 5)] = np.nan
    users['age'].fillna((users['age'].mean()), inplace=True)
    users['age']= users['age'].astype('int64')
    
    # Merging the datasets into one dataset on isbn
    # only take the ISBNs that also belongs to the main books dataset.
    unique_ratings = ratings[ratings.isbn.isin(books.isbn)]
    # separate the explicit ratings represented by 1–10 and implicit ratings represented by 0.
    ratings_explicit= unique_ratings[unique_ratings['book_rating'] != 0]
    ratings_implicit= unique_ratings[unique_ratings['book_rating'] == 0]
    #  only consider ISBNs that were explicitely rated for this recommendation system.
    _data = pd.merge(books, ratings_explicit, on='isbn')
    
    return _data