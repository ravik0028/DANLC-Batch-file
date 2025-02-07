import matplotlib.pyplot as plt

# Data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Plot
plt.figure(figsize=(7,7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140,
        colors=['blue', 'orange', 'green', 'red', 'purple'])
plt.title("Monthly Income Distribution")
plt.show()
