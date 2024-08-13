from TES7 import TES
import numpy as np


#relación de costos
rel_1 = 0.81
rel_2 = 0.85

# Datos conocidos
height = 11.5 # m
radius = 15 # m
steel_th = 0.07 # m
ins_th = 0.04 # m
total_volume = height*radius
iron_volume = 2*height*((radius+steel_th)**2 - radius**2)  # m³
insulation_volume = 2*height*np.pi*((radius+steel_th+ins_th)**2 - (radius+steel_th)**2)  # m³
components = []  # lista de componentes
target_capex_pereira = 3.72 * 1e6  # 3.72 millones de USD

# Parámetros adicionales
additional_parameters = {
    "temporal_adjustment_index": 1,
    "installation_percentage": 0
    # Agregar otros parámetros adicionales si son necesarios
}

# Limites de precios
min_price_iron = target_capex_pereira*rel_1/iron_volume
max_price_iron = target_capex_pereira*rel_2/iron_volume
min_price_insulation = target_capex_pereira*(1-rel_2)/insulation_volume
max_price_insulation = target_capex_pereira*(1-rel_1)/insulation_volume

price_per_cubic_meter_insulation_limits = (min_price_iron, max_price_iron)  # $/m³
price_per_cubic_meter_iron_limits = (min_price_insulation, max_price_insulation)  # $/m³

# price_per_cubic_meter_insulation_limits = (0, 3*1e6)  # $/m³
# price_per_cubic_meter_iron_limits = (0, 3*1e6)  # $/m³



# Crear una instancia del objeto TES con datos iniciales
tes_system = TES(
    iron_volume=iron_volume,
    insulation_volume=insulation_volume,
    price_per_cubic_meter_iron=0,  # inicializar con 0
    price_per_cubic_meter_insulation=0,  # inicializar con 0
    components=components
)

# Configuración de parámetros adicionales
tes_system.set_additional_parameters(**additional_parameters)

# Función para encontrar los precios ajustados
def find_adjusted_prices(target_capex, iron_limits, insulation_limits, tes_system):
    iron_price_range = np.linspace(iron_limits[0], iron_limits[1], 1000)
    insulation_price_range = np.linspace(insulation_limits[0], insulation_limits[1], 1000)
    
    best_error = float('inf')
    best_prices = (0, 0)
    
    for iron_price in iron_price_range:
        for insulation_price in insulation_price_range:
            tes_system.price_per_cubic_meter_iron = iron_price
            tes_system.price_per_cubic_meter_insulation = insulation_price
            try:
                capex = tes_system.capex_pereira()
                if isinstance(capex, str):
                    # Si capex es un string, significa que hay un error o falta de datos
                    print(f"Error al calcular CAPEX con hierro {iron_price} y aislamiento {insulation_price}: {capex}")
                    continue
                error = abs(capex - target_capex)
                if error < best_error:
                    best_error = error
                    best_prices = (iron_price, insulation_price)
            except Exception as e:
                # Captura cualquier excepción que ocurra durante el cálculo del CAPEX
                print(f"Excepción al calcular CAPEX con hierro {iron_price} y aislamiento {insulation_price}: {e}")
    
    return best_prices, best_error

# Encontrar los precios ajustados
best_prices, best_error = find_adjusted_prices(target_capex_pereira, price_per_cubic_meter_iron_limits, price_per_cubic_meter_insulation_limits, tes_system)

print(f"Mejor precio por m³ de hierro: {best_prices[0]} USD/m³")
print(f"Mejor precio por m³ de aislación: {best_prices[1]} USD/m³")
print(f"Error en CAPEX: {best_error} USD")
