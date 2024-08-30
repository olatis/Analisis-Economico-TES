
# Análisis Económico Sistema TES

## Descripción del Proyecto

El proyecto **Análisis Económico Sistema TES** se centra en el análisis financiero y económico de un sistema de almacenamiento de energía térmica (TES). A través de una serie de cálculos, se determinan los flujos de caja, el Valor Actual Neto (VAN) y la Tasa Interna de Retorno (TIR) del proyecto, proporcionando una evaluación completa de la viabilidad económica del sistema TES.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos principales:

- **`Flujo1.py`:** Este archivo contiene las funciones necesarias para calcular los flujos de caja, el VAN y la TIR del proyecto TES. Se encarga de procesar los ingresos, gastos y otros aspectos financieros relacionados con la operación del sistema TES.

- **`TES_functions.py`:** Aquí se encuentran diversas funciones que apoyan los cálculos específicos relacionados con los costos y parámetros del sistema TES. Estas funciones permiten una manipulación eficiente de los datos requeridos para el análisis económico.

- **`TES_object.py`:** Define la clase `TES`, que modela un sistema de almacenamiento de energía térmica. Este archivo incluye métodos para inicializar el objeto TES con parámetros clave, así como para realizar verificaciones y ajustes adicionales necesarios para los cálculos.

## Requisitos de Instalación

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- Pandas
- Numpy
- Numpy-financial

Puedes instalar las dependencias necesarias utilizando pip:

```bash
pip install pandas numpy numpy-financial
```

## Instrucciones de Uso

1. **Inicialización del Proyecto:**
   - Asegúrate de tener los archivos `Flujo1.py`, `TES_functions.py` y `TES_object.py` en el mismo directorio de trabajo.

2. **Ejecutar el Análisis Económico:**
   - Puedes utilizar las funciones en `Flujo1.py` para realizar los cálculos financieros del sistema TES. El flujo de trabajo típico incluye la inicialización del objeto `TES` en `TES_object.py`, seguido de la ejecución de funciones específicas en `TES_functions.py` para preparar los datos necesarios.

3. **Ejemplo de Uso:**
   - Aquí un pequeño ejemplo de cómo podrías utilizar los archivos:

   ```python
   from TES_object import TES
   from TES_functions import calcular_costos, obtener_datos
   from Flujo1 import calcular_flujos_caja

   # Inicializar el objeto TES con parámetros de ejemplo
   tes = TES(iron_volume=10, insulation_volume=5, price_per_cubic_meter_iron=100, price_per_cubic_meter_insulation=50, components=[('Component1', 20, 3)])

   # Establecer parámetros adicionales
   tes.set_additional_parameters(costo_operacion=2000, tasa_impuestos=0.3)

   # Verificar parámetros
   tes.check_parameters(required_params={'costo_operacion': 'USD', 'tasa_impuestos': '%'})

   # Calcular flujos de caja
   flujos_caja = calcular_flujos_caja(años=10, produccion_anual=1000, precio_energia=0.2, ...)

   print(flujos_caja)
   ```

## Contribuciones

Si deseas contribuir a este proyecto, por favor, sigue las siguientes pautas:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agregar nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.


## Contacto

Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en contactar al autor en [idrivera@uc.cl].
