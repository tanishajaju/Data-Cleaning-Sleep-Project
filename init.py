import pandas as pd

import os
import pandas as pd

# Input and output directories
input_dir = "experiment_data"
output_dir = "csv_files"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Column names
columns = [
    "block",
    "shape",
    "congruency",
    "cong_in_number",
    "response",
    "response_time",
    "correct",
    "consistency"
]

for file in os.listdir(input_dir):
    if file.endswith(".txt"):
        txt_path = os.path.join(input_dir, file)
        csv_path = os.path.join(output_dir, file.replace(".txt", ".csv"))

        df = pd.read_csv(
            txt_path,
            sep=r"\s+",
            header=None,
            names=columns,
            engine="python"
        )

        df.to_csv(csv_path, index=False)

        print(f"Saved: {csv_path}")
