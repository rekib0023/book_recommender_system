import numpy as np
import pandas as pd 
import joblib

from recommendation_models.config import config
from recommendation_models.processing.data_management import load_dataset


def run_training() -> None:
    """Train the model."""
    
    data = load_dataset()
    print(data.columns)
    print(data.iloc[0])
    print(data.iloc[1])

    print('Training...')


if __name__ == '__main__':
    run_training()
