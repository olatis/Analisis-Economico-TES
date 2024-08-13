class Tes:
    def __init__(self, clase, longitud, anchura, altura):
        self.clase = clase
        self.longitud = longitud
        self.anchura = anchura
        self.altura = altura
        self.acero_x_volumen = None # Indica la cantidad de kg acero necesario por cada m3 que utilice el sistema.
    
    
    def calcular_costo(self, costo_por_metro_cubico = 10):
        """
        Calcula el costo de la máquina basado en su volumen.
        Asume que el costo es de $10 por metro cúbico.
        """
        volumen = self.calcular_volumen()
        return volumen * costo_por_metro_cubico
    
    def kilos_acero(self, nuevo_kilos_acero):
        """
        Establece una nueva cantidad de kg de acero por m3 de volumen del sistema.
        """
        self.acero_x_volumen = nuevo_kilos_acero
    
    


# Ejemplo de uso:
# Creando una máquina con longitud=2m, anchura=3m, altura=4m
maquina = Tes(2, 3, 4)

# Calculando el costo
costo = maquina.calcular_costo()
print(f"El costo de la máquina es: ${costo}")

# Calculando la utilización del espacio
utilizacion_espacio = maquina.obtener_utilizacion_espacio()
print(f"La utilización del espacio de la máquina es: {utilizacion_espacio} metros cúbicos")


