from TES7 import TES
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

# Densidad del Therminol obtenido de https://productcatalog.eastman.com/tds/ProdDatasheet.aspx?product=71093459&_gl=1*v6fy0t*_gcl_au*MTE0NDY3MTI3OC4xNzIyOTU1Nzc2#_ga=2.134840118.699663767.1722955776-699318640.1722955776
Therminol_density = 1060

oil_tes = TES(
    iron_volume = 2 * np.pi * (height_oil_tes * ((radius_oil_tes + steel_th_oil) ** 2 - radius_oil_tes ** 2) + 2 * steel_th_oil * radius_oil_tes ** 2),  # m³
    insulation_volume = 2 * np.pi * (height_oil_tes * ((radius_oil_tes + steel_th_oil + ins_th_oil) ** 2 - (radius_oil_tes + steel_th_oil) ** 2) + 2 * ins_th_oil * radius_oil_tes ** 2),  # m³
    price_per_cubic_meter_iron=1630,  # $/m³
    price_per_cubic_meter_insulation=7000,  # $/m³
    components=[("Therminol1",  Therminol_density/Therminol_cost_kg, np.pi * height_oil_tes * radius_oil_tes**2 )] #m3
    # components=[("Pump", 2000, 2), ("Valve", 300, 4)]  # list of components
)

oil_tes.set_additional_parameters(
    temporal_adjustment_index=1,
    installation_percentage=0,
    annual_discount_rate=0.07,
    service_years=30,
    tes_energy_capacity=37500,
    cycles_per_year=365,
    tes_efficiency = 0.7
)
oil_tes.display_info()

capex_pereira =     oil_tes.capex_pereira()
print(f"CAPEX Pereira: {capex_pereira}")

lcos = oil_tes.LCOS()
print(f"LCOS: {lcos}")


"""
Estudio de Touzo (basado en el informe de Lucas Pereira)
"""
tes_touzo = TES(
    iron_volume = 1,
    insulation_volume=6.45,
    price_per_cubic_meter_iron=1737.47,
    price_per_cubic_meter_insulation=2432.64,
    components=[("válvulas", 242.82, 8)]
)

tes_touzo.set_additional_parameters(
)

