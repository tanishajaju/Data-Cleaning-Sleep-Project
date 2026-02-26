import pandas as pd
import os

# Load init data
init_df = pd.read_csv("init_data_final.csv")
# init_df = init_df.loc[:, ~init_df.columns.duplicated()]

csv_dir = "csv_files"
results = []

for _, row in init_df.iterrows():
    txt_name = row["cognitive_flexibility"]
    csv_name = txt_name.replace(".txt", ".csv")
    csv_path = os.path.join(csv_dir, csv_name)

    if not os.path.exists(csv_path):
        print(f"Missing file: {csv_name}")
        continue

    df = pd.read_csv(csv_path)

    # Only realblock trials
    df = df[df["block"] == "realblock"]

    metrics = {
        "cognitive_flexibility": txt_name,
        "total_correct": (df["correct"] == 1).sum(),
        "total_incorrect": (df["correct"] == 2).sum(),
        "total_timeouts": (df["correct"] == 3).sum(),
    }

    # RTs only from correct trials
    rt_df = df[df["correct"] == 1]

    # Overall average RT
    metrics["avg_RT"] = rt_df["response_time"].mean()

    # Consistency-based RTs
    metrics["avg_RT_consistent"] = rt_df.loc[
        rt_df["consistency"] == 1, "response_time"
    ].mean()

    metrics["avg_RT_inconsistent"] = rt_df.loc[
        rt_df["consistency"] == 2, "response_time"
    ].mean()

    metrics["task_switch_cost"] = (
        metrics["avg_RT_inconsistent"] - metrics["avg_RT_consistent"]
    )

    # Congruency-based RTs
    metrics["avg_RT_congruent"] = rt_df.loc[
        rt_df["cong_in_number"] == 1, "response_time"
    ].mean()

    metrics["avg_RT_incongruent"] = rt_df.loc[
        rt_df["cong_in_number"] == 2, "response_time"
    ].mean()

    metrics["task_interference"] = (
        metrics["avg_RT_incongruent"] - metrics["avg_RT_congruent"]
    )

    results.append(metrics)

# Metrics dataframe
metrics_df = pd.DataFrame(results)

# Merge back into init data
final_df = init_df.merge(
    metrics_df,
    on="cognitive_flexibility",
    how="left"
)

# Save final results
final_df.to_csv("results.csv", index=False)

final_df.head()
