import matplotlib.pyplot as plt

Ingredient = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
variables = [0.176, 0.3, 0.085, 0.185, 0.3]

plt.barh(Ingredient, variables, color='purple')

plt.title('BARCHART')
plt.xlabel('Proportion of Total')

plt.show()
