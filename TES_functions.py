def capex_knobloch(iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
    """
    Calcula el CAPEX utilizando el método de Knobloch.

    Parámetros:
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.
    - components (list of tuples): Lista de componentes, donde cada componente es una tupla con el nombre, el precio por unidad y la cantidad.

    Retorna:
    - float: El CAPEX calculado.
    """
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation
    components_cost = sum(price * quantity for name, price, quantity in components)
    capex = iron_cost + insulation_cost + components_cost
    return capex

def capex_kocher(density_tes_material, volume_tes_material, specific_heat_tes_material, temperature_difference, tes_efficiency, 
                 iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation):
    """
    Calcula el CAPEX utilizando el método de Kocher.

    Parámetros:
    - density_tes_material (float): Densidad del material TES en kg/m³.
    - volume_tes_material (float): Volumen del material TES en m³.
    - specific_heat_tes_material (float): Calor específico del material TES en kJ/(kg·K).
    - temperature_difference (float): Diferencia de temperatura en K.
    - tes_efficiency (float): Eficiencia del TES.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.

    Retorna:
    - float: El CAPEX calculado.
    """
    etes = (density_tes_material * specific_heat_tes_material * temperature_difference) / 3600
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation
    capex = (iron_cost + insulation_cost) / (etes * volume_tes_material * tes_efficiency)
    return capex

def capex_mctigue(k_mctigue, volume_tes_material, final_pressure, iron_volume, price_per_cubic_meter_iron):
    """
    Calcula el CAPEX utilizando el método de McTigue.

    Parámetros:
    - k_mctigue (float): Coeficiente de McTigue.
    - volume_tes_material (float): Volumen del material TES en m³.
    - final_pressure (float): Presión final en Pa.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.

    Retorna:
    - float: El CAPEX calculado.
    """
    iron_cost = iron_volume * price_per_cubic_meter_iron
    mctigue_cost = k_mctigue * volume_tes_material * final_pressure
    capex = iron_cost + mctigue_cost
    return capex

def capex_trevisan(temporal_adjustment_index, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation):
    """
    Calcula el CAPEX utilizando el método de Trevisan.

    Parámetros:
    - temporal_adjustment_index (float): Índice de ajuste temporal.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.

    Retorna:
    - float: El CAPEX calculado.
    """
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation * temporal_adjustment_index
    capex = iron_cost + insulation_cost
    return capex

def capex_pereira(temporal_adjustment_index, installation_percentage, iron_volume, insulation_volume, price_per_cubic_meter_iron, 
                  price_per_cubic_meter_insulation, components):
    """
    Calcula el CAPEX utilizando el método de Pereira.

    Parámetros:
    - temporal_adjustment_index (float): Índice de ajuste temporal.
    - installation_percentage (float): Porcentaje de instalación.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.
    - components (list of tuples): Lista de componentes, donde cada componente es una tupla con el nombre, el precio por unidad y la cantidad.

    Retorna:
    - float: El CAPEX calculado.
    """
    iron_cost = iron_volume * price_per_cubic_meter_iron
    insulation_cost = insulation_volume * price_per_cubic_meter_insulation * temporal_adjustment_index
    components_cost = sum(price * quantity for name, price, quantity in components)
    capex = (iron_cost + insulation_cost + components_cost) * (1 + installation_percentage)
    return capex

def opex(initial_pressure, final_pressure, working_fluid_flow, working_fluid_density, charging_time, discharging_time, cycles_per_year, 
         service_years, electricity_cost_per_joule, fan_efficiency, capex_maintenance_percentage, iron_volume, insulation_volume, 
         price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
    """
    Calcula el OPEX del sistema TES.

    Parámetros:
    - initial_pressure (float): Presión inicial en Pa.
    - final_pressure (float): Presión final en Pa.
    - working_fluid_flow (float): Flujo del fluido de trabajo en m³/s.
    - working_fluid_density (float): Densidad del fluido de trabajo en kg/m³.
    - charging_time (float): Tiempo de carga en horas.
    - discharging_time (float): Tiempo de descarga en horas.
    - cycles_per_year (float): Ciclos por año.
    - service_years (float): Años de servicio.
    - electricity_cost_per_joule (float): Costo de electricidad por joule en dólares.
    - fan_efficiency (float): Eficiencia del ventilador.
    - capex_maintenance_percentage (float): Porcentaje de mantenimiento del CAPEX.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.
    - components (list of tuples): Lista de componentes, donde cada componente es una tupla con el nombre, el precio por unidad y la cantidad.

    Retorna:
    - float: El OPEX calculado.
    """
    delta_pressure = final_pressure - initial_pressure
    charge_term = (working_fluid_flow * delta_pressure / working_fluid_density) * charging_time
    discharge_term = (working_fluid_flow * delta_pressure / working_fluid_density) * discharging_time
    capex = capex_knobloch(iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components)
    opex = (cycles_per_year / service_years) * (electricity_cost_per_joule / fan_efficiency) * (charge_term + discharge_term) + (capex_maintenance_percentage * capex) / service_years
    return opex

def LCOS(annual_discount_rate, tes_energy_capacity, cycles_per_year, service_years, tes_efficiency, iron_volume, insulation_volume, 
         price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components, initial_pressure, final_pressure, working_fluid_flow, 
         working_fluid_density, charging_time, discharging_time, electricity_cost_per_joule, fan_efficiency, capex_maintenance_percentage):
    """
    Calcula el Costo Nivelado de Almacenamiento de Energía (LCOS).

    Parámetros:
    - annual_discount_rate (float): Tasa de descuento anual.
    - tes_energy_capacity (float): Capacidad de energía del TES en kWh.
    - cycles_per_year (float): Ciclos por año.
    - service_years (float): Años de servicio.
    - tes_efficiency (float): Eficiencia del TES.
    - iron_volume (float): Volumen de acero en metros cúbicos.
    - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
    - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
    - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.
    - components (list of tuples): Lista de componentes, donde cada componente es una tupla con el nombre, el precio por unidad y la cantidad.
    - initial_pressure (float): Presión inicial en Pa.
    - final_pressure (float): Presión final en Pa.
    - working_fluid_flow (float): Flujo del fluido de trabajo en m³/s.
    - working_fluid_density (float): Densidad del fluido de trabajo en kg/m³.
    - charging_time (float): Tiempo de carga en horas.
    - discharging_time (float): Tiempo de descarga en horas.
    - electricity_cost_per_joule (float): Costo de electricidad por joule en dólares.
    - fan_efficiency (float): Eficiencia del ventilador.
    - capex_maintenance_percentage (float): Porcentaje de mantenimiento del CAPEX.

    Retorna:
    - float: El LCOS calculado.
    """
    capex = capex_knobloch(iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components)
    opex_total = sum(opex(initial_pressure, final_pressure, working_fluid_flow, working_fluid_density, charging_time, discharging_time, cycles_per_year, 
                          service_years, electricity_cost_per_joule, fan_efficiency, capex_maintenance_percentage, iron_volume, insulation_volume, 
                          price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components) / (1 + annual_discount_rate) ** n 
                     for n in range(1, service_years + 1))
    total_cycles = sum(cycles_per_year * tes_energy_capacity * tes_efficiency / (1 + annual_discount_rate) ** n for n in range(1, service_years + 1))
    lcos = (capex + opex_total) / total_cycles
    return lcos

# Ejemplo de uso

# Datos de entrada
iron_volume = 100.0  # m³
insulation_volume = 50.0  # m³
price_per_cubic_meter_iron = 200  # $/m³
price_per_cubic_meter_insulation = 50  # $/m³
components = [("Pump", 5000, 2), ("Valve", 1500, 4)]  # lista de componentes

density_tes_material = 1600  # kg/m³
volume_tes_material = 1200.0  # m³
specific_heat_tes_material = 1  # kJ/(kg·K)
temperature_difference = 300  # K
tes_efficiency = 0.9
k_mctigue = 0.02
initial_pressure = 101325  # Pa (1 atm)
final_pressure = 202650  # Pa (2 atm)
temporal_adjustment_index = 1.05
installation_percentage = 0.15
cycles_per_year = 250
service_years = 20
electricity_cost_per_joule = 0.00005  # $/J
fan_efficiency = 0.85
charging_time = 5  # horas
discharging_time = 5  # horas
working_fluid_flow = 0.1  # m³/s
working_fluid_density = 1000  # kg/m³
capex_maintenance_percentage = 0.02
annual_discount_rate = 0.05
tes_energy_capacity = 2  # kWh

# Calcular diferentes valores de CAPEX
capex_knobloch_value = capex_knobloch(iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components)
capex_kocher_value = capex_kocher(density_tes_material, volume_tes_material, specific_heat_tes_material, temperature_difference, tes_efficiency, 
                                  iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation)
capex_mctigue_value = capex_mctigue(k_mctigue, volume_tes_material, final_pressure, iron_volume, price_per_cubic_meter_iron)
capex_trevisan_value = capex_trevisan(temporal_adjustment_index, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation)
capex_pereira_value = capex_pereira(temporal_adjustment_index, installation_percentage, iron_volume, insulation_volume, price_per_cubic_meter_iron, 
                                    price_per_cubic_meter_insulation, components)

print(f"CAPEX Knobloch: ${capex_knobloch_value:.2f}")
print(f"CAPEX Kocher: ${capex_kocher_value:.2f}")
print(f"CAPEX McTigue: ${capex_mctigue_value:.2f}")
print(f"CAPEX Trevisan: ${capex_trevisan_value:.2f}")
print(f"CAPEX Pereira: ${capex_pereira_value:.2f}")

# Calcular OPEX
opex_value = opex(initial_pressure, final_pressure, working_fluid_flow, working_fluid_density, charging_time, discharging_time, cycles_per_year, 
                  service_years, electricity_cost_per_joule, fan_efficiency, capex_maintenance_percentage, iron_volume, insulation_volume, 
                  price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components)
print(f"OPEX: ${opex_value:.2f}")

# Calcular LCOS
lcos_value = LCOS(annual_discount_rate, tes_energy_capacity, cycles_per_year, service_years, tes_efficiency, iron_volume, insulation_volume, 
                  price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components, initial_pressure, final_pressure, working_fluid_flow, 
                  working_fluid_density, charging_time, discharging_time, electricity_cost_per_joule, fan_efficiency, capex_maintenance_percentage)
print(f"LCOS: ${lcos_value:.2f} $/kWh")
