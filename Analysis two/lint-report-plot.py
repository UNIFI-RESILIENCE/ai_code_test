import json
from collections import Counter
import matplotlib.pyplot as plt

# Load JSON data from file
with open("qwenhuman1_pylint-report.json", "r") as file:
    lint_data = json.load(file)

# Count occurrences of each 'type'
type_counts = Counter(entry['type'] for entry in lint_data)

# Prepare data for plotting
types = list(type_counts.keys())
counts = list(type_counts.values())

# Plot the data
plt.figure(figsize=(8, 5))
plt.bar(types, counts, color='tomato')
plt.xlabel('Issue Type')
plt.ylabel('Number of Occurrences')
plt.title('Pylint Report Summary by Issue Type')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
