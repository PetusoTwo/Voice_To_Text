# Speech Recognition App

Esta es una aplicación de reconocimiento de voz desarrollada con PyQt6 y la biblioteca `speech_recognition`. Permite convertir voz en texto. La aplicación también incluye una interfaz gráfica para facilitar el uso.

![image](https://github.com/user-attachments/assets/9460b3a5-5acd-4ae4-ad97-0dc4edb1c66a)

## Características

- **Conversión de voz a texto**: Usa la API de Google para convertir la voz capturada por el micrófono en texto.
- **Copiar texto al portapapeles**: Permite copiar el texto generado al portapapeles.
- **Interfaz gráfica**: Ventana sin bordes con opciones para moverla, cerrar y utilizar funcionalidades de reconocimiento de voz.

## Requisitos

- Python
- PyQt6
- speech_recognition

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/PetusoTwo/Voice_To_Text.git
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install SpeechRecognition
    pip install speech_recognition
    pip install PyQt6
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    python main.py
    ```

2. La aplicación se abrirá con una ventana sin bordes. Puedes:
   - Hacer clic en el botón para convertir voz en texto.
   - Hacer clic en el botón para copiar el texto al portapapeles.
   - Usar el botón para verificar la disponibilidad de la función de voz (aún no disponible).

## Funcionalidades Futuras

- **Convertir voz en texto directamente desde archivos de audio**: Implementar la capacidad de convertir archivos de audio pregrabados en texto.


