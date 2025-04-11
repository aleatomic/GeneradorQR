#Debemos de instalar esta libreria: pip install qrcode[pil]
'''
La librería qrcode en Python permite generar códigos QR de forma sencilla y personalizable. Se basa en la librería PIL (Pillow) para crear y manipular imágenes.
Lo que podemos lograr con esta librería es:
> Generar códigos QR de texto, URLs o cualquier dato.
> Ajustar tamaño, colores y nivel de corrección de errores.
> Guardar los QR como archivos de imagen (PNG, JPG, etc.).
> Convertir códigos QR en objetos PIL para editar o mostrar en pantalla.
'''
import qrcode # Importar la libreria qrcode, para generar el QR

# Pedir al usuario la URL o texto
data = input("Ingrese el texto o URL para el código QR: ")

# Crear el código QR
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1 es el más pequeño) / Tamaño del QR (va de 1 a 40, donde 40 es el más grande).
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores / Corrige errores si el QR está dañado (H es el más alto, corrige hasta 30% de daños).
    box_size=10,  # Tamaño de cada cuadro del QR / Tamaño de cada cuadrado dentro del QR.
    border=4  # Borde alrededor del QR / Borde en blanco alrededor del QR (mínimo recomendado es 4).
)
qr.add_data(data) # Agrega los datos al QR
qr.make(fit=True) # Genera el codigo QR ajustando el tamaño automáticamente

# Crear imagen QR
img = qr.make_image(fill_color="black", back_color="white")
'''
fill_color: Color del código(cuadros) QR (puede ser cualquier color).
back_color: Color de fondo del QR (puede ser cualquier color).
'''

# Guardar el código QR
img.save("codigo_qr.png")

print("✅ Código QR generado y guardado como 'codigo_qr.png'.")
