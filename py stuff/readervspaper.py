import matplotlib.pyplot as plt

# Data
years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
e_reader_cost = [200, 180, 160, 140, 120, 100, 90, 80]
paper_cost = [5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, e_reader_cost, marker='o', label='E-reader Device Cost (USD)')
plt.plot(years, paper_cost, marker='o', label='Paper Cost (per ream, USD)', color='orange')

# Adding titles and labels
plt.title('Cost of E-reader Device and Paper Over Time')
plt.xlabel('Year')
plt.ylabel('Cost (USD)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
