import pathlib

import recommendation_models


PACKAGE_ROOT = pathlib.Path(recommendation_models.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

BOOKS_DATASET = "BX-Books.csv"
BOOKS_FIXED_DATASET = "book_data_fixed.csv"
USERS_DATASET = "BX-Users.csv"
RATINGS_DATASET = "BX-Book-Ratings.csv"

# books
DROP_BOOKS_COLUMNS = ['image_url_s', 'image_url_m', 'image_url_l']

# users
MISSING_USERS_COLUMNS = ['age']

# ratings