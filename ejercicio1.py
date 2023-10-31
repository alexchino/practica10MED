import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('datos.csv')

ventas_por_mes = df.groupby('mes')['ventas'].sum()

plt.figure(figsize=(10, 6)) 
plt.barh(ventas_por_mes.index, ventas_por_mes.values, color='skyblue') }
plt.xlabel('Ventas Totales')  
plt.ylabel('Mes')  
plt.title('Ventas Totales por Mes')  
plt.yticks(ventas_por_mes.index, ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
plt.show()