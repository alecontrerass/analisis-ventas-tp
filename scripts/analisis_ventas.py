import pandas as pd
import matplotlib.pyplot as plt

#Leemos el archivo de ventas
df = pd.read_csv("datos/ventas.csv")

#Calculamos el total por venta (cantidad x precio)
df["total"] = df["cantidad"] * df["precio"]

#Ventas totales
print("Ventas totales:", df["total"].sum())

#Producto mas vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print("Producto mas vendido:", producto_mas_vendido)

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
ventas_mes = df.groupby(df["fecha"].dt.month)["total"].sum()
print("Ventas por mes:\n", ventas_mes)

# Grafico de evolucion de ventas
ventas_mes.plot(kind="line", marker="o", title="Evolucion de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total")
plt.savefig("resultados/grafico_ventas.png")
print("Grafico guardado")
