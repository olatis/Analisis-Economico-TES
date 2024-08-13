class TES:
    def __init__(self, working_fluid, storage_material, system_material, iron_volume, insulation_volume, density_tes_material, volume_tes_material, specific_heat_tes_material, temperature_difference, eficiencia_tes):
        """
        Initializes a Thermal Energy Storage (TES) system object.

        Args:
            working_fluid (str): The working fluid used in the TES system.
            storage_material (str): The material used for thermal energy storage.
            system_material (str): The material of the system that contains the storage.
            iron_volume (float): The volume of iron in the TES system in cubic meters.
            insulation_volume (float): The volume of insulation in the TES system in cubic meters.
            density_tes_material (float): The density of the TES material in kg/m³.
            volume_tes_material (float): The volume of TES material in cubic meters.
            specific_heat_tes_material (float): The specific heat capacity of the TES material in J/(kg·K).
            temperature_difference (float): The temperature difference in K.
            eficiencia_tes (float): The efficiency of the TES system (between 0 and 1).
        """
        self.working_fluid = working_fluid
        self.storage_material = storage_material
        self.system_material = system_material
        self.iron_volume = iron_volume
        self.insulation_volume = insulation_volume
        self.density_tes_material = density_tes_material
        self.volume_tes_material = volume_tes_material
        self.specific_heat_tes_material = specific_heat_tes_material
        self.temperature_difference = temperature_difference
        self.eficiencia_tes = eficiencia_tes
        self.price_per_cubic_meter_insulation = 0.0
        self.price_per_cubic_meter_iron = 0.0
        self.components = []

    def display_info(self):
        """
        Displays the information of the thermal energy storage system.
        """
        print(f"Working Fluid: {self.working_fluid}")
        print(f"Storage Material: {self.storage_material}")
        print(f"System Material: {self.system_material}")
        print(f"Iron Volume: {self.iron_volume} m³")
        print(f"Insulation Volume: {self.insulation_volume} m³")
        print(f"TES Material Density: {self.density_tes_material} kg/m³")
        print(f"TES Material Volume: {self.volume_tes_material} m³")
        print(f"Specific Heat of TES Material: {self.specific_heat_tes_material} J/(kg·K)")
        print(f"Temperature Difference: {self.temperature_difference} K")
        print(f"TES Efficiency: {self.eficiencia_tes}")
        print(f"Insulation Price per m³: {self.price_per_cubic_meter_insulation} $")
        print(f"Iron Price per m³: {self.price_per_cubic_meter_iron} $")
        if self.components:
            print("Components:")
            for name, price, quantity in self.components:
                print(f"  - {name}: {price} $ each, Quantity: {quantity}")
        else:
            print("No components added.")

    def set_insulation_price(self, price):
        """
        Sets the price per cubic meter of insulation.

        Args:
            price (float): Price per cubic meter of insulation in dollars.
        """
        self.price_per_cubic_meter_insulation = price

    def set_iron_price(self, price):
        """
        Sets the price per cubic meter of iron.

        Args:
            price (float): Price per cubic meter of iron in dollars.
        """
        self.price_per_cubic_meter_iron = price

    def add_component(self, name, price, quantity):
        """
        Adds a component to the list of components.

        Args:
            name (str): The name of the component.
            price (float): The price of the component in dollars.
            quantity (int): The quantity of the component.
        """
        self.components.append((name, price, quantity))

    def capex_knobloch(self):
        """
        Calculates the total cost of the TES system based on the iron and insulation volumes
        and the components list.

        Returns:
            float: The total cost of the TES system.
        """
        iron_cost = self.iron_volume * self.price_per_cubic_meter_iron
        insulation_cost = self.insulation_volume * self.price_per_cubic_meter_insulation
        components_cost = sum(price * quantity for name, price, quantity in self.components)
        capex = iron_cost + insulation_cost + components_cost
        return capex

    def capex_kocher(self):
        """
        Calculates the CAPEX based on the Kocher method using the given formula.

        Returns:
            float: The CAPEX value.
        """
        ETES = (self.density_tes_material * self.specific_heat_tes_material * self.temperature_difference) / 3600
        capex = (self.iron_volume * self.price_per_cubic_meter_iron + self.insulation_volume * self.price_per_cubic_meter_insulation) / (ETES * self.volume_tes_material * self.eficiencia_tes)
        return capex

# Example usage
tes = TES("Water", "Molten salt", "Stainless steel", 50.0, 10.0, 2500, 40.0, 800, 500, 0.85)
tes.set_insulation_price(50.0)
tes.set_iron_price(100.0)
tes.add_component("Pump", 1500.0, 2)
tes.add_component("Valve", 300.0, 4)
tes.display_info()

capex_knobloch = tes.capex_knobloch()
print(f"Total Knobloch CAPEX: {capex_knobloch} $")

capex_kocher = tes.capex_kocher()
print(f"CAPEX (Kocher): {capex_kocher} $/m³")
