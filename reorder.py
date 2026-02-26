import pandas as pd

# Read files
sleep_df = pd.read_excel("sleep_qual.xlsx")
results_df = pd.read_csv("results.csv")

# Clean column names
sleep_df.columns = sleep_df.columns.str.strip()
results_df.columns = results_df.columns.str.strip()

# Clean and standardize the key
sleep_df["Insert code"] = sleep_df["Insert code"].astype(str).str.strip()
results_df["Insert code"] = results_df["Insert code"].astype(str).str.strip()

# 🔴 Keep only NEW columns from results_df (avoid duplicates)
new_cols = [col for col in results_df.columns
            if col not in sleep_df.columns or col == "Insert code"]

results_df_reduced = results_df[new_cols]

# Merge (order preserved from sleep_df)
final_df = sleep_df.merge(
    results_df_reduced,
    on="Insert code",
    how="left",
    sort=False
)

# Save output
final_df.to_csv("final_results.csv", index=False)

