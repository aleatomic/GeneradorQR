import sys
import os
import qrcode
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from PIL import Image

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Generador de QR")
        self.setGeometry(100, 100, 400, 500)

        self.setWindowIcon(QIcon("logo.png"))  # Logo de la app

        # Layout principal
        layout = QVBoxLayout()

        # Entrada de texto
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Ingrese texto o URL")
        layout.addWidget(self.input_text)

        # Botón para generar QR
        self.generate_btn = QPushButton("Generar Codigo QR", self)
        self.generate_btn.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_btn)

        # Etiqueta para mostrar el QR
        self.qr_label = QLabel(self)
        layout.addWidget(self.qr_label)

        # Botón para guardar QR
        self.save_btn = QPushButton("Guardar QR", self)
        self.save_btn.clicked.connect(self.save_qr)
        layout.addWidget(self.save_btn)

        # Configurar layout
        self.setLayout(layout)

        # Variable para almacenar la imagen generada
        self.qr_image = None

    def generate_qr(self):
        """Genera y muestra un código QR."""
        data = self.input_text.text()
        if not data:
            self.qr_label.setText("⚠️ Ingresa un texto o URL.")
            return

        # Crear código QR
        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Crear imagen con módulos redondeados
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            fill_color="black",
            back_color="white"
        )

        # Guardar temporalmente la imagen para mostrarla en la interfaz
        img.save("temp_qr.png")
        self.qr_image = img

        # Mostrar la imagen en la etiqueta
        self.show_qr_image("temp_qr.png")

    def show_qr_image(self, path):
        """Carga la imagen del QR en la interfaz."""
        pixmap = QPixmap(path)
        self.qr_label.setPixmap(pixmap)
        self.qr_label.setScaledContents(True)

    def save_qr(self):
        """Guarda el QR generado en un archivo seleccionado por el usuario."""
        if not self.qr_image:
            self.qr_label.setText("⚠️ Genera un QR primero.")
            return

        # Abrir cuadro de diálogo para seleccionar la ruta y el nombre del archivo
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar QR", "mi_codigo_qr.png",  # Nombre por defecto
            "PNG Files (*.png);;JPG Files (*.jpg);;All Files (*)"
        )

        if file_path:  # Si el usuario elige una ubicación
            self.qr_image.save(file_path)
            self.qr_label.setText("✅ QR guardado correctamente.")
            
            # Borrar el archivo temporal después de guardarlo
            self.delete_temp_qr()

    def delete_temp_qr(self):
        """Elimina el archivo temporal temp_qr.png si existe."""
        if os.path.exists("temp_qr.png"):
            os.remove("temp_qr.png")

    def closeEvent(self, event):
        """Se ejecuta cuando se cierra la ventana, borra el archivo temporal."""
        self.delete_temp_qr()
        event.accept()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
