import numpy_financial as npf

# Definición de los flujos de caja
flujos_caja = [-100000, 30000, 40000, 50000, 20000]

# Definición de la tasa de descuento
tasa_descuento = 0.1

# Cálculo del VAN
van = npf.npv(tasa_descuento, flujos_caja)

print(f"El VAN del proyecto es: {van:.2f}")

# Cálculo de la TIR
tir = npf.irr(flujos_caja)


print(f"La TIR del proyecto es: {tir:.2f}")