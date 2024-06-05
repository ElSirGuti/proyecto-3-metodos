import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Usar el backend Agg para evitar problemas con la GUI
matplotlib.use('Agg')

class ProcesoEstocasticoNoEstacionario:
    def __init__(self, tamaño, tendencia=0.1):
        self.tamaño = tamaño
        self.tendencia = tendencia
        self.caminata = None
    
    def generar_caminata_aleatoria(self):
        # Generar una serie de pasos aleatorios usando una distribución normal
        pasos_aleatorios = np.random.normal(loc=0, scale=1, size=self.tamaño)
        
        # Crear una tendencia lineal
        tendencia_lineal = np.linspace(0, self.tendencia * self.tamaño, self.tamaño)
        
        # Calcular la caminata aleatoria sumando los pasos aleatorios a la tendencia lineal
        self.caminata = np.cumsum(pasos_aleatorios) + tendencia_lineal

    def graficar(self, filename='grafica.png', titulo='Caminata Aleatoria con Tendencia'):
        # Verificar si la caminata ha sido generada
        if self.caminata is None:
            raise ValueError("La caminata no ha sido generada. Llame a generar_caminata_aleatoria primero.")
        
        # Crear una figura y un gráfico
        plt.figure(figsize=(12, 6))
        
        # Graficar la caminata
        plt.plot(self.caminata, label=titulo)
        
        # Configurar título y etiquetas de los ejes
        plt.title(titulo)
        plt.xlabel("Tiempo")
        plt.ylabel("Valor")
        
        # Mostrar la leyenda y agregar una cuadrícula
        plt.legend()
        plt.grid(True)
        
        # Guardar la figura en un archivo y cerrarla
        plt.savefig(filename)
        plt.close()
