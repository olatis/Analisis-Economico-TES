from TES_object import TES
from Flujo_de_caja import calcular_flujo_de_caja



# Create an instance of the TES object with example data
tes_system = TES(
    iron_volume=2785,  # m³
    insulation_volume=50.0,  # m³
    price_per_cubic_meter_iron=200,  # $/m³
    price_per_cubic_meter_insulation=50,  # $/m³
    components=[]
    # components=[("Pump", 2000, 2), ("Valve", 300, 4)]  # list of components
)

# Set additional parameters
tes_system.set_additional_parameters(
    density_tes_material=3500,  # kg/m³
    volume_tes_material=1200.0,  # m³
    specific_heat_tes_material=1,  # kJ/(kg·K)
    temperature_difference=300,  # K
    tes_efficiency=0.9,
    k_mctigue=0.02,
    initial_pressure=101325,  # Pa (1 atm)
    final_pressure=202650,  # Pa (2 atm)
    temporal_adjustment_index=1.05,
    installation_percentage=0.15,
    cycles_per_year=250,
    service_years=20,
    electricity_cost_per_joule=0.00005,  # $/J
    fan_efficiency=0.85,
    charging_time=5,  # hours
    discharging_time=5,  # hours
    working_fluid_flow=0.1,  # m³/s
    flow_section_area=0.5,  # m²
    working_fluid_density=1000,  # kg/m³
    capex_maintenance_percentage=0.02,
    annual_discount_rate=0.05,
    tes_energy_capacity=2  # kWh
)

# Display TES system information
tes_system.display_info()

# Calculate different CAPEX values
capex_knobloch =    tes_system.capex_knobloch()
capex_kocher =      tes_system.capex_kocher()
capex_mctigue =     tes_system.capex_mctigue()
capex_trevisan =    tes_system.capex_trevisan()
capex_pereira =     tes_system.capex_pereira()

print(f"CAPEX Knobloch: {capex_knobloch}")
print(f"CAPEX Kocher: {capex_kocher}")
print(f"CAPEX McTigue: {capex_mctigue}")
print(f"CAPEX Trevisan: {capex_trevisan}")
print(f"CAPEX Pereira: {capex_pereira}")

# Calculate OPEX
opex = tes_system.opex()
print(f"OPEX: {opex}")

# Calculate LCOS
lcos = tes_system.LCOS()
print(f"LCOS: {lcos}")


# Parámetros de entrada
años = 5  # Número de años de análisis
precio_energia = 0.1  # Precio de venta de energía por kWh
produccion_anual = 1_000_000  # Producción anual de energía en kWh
subsidios = 50_000  # Subsidios anuales
costos_om = opex  # Costos de operación y mantenimiento anuales
costos_combustible = 0  # Costos de combustible anuales
costos_capital = 0  # Pagos de intereses y amortización de préstamos anuales
costos_seguro = 10_000  # Costos de seguro anuales
otros_costos = 5_000  # Otros costos anuales
inversion_inicial = capex_pereira  # Inversión inicial en la planta
tasa_impuestos = 0.25  # Tasa de impuestos sobre la renta
tasa_descuento = 0.1  # Tasa de descuento para el cálculo del VAN

# Llamada a la función calcular_flujo_de_caja
df_flujo_caja = calcular_flujo_de_caja(años, precio_energia, produccion_anual, subsidios, costos_om, costos_combustible, costos_capital, costos_seguro, otros_costos, inversion_inicial, tasa_impuestos, tasa_descuento)

# Mostrar el DataFrame resultante
print(df_flujo_caja)

# Guardar el DataFrame en un archivo Excel
df_flujo_caja.to_excel('flujo_caja_planta_energia.xlsx', index=False)

# Ejemplo de cómo acceder a datos específicos del DataFrame
año_especifico = 3  # Año específico para el que queremos los datos
van_año_especifico = df_flujo_caja.loc[df_flujo_caja['Año'] == año_especifico, 'VAN'].values[0]  # Obtener VAN del año específico
flujo_caja_libre_año_especifico = df_flujo_caja.loc[df_flujo_caja['Año'] == año_especifico, 'Flujo de Caja Libre'].values[0]  # Obtener flujo de caja libre del año específico

# Mostrar los datos específicos
print(f"VAN del año {año_especifico}: {van_año_especifico}")
print(f"Flujo de Caja Libre del año {año_especifico}: {flujo_caja_libre_año_especifico}")


