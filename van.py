from Flujo_de_caja2 import calcular_flujo_de_caja
import matplotlib.pyplot as plt

# # Parámetros generales
# años = 30
# tasa_descuento = 0.07  # 7%

# # Precio de venta de energía por kWh
# precio_energia_escenario1 = 0.024  # en USD/kWh
# precio_energia_escenario2 = 0.0284  # en USD/kWh

# # Producción anual de energía en kWh
# produccion_anual_kwh = None  # No especificado directamente

# # Subsidios anuales
# subsidios_anuales = None  # No especificado

# # Costos de operación y mantenimiento anuales
# costos_om_fijo_por_capacidad = 66  # en USD/kW-año
# costos_om_total_fijo_anual = 1.09  # en millones USD/año
# costos_om_variable_por_generacion = 4  # en USD/MWh

# # Costos de combustible anuales
# costos_combustible_anuales = None  # No aplicable

# # Pagos de intereses y amortización de préstamos anuales
# costos_capital_anuales = None  # No especificado directamente

# # Costos de seguro anuales
# costos_seguro_anuales = None  # No especificado

# # Otros costos anuales
# otros_costos_anuales = 3.09  # en millones USD

# # Inversión inicial en la planta
# inversion_inicial_costos_directos = 47.18  # en millones USD
# inversion_inicial_costos_indirectos = 7.55  # en millones USD
# inversion_inicial_costo_total_instalado = 54.73  # en millones USD

# # Tasa de impuestos sobre la renta
# tasa_impuestos = None  # No especificado

# Producción energía
produccion_diaria = 126.26e3 + 155.07e3 # kWh  


# Parámetros de entrada
años = 30  # Número de años de análisis
precio_energia = [0.11]*años  # Precio de venta de energía por kWh
produccion_anual = [produccion_diaria * 365]*años  # Producción anual de energía en kWh
subsidios = [0]*años  # Subsidios anuales
costos_om = [1.09e6] *años # Costos de operación y mantenimiento anuales
costos_combustible = [0]*años  # Costos de combustible anuales
costos_capital = [0]*años  # Pagos de intereses y amortización de préstamos anuales
costos_seguro = [0]*años  # Costos de seguro anuales
otros_costos = [3.09e6] *años # Otros costos anuales
inversion_inicial = 54.73e6 # Inversión inicial en la planta
tasa_impuestos = 0 # Tasa de impuestos sobre la renta
tasa_descuento = 0.07 # Tasa de descuento para el cálculo del VAN

# Llamada a la función calcular_flujo_de_caja
df_flujo_caja = calcular_flujo_de_caja(años, precio_energia, produccion_anual, subsidios, costos_om, costos_combustible, costos_capital, costos_seguro, otros_costos, inversion_inicial, tasa_impuestos, tasa_descuento)

# Mostrar el DataFrame resultante
# print(df_flujo_caja)

# Escoger las columnas a mostrar de la función
df_van = df_flujo_caja.loc[:, ['Año', 'Ingresos','Total Gastos', 'Flujo de Caja Libre', 'VAN', 'TIR']]
print(df_van)




# Guardar el DataFrame en un archivo Excel
df_flujo_caja.to_excel('flujo_caja_planta_energia.xlsx', index=False)

# Ejemplo de cómo acceder a datos específicos del DataFrame
año_especifico = 3  # Año específico para el que queremos los datos
van_año_especifico = df_flujo_caja.loc[df_flujo_caja['Año'] == año_especifico, 'VAN'].values[0]  # Obtener VAN del año específico
flujo_caja_libre_año_especifico = df_flujo_caja.loc[df_flujo_caja['Año'] == año_especifico, 'Flujo de Caja Libre'].values[0]  # Obtener flujo de caja libre del año específico

# Mostrar los datos específicos
print(f"VAN del año {año_especifico}: {van_año_especifico}")
print(f"Flujo de Caja Libre del año {año_especifico}: {flujo_caja_libre_año_especifico}")

def graficar_van(df_flujo_caja):
    """
    Genera una gráfica del VAN acumulado a lo largo de los años.

    Args:
    df_flujo_caja (pd.DataFrame): DataFrame con los datos de flujo de caja y VAN acumulado.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df_flujo_caja['Año'], df_flujo_caja['VAN'], marker='o')
    plt.title('VAN Acumulado a lo largo de los años')
    plt.xlabel('Año')
    plt.ylabel('VAN Acumulado')
    plt.grid(True)
    plt.show()

graficar_van(df_van)