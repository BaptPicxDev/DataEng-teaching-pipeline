# Import
import pandas as pd
from src.extract import (
    retrieve_country_population_from_wikipedia,
    retrieve_country_population_from_kaggle,
)
import typing


# Function
def retrieve_inputs() -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
    return (
        retrieve_country_population_from_wikipedia(),
        retrieve_country_population_from_kaggle(),
    )


def transform_inputs() -> pd.DataFrame:
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
    # Merging
    possible_countries = (
        df_wiki.merge(
            df_kaggle,
            on="country_name",
            how="left",
        )
        .loc[:, "country_name"]
        .unique()
    )
    df_kaggle = df_kaggle.merge(
        df_wiki.loc[:, ["country_name", "continent", "capital"]],
        on="country_name",
        how="left",
    )
    df_final = pd.concat([df_wiki, df_kaggle]).sort_values(by="year").reset_index(drop=True)
    df_final = df_final.drop(columns=["index"])
    df_final = df_final[df_final.country_name.isin(possible_countries)]
    return df_final