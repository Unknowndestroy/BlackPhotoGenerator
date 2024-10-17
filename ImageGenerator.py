import subprocess
import sys
import PIL

# Pillow kütüphanesinin yüklü olup olmadığını kontrol et
try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

# Kullanıcıdan resim boyutlarını alma
width = int(input("Give the width of black photo (E.g, 512): "))
height = int(input("Give the height of the black photo (E.g, 768): "))

# Siyah renk (RGB formatında)
black = (0, 0, 0)

# Yeni bir siyah resim oluştur
image = Image.new("RGB", (width, height), black)

# Resmi mevcut dizine kaydet
image.save("black_photo.png")

print("Black photo generated and saved as black_photo.png")
