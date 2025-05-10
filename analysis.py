import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Intel_Fab_Dataset.csv")  # Make sure this file is uploaded to the repo
print("Preview of data:")
print(df.head())

# Summary: Cycle & Queue Time by Fab Step
summary = df.groupby("Fab_Step")[["Cycle_Time_Sec", "Queue_Time_Sec"]].mean()
print("\nCycle & Queue Time by Fab Step:\n", summary)

# Save summary table to CSV
summary.to_csv("summary_cycle_queue_by_step.csv")

sns.set(style="whitegrid")

# 1. Avg Cycle Time
sns.barplot(x=summary.index, y=summary["Cycle_Time_Sec"])
plt.title("Avg Cycle Time by Fab Step")
plt.ylabel("Cycle Time (s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("cycle_time_by_step.png")
plt.clf()

# 2. Avg Queue Time
sns.barplot(x=summary.index, y=summary["Queue_Time_Sec"])
plt.title("Avg Queue Time by Fab Step")
plt.ylabel("Queue Time (s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("queue_time_by_step.png")
plt.clf()

# 3. Machine Status Pie Chart
status_counts = df["Machine_Status"].value_counts()
status_counts.plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Machine Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("machine_status_pie.png")
plt.clf()

# 4. Wafer Yield Distribution
sns.histplot(df["Wafer_Yield_Percent"], bins=30, kde=True)
plt.title("Wafer Yield Distribution")
plt.xlabel("Yield (%)")
plt.tight_layout()
plt.savefig("wafer_yield_distribution.png")
plt.clf()

# 5. Defect Count Distribution
sns.histplot(df["Defect_Count"], bins=20)
plt.title("Defect Count Distribution")
plt.xlabel("Defects")
plt.tight_layout()
plt.savefig("defect_distribution.png")
plt.clf()

# 6. Correlation Matrix
corr = df[["Cycle_Time_Sec", "Queue_Time_Sec", "Wafer_Yield_Percent", "Defect_Count"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.clf()

# 7. Cycle Time Over Time
df_sorted = df.sort_values("Run_Timestamp")
plt.figure(figsize=(12, 6))
plt.plot(df_sorted["Run_Timestamp"], df_sorted["Cycle_Time_Sec"], alpha=0.3)
plt.title("Cycle Time Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Cycle Time (s)")
plt.tight_layout()
plt.savefig("cycle_time_over_time.png")
plt.clf()

# 8. Queue Time vs Defect Count
sns.scatterplot(data=df, x="Queue_Time_Sec", y="Defect_Count", alpha=0.3)
plt.title("Queue Time vs Defect Count")
plt.xlabel("Queue Time (s)")
plt.ylabel("Defect Count")
plt.tight_layout()
plt.savefig("queue_vs_defects.png")
plt.clf()
