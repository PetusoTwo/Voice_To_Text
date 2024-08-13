import speech_recognition as sr
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIntValidator
import sys
# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Usar el micrófono para capturar el audio
def convertText():
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

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("./design.ui", self)
        
        #Configuraciones de ventana#
        self.setWindowOpacity(1)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        #Conexion a los botones
        self.close.clicked.connect(lambda: self.close())
        #self.voice_txt.clicked.connect(convertText()) #Crear funcion#
        self.copytext.clicked.connect(self.clearData)
        self.copytext.clicked.connect(self.copyText)
        
    def clearData(self):
        self.output.setText("")
        self.output.clear()
    def copyText(self):
        #Condicionales para copiar tecxto#
        if (self.output is not None):
            QMessageBox.information(self, "Error", "No hay texto para copiar")
        else:
            QMessageBox.information(self, "Copiado", "Copiado al portapapeles")
        
        
        
        
    #Funciones para que la ventana se pueda mover#
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_position = event.globalPosition().toPoint()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.click_position is not None:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_position)
            self.click_position = event.globalPosition().toPoint()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_position = None
# Ejecutar el bucle para la app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())