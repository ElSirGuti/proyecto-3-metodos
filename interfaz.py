import flet as ft
from proceso_estocastico import ProcesoEstocasticoNoEstacionario
import time

def main(page: ft.Page):
    # Definir los campos de entrada y el botón
    tamaño_input = ft.TextField(label="Tamaño", value="1000", width=200)
    tendencia_input = ft.TextField(label="Tendencia", value="0.1", width=200)
    titulo_input = ft.TextField(label="Título de la Gráfica", value="Caminata Aleatoria con Tendencia", width=400)
    generar_button = ft.ElevatedButton(text="Generar Gráfica", on_click=lambda _: generar_grafica())

    # Definir un espacio para mostrar la imagen
    grafica_image = ft.Image(src="", width=800, height=400)

    # Función para generar la gráfica y actualizar la imagen
    def generar_grafica():
        tamaño = int(tamaño_input.value)
        tendencia = float(tendencia_input.value)
        titulo = titulo_input.value
        proceso = ProcesoEstocasticoNoEstacionario(tamaño, tendencia)
        proceso.generar_caminata_aleatoria()
        
        # Generar un nombre único para la imagen utilizando una marca de tiempo
        timestamp = int(time.time())
        filename = f'grafica_{timestamp}.png'
        proceso.graficar(filename=filename, titulo=titulo)
        
        # Actualizar la imagen en la interfaz
        grafica_image.src = filename
        page.update()

    # Añadir los componentes a la página
    page.add(
        ft.Column([
            tamaño_input,
            tendencia_input,
            titulo_input,
            generar_button,
            grafica_image
        ])
    )

# Ejecutar la aplicación
ft.app(target=main)
