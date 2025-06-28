# Import
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import typing


# Functions.
def retrieve_country_population_from_wikipedia(
        url="https://simple.wikipedia.org/wiki/List_of_countries_by_continents",
    ) -> pd.DataFrame:
    """Use pandas read_html to retrieve all the tableau data contained into the html page.
    Once retrieve, select the specific one and return the corresponding DataFrame.

    :param url: URL of the wikipedia page.
    :return pd.DataFrame: DataFrame with wikipedia 2021 country population.
    """
    dfs_continents = pd.read_html(url)
    df_africa = dfs_continents[0]
    df_africa["continent"] = "africa"
    df_africa = df_africa.drop(columns=["Unnamed: 0", "Flag", "Map"], errors='ignore').rename(
        columns={
            'English Name [1][2][3][4]': 'country_name',
            'Capital [3][5][6]': 'capital',
            'Population 2021 [7][8]': 'population_2021',
            'Area[a][b] [9]': 'area',
            'Currency [3]': 'currency',
        },
    )
    df_african_islands = dfs_continents[1]
    df_african_islands["continent"] = "africa"
    df_african_islands = df_african_islands.drop(columns=["Flag", "Map"], errors='ignore').rename(
        columns={
            'English Name': 'country_name',
            'Capital': 'capital',
            'Population 2021': 'population_2021',
            'Area (km²/mi²)': 'area',
            'Currency': 'currency',
        },
    )
    df_asia = dfs_continents[2]
    df_asia["continent"] = "asia"
    df_asia = df_asia.drop(columns=["Unnamed: 0", "Flag", "Map"], errors='ignore').rename(
        columns={
            'English Name [4][10][11][12]': 'country_name',
            'Capital [12][13][14]': 'capital',
            'Population 2021 [7][8]': 'population_2021',
            'Area[a][b] [9]': 'area',
        },
    )
    df_europe = dfs_continents[3]
    df_europe["continent"] = "europe"
    df_europe = df_europe.drop(columns=[0, 1, 7], errors='ignore').rename(
        columns={
            2: 'country_name',
            3: 'capital',
            4: 'population_2021',
            5: 'area',
            6: 'currency',
        },
    )
    df_north_america = dfs_continents[4]
    df_north_america["continent"] = "north america"
    df_north_america = df_north_america.drop(columns=['Unnamed: 0', 'Flag', 'Map'], errors='ignore').rename(
        columns={
            'English Name [4][12][19][20]': 'country_name',
            'Capital [12][14][21]': 'capital',
            'Population 2021 [7][8]': 'population_2021',
            'Area[a][b] [9]': 'area',
            'Currency [12]': 'currency',
        },
    )
    df_south_america = dfs_continents[5]
    df_south_america["continent"] = "south america"
    df_south_america = df_south_america.drop(columns=['Unnamed: 0', 'Flag', 'Location'], errors='ignore').rename(
        columns={
            'English Name': 'country_name',
            'Capital': 'capital',
            'Population 2021 [7][8]': 'population_2021',
            'Area[a][b][9]': 'area',
            'Official languages': 'language',
            'Currency': 'currency',
        },
    )
    df_oceania = dfs_continents[6]
    df_oceania["continent"] = "oceania"
    df_oceania = df_oceania.drop(columns=['Unnamed: 0', 'Flag', 'Location'], errors='ignore').rename(
        columns={
            'English Name': 'country_name',
            'Capital': 'capital',
            'Population 2021 [7][8]': 'population_2021',
            'Area[a][b] [9]': 'area',
            'Official languages': 'language',
            'Coin': 'currency',
        },
    )
    df_continent = pd.concat(
        [
            df_africa,
            df_african_islands,
            df_asia,
            df_europe,
            df_north_america,
            df_south_america,
            df_oceania,
        ]
    )
    df_continent["area"] = df_continent["area"].str.replace(
        r'\(.*\)', "", regex=True,
    )
    df_continent = df_continent.rename(columns={"area": "area_km2"})
    df_continent = df_continent.drop(columns=["language", "currency", "area_km2"])
    return df_continent.reset_index()


def retrieve_country_population_from_kaggle(
        dataset_name="imdevskp/world-population-19602018",
        filename="population_total_long.csv",
    ) -> pd.DataFrame:
    """Use Python Kaggle API to retrieve the historic data of country population.
    Within Kaggle, there is a dataset created by the user imdevskp with historical data.
    Using kaggle python package installed within the virtual environment, we will get the data
    and extract it in a pandas DataFrame.
    You can access it here: https://www.kaggle.com/datasets/imdevskp/world-population-19602018?select=population_total_long.csv

    :param dataset_name: user and dataset name separated by '/'
    :param filename: corresponding filename.
    :return pd.DataFrame: DataFrame with kaggle historical country population.
    """
    # Authenticating through kaggle API.
    kaggle_api = KaggleApi()
    try:
        kaggle_api.authenticate()
    except Exception as exc:
        raise exc
    # Creating data/ folder if not existing.
    if not os.path.exists("data/"):
        os.makedirs("data/")
    # Download the data using python kaggle API if it does not exists
    if not os.path.exists(os.path.join("data/", filename)):
       kaggle_api.dataset_download_file(dataset_name, filename, path="data/")
    # Reading the file
    df = pd.read_csv(os.path.join("data/", filename))
    df.columns = ["country_name", "year", "population"]
    return df


# Main thread for testing.
if __name__ == "__main__":
    retrieve_country_population_from_wikipedia()
