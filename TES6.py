import math

class TES:
    def __init__(self, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
        self.iron_volume = iron_volume
        self.insulation_volume = insulation_volume
        self.price_per_cubic_meter_iron = price_per_cubic_meter_iron
        self.price_per_cubic_meter_insulation = price_per_cubic_meter_insulation
        self.components = components

    def set_additional_parameters(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display_info(self):
        print(f"Iron Volume: {self.iron_volume} m³")
        print(f"Insulation Volume: {self.insulation_volume} m³")
        print(f"Price per Cubic Meter of Iron: ${self.price_per_cubic_meter_iron}")
        print(f"Price per Cubic Meter of Insulation: ${self.price_per_cubic_meter_insulation}")
        print("Components:")
        for component in self.components:
            print(f"  - {component[0]}: ${component[1]} x {component[2]}")

    def capex_knobloch(self):
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation
        components_cost = sum(price * quantity for name, price, quantity in self.components)
        capex = iron_cost + insulation_cost + components_cost
        return capex

    def capex_kocher(self):
        etes = (self.density_tes_material * self.specific_heat_tes_material * self.temperature_difference) / 3600
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation
        capex = (iron_cost + insulation_cost) / (etes * self.volume_tes_material * self.tes_efficiency)
        return capex

    def capex_mctigue(self):
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        mctigue_cost = self.k_mctigue * self.volume_tes_material * self.final_pressure
        capex = iron_cost + mctigue_cost
        return capex

    def capex_trevisan(self):
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation * self.temporal_adjustment_index
        capex = iron_cost + insulation_cost
        return capex

    def capex_pereira(self):
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation * self.temporal_adjustment_index
        components_cost = sum(price * quantity for name, price, quantity in self.components)
        capex = (iron_cost + insulation_cost + components_cost) * (1 + self.installation_percentage)
        return capex

    def opex(self):
        delta_pressure = self.final_pressure - self.initial_pressure
        charge_term = (self.working_fluid_flow * delta_pressure / self.working_fluid_density) * self.charging_time
        discharge_term = (self.working_fluid_flow * delta_pressure / self.working_fluid_density) * self.discharging_time
        opex = (self.cycles_per_year / self.service_years) * (self.electricity_cost_per_joule / self.fan_efficiency) * (charge_term + discharge_term) + (self.capex_maintenance_percentage * self.capex_knobloch()) / self.service_years
        return opex

    def LCOS(self):
        capex = self.capex_knobloch()
        opex_total = sum(self.opex() / (1 + self.annual_discount_rate) ** n for n in range(1, self.service_years + 1))
        total_cycles = sum(self.cycles_per_year * self.tes_energy_capacity * self.tes_efficiency / (1 + self.annual_discount_rate) ** n for n in range(1, self.service_years + 1))
        lcos = (capex + opex_total) / total_cycles
        return lcos

# Example usage
# Create an instance of the TES object with example data
tes_system = TES(
    iron_volume=100.0,  # m³
    insulation_volume=50.0,  # m³
    price_per_cubic_meter_iron=200,  # $/m³
    price_per_cubic_meter_insulation=50,  # $/m³
    components=[("Pump", 5000, 2), ("Valve", 1500, 4)]  # list of components
)

# Set additional parameters
tes_system.set_additional_parameters(
    density_tes_material=1600,  # kg/m³
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
capex_knobloch = tes_system.capex_knobloch()
capex_kocher = tes_system.capex_kocher()
capex_mctigue = tes_system.capex_mctigue()
capex_trevisan = tes_system.capex_trevisan()
capex_pereira = tes_system.capex_pereira()

print(f"CAPEX Knobloch: ${capex_knobloch:.2f}")
print(f"CAPEX Kocher: ${capex_kocher:.2f}")
print(f"CAPEX McTigue: ${capex_mctigue:.2f}")
print(f"CAPEX Trevisan: ${capex_trevisan:.2f}")
print(f"CAPEX Pereira: ${capex_pereira:.2f}")

# Calculate OPEX
opex = tes_system.opex()
print(f"OPEX: ${opex:.2f}")

# Calculate LCOS
lcos = tes_system.LCOS()
print(f"LCOS: ${lcos:.2f} $/kWh")
