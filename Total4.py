import numpy as np
from scipy.optimize import minimize

# Parámetros proporcionados
height = [7.5, 11.5, 13]  # m
radius = [13, 15, 17]  # m
steel_th = [0.06, 0.07, 0.08]  # m
ins_th = [0.03, 0.04, 0.05]  # m

htf_volume = [np.pi* a * b**2 for a,b in zip(height, radius)]
iron_volume = [2 * np.pi * (a * ((b + c) ** 2 - b ** 2) + 2 * c * b ** 2) for a, b, c in zip(height, radius, steel_th)]  # m³
insulation_volume = [2 * np.pi * (a * ((b + c + d) ** 2 - (b + c) ** 2) + 2 * d * b ** 2) for a, b, c, d in zip(height, radius, steel_th, ins_th)]  # m³

target_capex_pereira = [1.86e6, 3.72e6, 5.58e6]  # USD
temporal_adjustment_index = 1
installation_percentage = 0



# Costo del Therminol (aceite del estanque) obtenido de https://www.zauba.com/importanalysis-therminol+vp1-report.html
Therminol_cost_kg = 5

# Densidad del Therminol obtenido de https://productcatalog.eastman.com/tds/ProdDatasheet.aspx?product=71093459&_gl=1*v6fy0t*_gcl_au*MTE0NDY3MTI3OC4xNzIyOTU1Nzc2#_ga=2.134840118.699663767.1722955776-699318640.1722955776
Therminol_density = 1060

# Lista de componentes adicionales
nuevo_componente = [
    [("Therminol1", Therminol_density/Therminol_cost_kg, htf_volume[0])],  # para el primer CAPEX
    [("Therminol2", Therminol_density/Therminol_cost_kg, htf_volume[1])],  # para el segundo CAPEX
    [("Therminol3", Therminol_density/Therminol_cost_kg, htf_volume[2])]   # para el tercer CAPEX
] 


# Función de cálculo de CAPEX Pereira
def capex_pereira(iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation
    components_cost = sum(price * quantity for name, price, quantity in components)
    installation_cost = installation_percentage * (iron_cost + insulation_cost + components_cost)
    capex = (iron_cost + insulation_cost + components_cost + installation_cost) * temporal_adjustment_index
    return capex

# Función de error para optimización
def error_function(prices):
    price_per_cubic_meter_iron, price_per_cubic_meter_insulation = prices
    errors = []
    for iron_vol, ins_vol, target_capex, additional_components in zip(iron_volume, insulation_volume, target_capex_pereira, nuevo_componente):
        calculated_capex = capex_pereira(iron_vol, ins_vol, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, additional_components)
        errors.append((calculated_capex - target_capex) ** 2)
    return sum(errors)



# Valores iniciales para la optimización
initial_guess = [1000, 100]  # suposiciones iniciales para los precios

# Optimización
result = minimize(error_function, initial_guess, method='Nelder-Mead')
optimal_prices = result.x

print(optimal_prices)
