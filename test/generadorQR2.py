# Es lo mismo | pero con píxeles redondeados, diseño diferente y colores personalizados.
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

# Pedir el texto o URL
data = input("Ingrese el texto o URL para el código QR: ")

# Crear el código QR
qr = qrcode.QRCode(
    version=4,  # QR más grande para mejor visibilidad de formas
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# Crear imagen con píxeles redondeados
img = qr.make_image(
    image_factory=StyledPilImage, # Usar imagen estilizada / Permite modificar la forma de los cuadros del QR
    module_drawer=RoundedModuleDrawer(),  # Usa píxeles redondeados
    fill_color="black",
    back_color="white"
)

# Guardar imagen
img.save("codigo_qr_redondeado.png")

print("✅ Código QR con píxeles redondeados generado.")
