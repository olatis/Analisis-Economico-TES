import numpy_financial as npf
import pandas as pd

def calcular_flujo_de_caja(años, precio_energia, produccion_anual, subsidios, costos_om, costos_combustible, costos_capital, costos_seguro, otros_costos, inversion_inicial, tasa_impuestos, tasa_descuento):
    """
    Calcula el flujo de caja de una planta de energía y retorna un DataFrame con los resultados.

    Args:
    años (int): Número de años de análisis.
    precio_energia (list of float): Lista de precios de venta de energía por kWh a lo largo de los años.
    produccion_anual (list of int): Lista de producciones anuales de energía en kWh a lo largo de los años.
    subsidios (list of float): Lista de subsidios anuales.
    costos_om (list of float): Lista de costos de operación y mantenimiento anuales.
    costos_combustible (list of float): Lista de costos de combustible anuales.
    costos_capital (list of float): Lista de pagos de intereses y amortización de préstamos anuales.
    costos_seguro (list of float): Lista de costos de seguro anuales.
    otros_costos (list of float): Lista de otros costos anuales.
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
        # Asegurarse de que los índices sean válidos para las listas
        idx = año - 1
        if idx >= len(precio_energia) or idx >= len(produccion_anual) or idx >= len(subsidios) or idx >= len(costos_om) or idx >= len(costos_combustible) or idx >= len(costos_capital) or idx >= len(costos_seguro) or idx >= len(otros_costos):
            raise ValueError("Las listas de parámetros deben tener al menos tantos elementos como el número de años especificado.")

        # Cálculo de ingresos por venta de energía
        ingresos = produccion_anual[idx] * precio_energia[idx]
        
        # Cálculo del total de gastos
        total_gastos = costos_om[idx] + costos_combustible[idx] + costos_capital[idx] + costos_seguro[idx] + otros_costos[idx]
        
        # Cálculo de ingresos netos (ingresos más subsidios menos total de gastos)
        ingresos_netos = ingresos + subsidios[idx] - total_gastos
        
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
        data.append([año, ingresos, subsidios[idx], costos_om[idx], costos_combustible[idx], costos_capital[idx], costos_seguro[idx], otros_costos[idx], total_gastos, ingresos_netos, impuestos, flujo_caja_operativo, inversiones_capital, flujo_caja_libre, VAN, TIR])
    
    # Crear el DataFrame con los datos
    df_flujo_caja = pd.DataFrame(data, columns=columnas)

    return df_flujo_caja
