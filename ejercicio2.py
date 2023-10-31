import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('puntajes.csv')

plt.figure(figsize=(10, 6))
plt.stackplot(df.index, df['examen1'], df['examen2'], labels=['Examen 1', 'Examen 2'], alpha=0.7)  # Crear el gráfico de áreas
plt.xlabel('Número de Estudiantes') 
plt.ylabel('Puntajes') 
plt.title('Relación entre Puntajes de Examen 1 y Examen 2') 
plt.legend(loc='upper left')  
plt.show()
