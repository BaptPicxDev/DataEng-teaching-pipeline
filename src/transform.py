# Import
import pandas as pd
from src.extract import (
    retrieve_country_population_from_wikipedia,
    retrieve_country_population_from_kaggle,
)


# Function
def transform_inputs() -> pd.DataFrame:
    return