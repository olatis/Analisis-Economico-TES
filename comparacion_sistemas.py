from TES_object import TES
import numpy as np




"""
Objeto TES (Orsini et al. 2021)
"""

height_oil_tes = 11.5 # m
radius_oil_tes = 15 # m
steel_th_oil = 0.07 # m
ins_th_oil = 0.04 # m

# Costo del Therminol (aceite del estanque) obtenido de https://www.zauba.com/importanalysis-therminol+vp1-report.html
Therminol_cost_kg = 5

# Propiedades del therminol asumiendo que entra a la temperatura que sale del campo solar
T_ent = 393
T_sal = 350
p_ent = 1e4
p_sal = 1e3

# Densidad del Therminol obtenido de https://productcatalog.eastman.com/tds/ProdDatasheet.aspx?product=71093459&_gl=1*v6fy0t*_gcl_au*MTE0NDY3MTI3OC4xNzIyOTU1Nzc2#_ga=2.134840118.699663767.1722955776-699318640.1722955776
Therminol_density = 700

# Información sacada de los gráficos de Orsini
m_charge = 230 # m3/h
m_discharge = 590 #m3/h
t_charge = 9 # h
t_discharge = 4 # h

oil_tes = TES(
    iron_volume = 2 * np.pi * (height_oil_tes * ((radius_oil_tes + steel_th_oil) ** 2 - radius_oil_tes ** 2) + 2 * steel_th_oil * radius_oil_tes ** 2),  # m³
    insulation_volume = 2 * np.pi * (height_oil_tes * ((radius_oil_tes + steel_th_oil + ins_th_oil) ** 2 - (radius_oil_tes + steel_th_oil) ** 2) + 2 * ins_th_oil * radius_oil_tes ** 2),  # m³
    price_per_cubic_meter_iron=1630,  # $/m³
    price_per_cubic_meter_insulation=7000,  # $/m³
    components=[("Therminol1",  1.5*Therminol_density/Therminol_cost_kg, np.pi * height_oil_tes * radius_oil_tes**2 )] #m3
    # components=[("Pump", 2000, 2), ("Valve", 300, 4)]  # list of components
)

oil_tes.set_additional_parameters(
    temporal_adjustment_index=1,
    installation_percentage=0,
    annual_discount_rate=0.07,
    service_years=30,
    tes_energy_capacity=37500,
    cycles_per_year=365,
    tes_efficiency = 0.7,
    # datos posteriores ?? revisar
    delta_pressure_charge = p_ent-p_sal, # Ajustar
    delta_pressure_discharge = p_ent-p_sal, # Ajustar
    mass_flow_rate_charge = m_charge*Therminol_density,
    mass_flow_rate_discharge = m_discharge*Therminol_density,
    working_fluid_density = Therminol_density, # ajuste simple 
    charging_time = t_charge,
    discharging_time = t_discharge,
    # Datos asumidos en base a Lucas
    electricity_cost_per_joule = 0.396,
    fan_efficiency = 0.95,
    capex_maintenance_percentage = 0.02

)
oil_tes.display_info()

print("TES Orsini")

capex_pereira_oil_tes =     oil_tes.capex_pereira()
print(f"CAPEX Pereira: {capex_pereira_oil_tes}")

opex_oil_tes = oil_tes.opex()
print(f"OPEX: {opex_oil_tes}")

lcos_oil_tes = oil_tes.LCOS()
print(f"LCOS: {lcos_oil_tes}")


"""
Estudio de Touzo (basado en el informe de Lucas Pereira)
"""
tes_touzo = TES(
    iron_volume = 1,
    insulation_volume=6.45,
    price_per_cubic_meter_iron=1737.47,
    price_per_cubic_meter_insulation=2432.64,
    components=[("válvulas", 242.82, 8), ("ventilador", 475.94, 1), ("Resistencia", 4241.31, 1)]
)

tes_touzo.set_additional_parameters(
    # Datos Capex Pereira
    temporal_adjustment_index = 1,
    installation_percentage = 0.15,
    # Datos Capex Kosher
    density_tes_material = 3005,
    volume_tes_material = 8.9,
    specific_heat_tes_material = 0.7527,
    temperature_difference = 300,
    tes_efficiency = 0.89,
    # Datos Opex
    delta_pressure_charge = 11000,
    delta_pressure_discharge = 1000,
    mass_flow_rate_charge = 0.58,
    mass_flow_rate_discharge = 0.65,
    working_fluid_density = 1.274,
    charging_time = 32400/3600,
    discharging_time = 14400/3600,
    cycles_per_year = 365,
    service_years = 30,
    electricity_cost_per_joule = 0.396,
    fan_efficiency = 0.95,
    capex_maintenance_percentage = 0.02,
    # Datos LCOS
    annual_discount_rate = 0.07,
    tes_energy_capacity = 1900
)

