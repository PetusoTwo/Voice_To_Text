import speech_recognition as sr
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QApplication
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
        self.copytext.clicked.connect(self.copyText)
        self.txt_voice.clicked.connect(self.convertVoice)

    def copyText(self):
        if self.output.toPlainText() != "":
            self.output.selectAll()
            self.output.copy()
            self.output.clear()
            QMessageBox.information(self, "Texto copiado", "Texto copiado exitosamente")
        else:
            QMessageBox.critical(self, "Error", "No hay texto para copiar")

    def convertText(self):
        with sr.Microphone() as source:
            QMessageBox.information(self, "Micrófono", "Listo para hablar!!")
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

    def convertVoice(self):
        QMessageBox.information(self, 'Aviso', 'Esta funcion aun no se encuentra disponible')

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