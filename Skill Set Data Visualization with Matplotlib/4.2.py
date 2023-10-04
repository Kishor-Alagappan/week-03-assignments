import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [35000, 42000, 38000, 46000, 51000, 60000, 65000, 72000, 69000, 75000, 83000, 95000],
    'Profit': [5000, 6000, 5500, 7000, 7500, 9000, 9500, 10500, 10000, 11000, 12000, 13500],
    'Products_Sold': [300, 350, 320, 380, 400, 430, 450, 480, 460, 490, 520, 550]
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
x_label = 'Month'

# Line Plot for Sales
axs[0].plot(df['Month'], df['Sales'], 'bo-', label='Sales')
axs[0].set_title('Monthly Sales')
axs[0].set_xlabel(x_label)
axs[0].set_ylabel('Sales')
axs[0].legend()

# Scatter Plot for Profit
axs[1].scatter(df['Month'], df['Profit'], marker='x', color='r', label='Profit')
axs[1].set_title('Monthly Profit')
axs[1].set_xlabel(x_label)
axs[1].set_ylabel('Profit')
axs[1].legend()

# Bar Plot for Number of Products Sold
axs[2].bar(df['Month'], df['Products_Sold'], color='g', label='Products Sold')
axs[2].set_title('Number of Products Sold')
axs[2].set_xlabel(x_label)
axs[2].set_ylabel('Products Sold')
axs[2].legend()

plt.tight_layout()

plt.show()