print("TES Touzo")

capex_pereira_touzo =     tes_touzo.capex_pereira()
print(f"CAPEX Pereira: {capex_pereira_touzo}")

opex_touzo = tes_touzo.opex()
print(f"OPEX: {opex_touzo}")

lcos_touzo = tes_touzo.LCOS()
print(f"LCOS: {lcos_touzo}")



"""
Estudio de Knobloch (de acuerdo a informe de Lucas Pereira)
"""

tes_knobloch = TES(
    iron_volume = 1,
    insulation_volume=1,
    price_per_cubic_meter_iron=154374.21,
    price_per_cubic_meter_insulation=18059.28,
    components=[("válvulas", 4493.06, 1), ("ventilador", 5221.96, 1), ("Resistencia", 7941.73, 1)]
)

tes_knobloch.set_additional_parameters(
    # Datos Capex Pereira
    temporal_adjustment_index = 799.1/761.4,
    installation_percentage = 0.15,
    # Datos Capex Kosher
    density_tes_material = 3007,
    volume_tes_material = 3.2,
    specific_heat_tes_material = 1.12,
    temperature_difference = 600,
    tes_efficiency = 0.807,
    # Datos Opex
    delta_pressure_charge = 900,
    delta_pressure_discharge = 900,
    mass_flow_rate_charge = 0.50283,
    mass_flow_rate_discharge = 0.64450,
    working_fluid_density = 1.293,
    charging_time = 86400/3600,
    discharging_time = 86400/3600,
    cycles_per_year = 182.5,
    service_years = 30,
    electricity_cost_per_joule = 0.396,
    fan_efficiency = 0.95,
    capex_maintenance_percentage = 0.02,
    # Datos LCOS
    annual_discount_rate = 0.07,
    tes_energy_capacity = 1007
)

print("TES Knobloch")

capex_pereira_knobloch = tes_knobloch.capex_pereira()
print(f"CAPEX Pereira: {capex_pereira_knobloch}")

opex_knobloch = tes_knobloch.opex()
print(f"OPEX: {opex_knobloch}")

lcos_knobloch = tes_knobloch.LCOS()
print(f"LCOS: {lcos_knobloch}")



"""
Estudio de Experimento (de acuerdo a informe de Lucas Pereira)
"""

tes_experimento = TES(
    iron_volume = 1,
    insulation_volume = 1,
    price_per_cubic_meter_iron = 1590,
    price_per_cubic_meter_insulation = 507.884,
    components = [("válvulas", 242.82, 8), ("ventilador", 475.94, 1), ("Resistencia", 4241.31, 1)]
)

tes_experimento.set_additional_parameters(
    # Datos Capex Pereira
    temporal_adjustment_index = 1,
    installation_percentage = 0.15,
    # Datos Capex Kosher
    density_tes_material = 3700,
    volume_tes_material = 0.225,
    specific_heat_tes_material = 1.45,
    temperature_difference = 400,
    tes_efficiency = 0.724,
    # Datos Opex
    delta_pressure_charge = 133.41,
    delta_pressure_discharge = 133.41,
    mass_flow_rate_charge = 1.013,
    mass_flow_rate_discharge = 1.013,
    working_fluid_density = 1.225,
    charging_time = 28800 / 3600,
    discharging_time = 43200 / 3600,
    cycles_per_year = 365,
    service_years = 30,
    electricity_cost_per_joule = 0.396,
    fan_efficiency = 0.95,
    capex_maintenance_percentage = 0.02,
    # Datos LCOS
    annual_discount_rate = 0.07,
    tes_energy_capacity = 169.66
)

print("TES Experimento")

capex_pereira_experimento = tes_experimento.capex_pereira()
print(f"CAPEX Pereira: {capex_pereira_experimento}")

opex_experimento = tes_experimento.opex()
print(f"OPEX: {opex_experimento}")

lcos_experimento = tes_experimento.LCOS()
print(f"LCOS: {lcos_experimento}")
