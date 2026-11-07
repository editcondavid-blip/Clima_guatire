import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Clima en Guatire"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    resultado_text = ft.Text("Presiona el botón para verificar el clima...", size=16)

    def verificar_clima_y_avisar(e):
        print("Consultando el clima actual de Guatire...")
        resultado_text.value = "Consultando el cielo..."
        page.update()

        try:
            url = "https://wttr.in/Guatire?format=j1"
            respuesta = requests.get(url, timeout=8)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                condicion_actual = datos['current_condition'][0]['weatherDesc'][0]['value'].lower()
                temperatura = datos['current_condition'][0]['temp_C']

                palabras_lluvia = ["rain", "drizzle", "shower", "thunderstorm", "torrential"]
                va_a_llover = any(palabra in condicion_actual for palabra in palabras_lluvia)

                if va_a_llover:
                    resultado_text.value = f"¡VA A LLOVER CUIDADO! 🌧️\n\nClima: {condicion_actual.capitalize()} | Temp: {temperatura}°C"
                else:
                    resultado_text.value = f"Clima despejado y neutralizado, tranquilo ☀️\n\nClima: {condicion_actual.capitalize()} | Temp: {temperatura}°C"
            else:
                resultado_text.value = "ERROR 01: NO SE PUDO CONSULTAR EL CLIMA"

        except Exception as err:
            resultado_text.value = f"Ocurrió un error inesperado: {err}"

        page.update()

    verificar_button = ft.Button("Verificar Clima", on_click=verificar_clima_y_avisar)

    page.add(
        ft.Text("🌧️ WEATHER GUATIRE", size=22, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color="transparent"),
        verificar_button,
        ft.Divider(height=20, color="transparent"),
        resultado_text
    )

ft.run(main)