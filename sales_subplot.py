import pandas as pd
import matplotlib.pyplot as plt

# Sample Data (Replace this with actual file path)
data = {
    'Date': pd.date_range(start='1/1/2023', periods=12, freq='ME').tolist() * 3,
    'Region': ['North'] * 12 + ['South'] * 12 + ['West'] * 12,
    'Sales': [200, 220, 250, 270, 300, 320, 310, 330, 350, 370, 390, 400,
              150, 170, 190, 210, 230, 250, 260, 270, 280, 290, 300, 310,
              180, 190, 200, 210, 220, 230, 250, 270, 280, 290, 300, 310]
}
df = pd.DataFrame(data)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Get unique regions
regions = df['Region'].unique()

# Create subplots
fig, axes = plt.subplots(len(regions), 1, figsize=(10, 6), sharex=True)
fig.suptitle("Sales Figures by Region Over Time")

# Plot data for each region
for ax, region in zip(axes, regions):
    region_data = df[df['Region'] == region]
    ax.plot(region_data['Date'], region_data['Sales'], marker='o', label=region)
    ax.set_title(region)
    ax.set_ylabel("Sales")
    ax.legend()

# Formatting
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
