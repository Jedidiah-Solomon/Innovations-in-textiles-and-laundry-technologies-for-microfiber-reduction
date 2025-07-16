import matplotlib.pyplot as plt


years = [2020, 2021, 2022, 2023, 2024, 2025]
counts = [97, 118, 113, 118, 146, 93]

plt.figure(figsize=(9, 5))
plt.bar(years, counts, color='teal')
plt.title('Research Trend on Microfibre Pollution (2020–2025) - July 2025', fontsize=14)
plt.xlabel('Publication Year', fontsize=12)
plt.ylabel('Number of Publications', fontsize=12)
plt.xticks(years)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
