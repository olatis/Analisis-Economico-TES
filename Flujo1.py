import pandas as pd
import numpy as np
import numpy_financial as npf

def calcular_flujo_de_caja(años, precio_energia, produccion_anual, subsidios, costos_om, costos_combustible, costos_capital, costos_seguro, otros_costos, inversion_inicial, tasa_impuestos, tasa_descuento):
    """
    Calcula el flujo de caja de una planta de energía y retorna un DataFrame con los resultados.

    Args:
    años (int): Número de años de análisis.
    precio_energia (float): Precio de venta de energía por kWh.
    produccion_anual (int): Producción anual de energía en kWh.
    subsidios (float): Subsidios anuales.
    costos_om (float): Costos de operación y mantenimiento anuales.
    costos_combustible (float): Costos de combustible anuales.
    costos_capital (float): Pagos de intereses y amortización de préstamos anuales.
    costos_seguro (float): Costos de seguro anuales.
    otros_costos (float): Otros costos anuales.
    inversion_inicial (float): Inversión inicial en la planta.
    tasa_impuestos (float): Tasa de impuestos sobre la renta.
    tasa_descuento (float): Tasa de descuento para el cálculo del VAN.

    Returns:
    pd.DataFrame: DataFrame con los resultados del flujo de caja, incluyendo VAN y TIR.
    """
    
    # Definición de las columnas del DataFrame
    columnas = ['Año', 'Ingresos', 'Subsidios', 'Costos de O&M', 'Costos de Combustible', 'Costos de Capital', 'Seguros', 'Otros Costos', 'Total Gastos', 'Ingresos Netos', 'Impuestos', 'Flujo de Caja Operativo', 'Inversiones de Capital', 'Flujo de Caja Libre', 'VAN', 'TIR']
    data = []

    # Lista para almacenar los flujos de caja libre de cada año
    flujos_caja_libre = []
    
    for año in range(1, años + 1):
        # Cálculo de ingresos por venta de energía
        ingresos = produccion_anual * precio_energia
        
        # Cálculo del total de gastos
        total_gastos = costos_om + costos_combustible + costos_capital + costos_seguro + otros_costos
        
        # Cálculo de ingresos netos (ingresos más subsidios menos total de gastos)
        ingresos_netos = ingresos + subsidios - total_gastos
        
        # Cálculo de impuestos
        impuestos = ingresos_netos * tasa_impuestos
        
        # Cálculo del flujo de caja operativo
        flujo_caja_operativo = ingresos_netos - impuestos
        
        # Inversión de capital en el primer año
        inversiones_capital = inversion_inicial if año == 1 else 0
        
        # Cálculo del flujo de caja libre
        flujo_caja_libre = flujo_caja_operativo - inversiones_capital
        
        # Almacenar el flujo de caja libre en la lista
        flujos_caja_libre.append(flujo_caja_libre)
        
        # Cálculo del VAN utilizando numpy_financial
        VAN = npf.npv(tasa_descuento, flujos_caja_libre)
        
        # Cálculo de la TIR utilizando numpy_financial
        TIR = npf.irr(flujos_caja_libre)

        # Añadir los datos del año al DataFrame
        data.append([año, ingresos, subsidios, costos_om, costos_combustible, costos_capital, costos_seguro, otros_costos, total_gastos, ingresos_netos, impuestos, flujo_caja_operativo, inversiones_capital, flujo_caja_libre, VAN, TIR])
    
    # Crear el DataFrame con los datos
    df_flujo_caja = pd.DataFrame(data, columns=columnas)

    return df_flujo_caja

# Parámetros de entrada
años = 5  # Número de años de análisis
precio_energia = 0.1  # Precio de venta de energía por kWh
produccion_anual = 1_000_000  # Producción anual de energía en kWh
subsidios = 50_000  # Subsidios anuales
costos_om = 10_000  # Costos de operación y mantenimiento anuales
costos_combustible = 20_000  # Costos de combustible anuales
costos_capital = 0  # Pagos de intereses y amortización de préstamos anuales
costos_seguro = 0 # Costos de seguro anuales
otros_costos = 5_000  # Otros costos anuales
inversion_inicial = 500_000  # Inversión inicial en la planta
tasa_impuestos = 0.2  # Tasa de impuestos sobre la renta
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
