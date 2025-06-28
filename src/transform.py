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
    df_wiki["country_name"] = df_wiki["country_name"].str.lower().str.strip()
    df_wiki["capital"] = df_wiki["capital"].str.lower().str.strip()
    df_wiki["year"] = 2021
    df_wiki = df_wiki.rename(columns={"population_2021": "population"})
    # Cleaning kaggle data.
    df_kaggle["country_name"] = df_kaggle["country_name"].str.lower().str.strip()
    df_kaggle["year"] = df_kaggle["year"].astype("int")
    # Retrieving the possible 205 countries with want to work with - from wikipedia
    possible_countries = (
        df_wiki.merge(
            df_kaggle,
            on="country_name",
            how="left",
        )
        .loc[:, "country_name"]
        .unique()
    )
    # Adding 'capital' and 'continent' coming from df_wiki to df_kaggle
    df_kaggle = # WRITE SOMETHING HERE
    # Concatenating df_kaggle & df_wiki into df_final
    df_final = # WRITE SOMETHING HERE
    # return 
    df_final = df_final[df_final.country_name.isin(possible_countries)]
    df_final = df_final.drop(columns=["index"])
    return df_final
