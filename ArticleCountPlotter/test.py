
import matplotlib.pyplot as plt

# Prepare your data
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 25, 40]

# Create a horizontal bar plot using Matplotlib
plt.barh(categories, values, color='skyblue')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Plot Example')

# Add numbers on top of bars
for index, value in enumerate(values):
    plt.text(value, index, str(value))

# Show plot
plt.show()
