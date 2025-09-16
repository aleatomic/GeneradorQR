# 🧠 Generador de Códigos QR

Esta es una aplicación de escritorio hecha en **Python con QtPy6** que permite generar **códigos QR estáticos y personalizados**, ideales para compartir enlaces, textos o cualquier dato de forma rápida y visual.

---

## 💻 Cómo Usar la App

1. Abre la carpeta `dist/`.
2. Ejecuta el archivo `QRGenerator.exe` ✅ (puede tener otro nombre si lo cambiaste).
3. Escribe el contenido que deseas codificar.
4. Haz clic en "Generar QR" para ver la previsualización.
5. Haz clic en "Guardar QR" para exportarlo como imagen.

---

## 🚀 Características

- ✅ Genera códigos QR con solo ingresar texto o URL.
- 🎨 Visualiza una **previsualización en tiempo real** del QR generado.
- 🖌️ Estilo visual con módulos redondeados.
- 💾 Posibilidad de guardar el QR como imagen (.png, .jpg).
- 🧩 Interfaz gráfica amigable y sin consola emergente.

---

## 📦 Cómo fue compilado

La aplicación fue empaquetada usando [PyInstaller](https://www.pyinstaller.org/) con el siguiente comando:

```bash
pyinstaller --onefile --windowed --icon=icon.ico qr_generator.py
```

@aleatomic :: https://github.com/aleatomic



