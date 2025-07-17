#CONFUSION MATRIX

import matplotlib.pyplot as plt import seaborn as sns
import pandas as pd
# Confusion matrix data confusion_data = {
"Predicted Drowsy": [138, 11],
"Predicted Not Drowsy": [2, 249] }
confusion_df = pd.DataFrame(confusion_data, index=["Actual Drowsy", "Actual Not Drowsy"])
# Performance metrics metrics = {
"Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
"Value": [96.4, 92.6, 98.6, 95.5] }
metrics_df = pd.DataFrame(metrics)
# Plotting the confusion matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_df, annot=True, fmt="d", cmap="Blues") plt.title("Confusion Matrix")
plt.ylabel("Actual") plt.xlabel("Predicted") plt.tight_layout() plt.show()
