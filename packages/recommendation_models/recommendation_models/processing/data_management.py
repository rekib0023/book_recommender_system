import pandas as pd
import html

from recommendation_models.config import config


def load_datasets() -> pd.DataFrame:
    with open(config.DATASET_DIR / config.BOOKS_DATASET, 'r', encoding='latin-1') as f, open(config.DATASET_DIR / config.BOOKS_FIXED_DATASET, 'w') as g:
        content = html.unescape(f.read())
        g.write(content)
        
    books = pd.read_csv(f"{config.DATASET_DIR}/{config.BOOKS_FIXED_DATASET}", skipinitialspace = True, sep=';', quotechar = '"', escapechar = '\\', encoding= 'latin-1')
    users= pd.read_csv(f"{config.DATASET_DIR}/{config.USERS_DATASET}", sep= ';', encoding= 'latin-1')
    ratings= pd.read_csv(f"{config.DATASET_DIR}/{config.RATINGS_DATASET}", sep= ';', encoding= 'latin-1')
    
    books.columns= books.columns.str.strip().str.lower().str.replace('-', '_')
    users.columns= users.columns.str.strip().str.lower().str.replace('-', '_')
    ratings.columns= ratings.columns.str.strip().str.lower().str.replace('-', '_')
    
    return books, users, ratings