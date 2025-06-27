# Import
import os
from src.transform import (
    transform_inputs,
)


# Functions
def store_transfomed_df_into_csv_files(output_name="df.csv") -> None:
    """
    """
    # Extract and transform data.
    df = transform_inputs()
    # Check for output folder.
    if not os.path.exists("data/"):
        os.makedirs("data/")
    df.to_csv(os.path.join("data/", output_name))
