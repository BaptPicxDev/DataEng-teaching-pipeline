# Import
import os
import kaggle
import pandas as pd
import typing

# Functions.
def retrieve_country_population_from_wikipedia(url="https://simple.wikipedia.org/wiki/List_of_countries_by_continents") -> pd.DataFrame:
    """
    :param url:
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

    :param dataset_name:
    :param filename:
    :return pd.DataFrame:
    """
    # Creating data/ folder if not existing.
    if not os.path.exists:
        os.makedirs("data/")
    # Download the data using python kaggle API if it does not exists
    if not os.path.exists(os.path.join("data/", filename)):
        kaggle.KaggleApi().dataset_download_file(dataset_name, filename, path="data/")
    # Reading the file
    return pd.DataFrame(os.path.join("data/", filename))


# Main thread for testing.
if __name__ == "__main__":
    print(dir(kaggle.KaggleApi()))
    print(retrieve_country_population_from_wikipedia())