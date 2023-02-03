import numpy as np

country = np.array(["Canada", "Canada", "Canada", "Germany", "Argentina", "Germany", "Argentina"])
price = np.array([250, 250, 100, 120, 50, 80, 38])

# Crear una máscara para obtener los índices del array
# que corresponden al país Canada
mask_0 = country == "Canada"
mask_1 = country == "Germany"
mask_2 = country == "Argentina"

# Utilizo la máscara para acceder a los indices del array price
# que corresponden a canada
ventas_canada = price[mask_0]
ventas_germany = price[mask_1]
ventas_argentina = price[mask_2]

suma_canada = np.sum(ventas_canada)
suma_germany = np.sum(ventas_germany)
suma_argentina = np.sum(ventas_argentina)
print(suma_canada, suma_germany, suma_argentina)