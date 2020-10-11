import numpy as np
import pandas as pd 
import joblib

from recommendation_models.config import config
from recommendation_models.processing import data_management


def run_training() -> None:
    """Train the model."""
    
    books, users, ratings = data_management.load_datasets()
    print(books.columns)

    print('Training...')


if __name__ == '__main__':
    run_training()
