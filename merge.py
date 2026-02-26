import pandas as pd

# Read files
sleep_df = pd.read_excel("sleep_qual.xlsx")
results_df = pd.read_csv("results.csv")

# Clean column names (VERY important)
sleep_df.columns = sleep_df.columns.str.strip()
results_df.columns = results_df.columns.str.strip()

# Optional: print to verify
print("sleep_df columns:", sleep_df.columns.tolist())
print("results_df columns:", results_df.columns.tolist())

# Merge (order preserved from sleep_df)
final_df = sleep_df.merge(
    results_df,
    on="Insert code",
    how="left",
    sort=False
)

# Save final output
final_df.to_csv("final_results.csv", index=False)
