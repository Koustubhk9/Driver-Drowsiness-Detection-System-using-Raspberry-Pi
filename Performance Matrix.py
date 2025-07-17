#PERFORMANCE METRICS

# Plotting bar graph for metrics
plt.figure(figsize=(8, 5))
sns.barplot(x="Metric", y="Value", data=metrics_df, palette="viridis") plt.ylim(0, 100)
plt.title("Performance Metrics")
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.show()
