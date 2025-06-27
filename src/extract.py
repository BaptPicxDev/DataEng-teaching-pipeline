# Import
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import typing

# Functions.
def retrieve_country_population_from_wikipedia(url="https://simple.wikipedia.org/wiki/List_of_countries_by_continents") -> pd.DataFrame:
    """USe pandas read_html to retrieve all the tableau data contained into the html page.
    Once retrieve, select the specific one and return the corresponding DataFrame.

    :param url: URL of the wikipedia page.
    :return pd.DataFrame:
    """
    tableau = pd.read_html(url)
    df = tableau[0]
    df.columns = ["index", "flag", "country_name", "capital", "population", "area", "currency", "map"]
    df = df.drop(columns=["index", "flag", "map"])
    return df

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
    :param filename: corresponding filename
    :return pd.DataFrame:
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
    print(retrieve_country_population_from_kaggle())