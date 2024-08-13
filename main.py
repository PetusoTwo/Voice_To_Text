import speech_recognition as sr
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIntValidator
import sys
# Inicializar el reconocedor
recognizer = sr.Recognizer()

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
        self.voice_txt.clicked.connect(self.convertText)
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
    def convertText(self):
        with sr.Microphone() as source:
            QMessageBox.information(self, "Micrófono", "Ajustando el micrófono. Por favor, espere...")
            recognizer.adjust_for_ambient_noise(source)  # Ajustar el ruido ambiental
            audio = recognizer.listen(source)
            # Capturar el audio y posibles errores
            try:
                # Usar Google Web Speech API para reconocer el audio
                text = recognizer.recognize_google(audio, language='es-ES')
                self.output.setText(text)
                QMessageBox.information(self, "Éxito", "Texto reconocido exitosamente")
            except sr.UnknownValueError:
                QMessageBox.critical(self, "Error", "No se pudo entender el audio")
            except sr.RequestError as e:
                QMessageBox.critical(self, "Error", f"No se pudo conectar con el servicio de Google Speech Recognition; {e}")

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