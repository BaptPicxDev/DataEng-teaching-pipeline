# Import
import pandas as pd
from src.extract import (
    retrieve_country_population_from_wikipedia,
    retrieve_country_population_from_kaggle,
)
import typing


# Functions.
def retrieve_inputs() -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
    """Retrieve the input data.
    Utilitary function to simplify.

    :return tuple: Tuple of two dataframe that corresponds to the extraction of wikipedia and kaggle country population data
    """
    return (
        retrieve_country_population_from_wikipedia(),
        retrieve_country_population_from_kaggle(),
    )


def transform_inputs() -> pd.DataFrame:
    """After retrieving the data from wikipedia and kaggle,
    Clean and uniformise the data.
    Then merge it into a single DataFrame.

    :return pd.DataFrame: Merge DataFrame.
    """
    # Retrieving inputs
    df_wiki, df_kaggle = retrieve_inputs()
    # Cleaning Wiki data.
    
    # WRITE SOMETHING HERE
