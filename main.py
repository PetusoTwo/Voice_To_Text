import speech_recognition as sr

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Usar el micrófono para capturar el audio
with sr.Microphone() as source:
    print("Ajustando el micrófono. Por favor, espere...")
    recognizer.adjust_for_ambient_noise(source)  # Ajustar el ruido ambiental
    print("¡Listo para hablar!")
    audio = recognizer.listen(source)

try:
    # Usar Google Web Speech API para reconocer el audio
    text = recognizer.recognize_google(audio, language= 'es- ES')
    print("Texto reconocido: " + text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("No se pudo conectar con el servicio de Google Speech Recognition; {0}".format(e))
