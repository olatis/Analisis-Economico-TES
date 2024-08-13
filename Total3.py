import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (sustituir con tus datos)
temporal_adjustment_index = 1.05
installation_percentage = 0.10
iron_volume = np.array([100, 150, 200, 250, 300])
insulation_volume = np.array([50, 75, 100, 125, 150])
price_per_cubic_meter_iron = np.linspace(500, 1500, 5)  # supongamos precios entre 500 y 1500 USD/m³
price_per_cubic_meter_insulation = np.linspace(200, 800, 5)  # supongamos precios entre 200 y 800 USD/m³
components = [('Componente1', 1000, 2), ('Componente2', 1500, 3)]

# Función capex_pereira (copiada del archivo)
def capex_pereira(temporal_adjustment_index, installation_percentage, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation
    components_cost = sum(price * quantity for name, price, quantity in components)
    capex = (iron_cost + insulation_cost + components_cost) * temporal_adjustment_index * (1 + installation_percentage)
    return capex

# Calcular el CAPEX para cada combinación de precios
capex_values = capex_pereira(temporal_adjustment_index, installation_percentage, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components)

# Graficar los resultados
plt.figure(figsize=(10, 5))
plt.plot(price_per_cubic_meter_iron, capex_values, label='Precio Acero')
plt.plot(price_per_cubic_meter_insulation, capex_values, label='Precio Aislamiento')
plt.xlabel('Precio por metro cúbico (USD)')
plt.ylabel('CAPEX (USD)')
plt.title('CAPEX en función del precio del acero y del aislamiento')
plt.legend()
plt.grid(True)
plt.show()
