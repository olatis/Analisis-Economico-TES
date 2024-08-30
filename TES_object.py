import math

class TES:
    def __init__(self, iron_volume, insulation_volume, price_per_cubic_meter_iron, price_per_cubic_meter_insulation, components):
        """
        Inicializa el objeto TES con los parámetros esenciales.

        Parámetros:
        - iron_volume (float): Volumen de acero en metros cúbicos.
        - insulation_volume (float): Volumen de aislamiento en metros cúbicos.
        - price_per_cubic_meter_iron (float): Precio por metro cúbico de acero en dólares.
        - price_per_cubic_meter_insulation (float): Precio por metro cúbico de aislamiento en dólares.
        - components (list of tuples): Lista de componentes, donde cada componente es una tupla con el nombre, el precio por unidad y la cantidad.
        """
        self.iron_volume = iron_volume
        self.insulation_volume = insulation_volume
        self.price_per_cubic_meter_iron = price_per_cubic_meter_iron
        self.price_per_cubic_meter_insulation = price_per_cubic_meter_insulation
        self.components = components

    def set_additional_parameters(self, **kwargs):
        """
        Establece los parámetros adicionales necesarios para los cálculos de costos.

        Parámetros:
        - kwargs: Diccionario de parámetros adicionales. Las claves son los nombres de los parámetros y los valores son los valores de los parámetros.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def check_parameters(self, required_params):
        """
        Verifica si los parámetros necesarios están presentes en el objeto.

        Parámetros:
        - required_params (dict): Diccionario de parámetros necesarios, donde las claves son los nombres de los parámetros y los valores son las unidades.

        Retorna:
        - list: Lista de tuplas con los nombres de los parámetros faltantes y sus unidades.
        """
        missing_params = []
        for param, unit in required_params.items():
            if not hasattr(self, param):
                missing_params.append((param, unit))
        return missing_params

    def display_info(self):
        """
        Muestra la información básica del sistema TES.
        """
        print(f"Iron Volume: {self.iron_volume} m³")
        print(f"Insulation Volume: {self.insulation_volume} m³")
        print(f"Price per Cubic Meter of Iron: ${self.price_per_cubic_meter_iron}")
        print(f"Price per Cubic Meter of Insulation: ${self.price_per_cubic_meter_insulation}")
        print("Components:")
        for component in self.components:
            print(f"  - {component[0]}: ${component[1]} x {component[2]}")

    def capex_knobloch(self):
        """
        Calcula el CAPEX utilizando el método de Knobloch.

        Retorna:
        - float o str: El CAPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {}
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation
        components_cost = sum(price * quantity for name, price, quantity in self.components)
        capex = iron_cost + insulation_cost + components_cost
        return capex

    def capex_kocher(self):
        """
        Calcula el CAPEX utilizando el método de Kocher.

        Retorna:
        - float o str: El CAPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'density_tes_material': 'kg/m³',
            'volume_tes_material': 'm³',
            'specific_heat_tes_material': 'kJ/(kg·K)',
            'temperature_difference': 'K',
            'tes_efficiency': '',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        etes = (self.density_tes_material * self.specific_heat_tes_material * self.temperature_difference) / 3600
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation
        capex = (iron_cost + insulation_cost) / (etes * self.volume_tes_material * self.tes_efficiency)
        return capex

    def capex_mctigue(self):
        """
        Calcula el CAPEX utilizando el método de McTigue.

        Retorna:
        - float o str: El CAPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'k_mctigue': '',
            'volume_tes_material': 'm³',
            'final_pressure': 'Pa',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        mctigue_cost = self.k_mctigue * self.volume_tes_material * self.final_pressure
        capex = iron_cost + mctigue_cost
        return capex

    def capex_trevisan(self):
        """
        Calcula el CAPEX utilizando el método de Trevisan, Kost, Calderon-Vasquez

        Retorna:
        - float o str: El CAPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'temporal_adjustment_index': '',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation * self.temporal_adjustment_index
        capex = iron_cost + insulation_cost
        return capex

    def capex_pereira(self):
        """
        Calcula el CAPEX utilizando el método de Pereira, Trevisan, Kost, Calderon-Vasquez

        Retorna:
        - float o str: El CAPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'temporal_adjustment_index': '',
            'installation_percentage': '',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation * self.temporal_adjustment_index
        components_cost = sum(price * quantity for name, price, quantity in self.components)
        capex = (iron_cost + insulation_cost + components_cost) * (1 + self.installation_percentage)
        return capex

    def opex(self):
        """
        Calcula el OPEX del sistema TES.

        Retorna:
        - float o str: El OPEX calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'delta_pressure_charge': 'Pa',
            'delta_pressure_discharge': 'Pa',
            'mass_flow_rate_charge': 'kg/s',  # Cambiado aquí
            'mass_flow_rate_discharge': 'kg/s',  # Cambiado aquí
            'working_fluid_density': 'kg/m³',
            'charging_time': 'hours',
            'discharging_time': 'hours',
            'cycles_per_year': '',
            'service_years': '',
            'electricity_cost_per_joule': '$/J',
            'fan_efficiency': '',
            'capex_maintenance_percentage': '',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        
        charge_term = (self.mass_flow_rate_charge * self.delta_pressure_charge / self.working_fluid_density) * self.charging_time  # Cambiado aquí
        discharge_term = (self.mass_flow_rate_discharge * self.delta_pressure_discharge / self.working_fluid_density) * self.discharging_time  # Cambiado aquí
        opex = (self.cycles_per_year / self.service_years) * (self.electricity_cost_per_joule / self.fan_efficiency) * (charge_term + discharge_term) + (self.capex_maintenance_percentage * self.capex_knobloch()) / self.service_years
        return opex


    def LCOS(self):
        """
        Calcula el Costo Nivelado de Almacenamiento de Energía (LCOS).

        Retorna:
        - float o str: El LCOS calculado o un mensaje indicando los parámetros faltantes.
        """
        required_params = {
            'annual_discount_rate': '',
            'tes_energy_capacity': 'kWh',
            'tes_efficiency': '',
        }
        missing_params = self.check_parameters(required_params)
        if missing_params:
            return f"Faltan los siguientes datos: {missing_params}"
        

        # Verificación de si self.opex es un string
        opex = self.opex()
        if isinstance(opex, str):
            return f"Faltan datos de OPEX: {opex}"
        
        capex = self.capex_pereira()
        if isinstance(capex, str):
            return capex

        opex_total = sum(self.opex() / (1 + self.annual_discount_rate) ** n for n in range(1, self.service_years + 1))
        total_cycles = sum(self.cycles_per_year * self.tes_energy_capacity * self.tes_efficiency / (1 + self.annual_discount_rate) ** n for n in range(1, self.service_years + 1))
        lcos = (capex + opex_total) / total_cycles
        return lcos

# # Example usage
# # Create an instance of the TES object with example data
# tes_system = TES(
#     iron_volume=100.0,  # m³
#     insulation_volume=50.0,  # m³
#     price_per_cubic_meter_iron=200,  # $/m³
#     price_per_cubic_meter_insulation=50,  # $/m³
#     components=[("Pump", 5000, 2), ("Valve", 1500, 4)]  # list of components
# )

# # Set additional parameters
# tes_system.set_additional_parameters(
#     density_tes_material=1600,  # kg/m³
#     volume_tes_material=1200.0,  # m³
#     specific_heat_tes_material=1,  # kJ/(kg·K)
#     temperature_difference=300,  # K
#     tes_efficiency=0.9,
#     k_mctigue=0.02,
#     initial_pressure=101325,  # Pa (1 atm)
#     final_pressure=202650,  # Pa (2 atm)
#     temporal_adjustment_index=1.05,
#     installation_percentage=0.15,
#     cycles_per_year=250,
#     service_years=20,
#     electricity_cost_per_joule=0.00005,  # $/J
#     fan_efficiency=0.85,
#     charging_time=5,  # hours
#     discharging_time=5,  # hours
#     working_fluid_flow=0.1,  # m³/s
#     flow_section_area=0.5,  # m²
#     working_fluid_density=1000,  # kg/m³
#     capex_maintenance_percentage=0.02,
#     annual_discount_rate=0.05,
#     tes_energy_capacity=2  # kWh
# )

# # Display TES system information
# tes_system.display_info()

# # Calculate different CAPEX values
# capex_knobloch = tes_system.capex_knobloch()
# capex_kocher = tes_system.capex_kocher()
# capex_mctigue = tes_system.capex_mctigue()
# capex_trevisan = tes_system.capex_trevisan()
# capex_pereira = tes_system.capex_pereira()

# print(f"CAPEX Knobloch: {capex_knobloch}")
# print(f"CAPEX Kocher: {capex_kocher}")
# print(f"CAPEX McTigue: {capex_mctigue}")
# print(f"CAPEX Trevisan: {capex_trevisan}")
# print(f"CAPEX Pereira: {capex_pereira}")

# # Calculate OPEX
# opex = tes_system.opex()
# print(f"OPEX: {opex}")

# # Calculate LCOS
# lcos = tes_system.LCOS()
# print(f"LCOS: {lcos}")
