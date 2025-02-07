import matplotlib.pyplot as plt

# Data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Plot
plt.figure(figsize=(7,7))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140,
        colors=['cyan', 'magenta', 'yellow', 'gray'])
plt.title("Company Revenue Distribution")
plt.show()
