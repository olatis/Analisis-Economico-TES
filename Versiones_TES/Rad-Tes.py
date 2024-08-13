class RadTes:
    def __init__(self, longitud, anchura, altura):
        self.longitud = longitud
        self.anchura = anchura
        self.altura = altura
    
    def calcular_volumen(self):
        """
        Calcula el volumen de la máquina basado en sus dimensiones.
        Volumen = longitud * anchura * altura
        """
        return self.longitud * self.anchura * self.altura
    
    def calcular_costo(self):
        """
        Calcula el costo de la máquina basado en su volumen.
        Asume que el costo es de $10 por metro cúbico.
        """
        volumen = self.calcular_volumen()
        costo_por_metro_cubico = 10  # Costo en dólares
        return volumen * costo_por_metro_cubico
    
    def obtener_utilizacion_espacio(self):
        """
        Devuelve la utilización del espacio en metros cúbicos.
        """
        return self.calcular_volumen()

# Ejemplo de uso:
# Creando una máquina con longitud=2m, anchura=3m, altura=4m
maquina = RadTes(2, 3, 4)

# Calculando el costo
costo = maquina.calcular_costo()
print(f"El costo de la máquina es: ${costo}")

# Calculando la utilización del espacio
utilizacion_espacio = maquina.obtener_utilizacion_espacio()
print(f"La utilización del espacio de la máquina es: {utilizacion_espacio} metros cúbicos")
