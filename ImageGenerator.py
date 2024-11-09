import subprocess
import sys
import PIL


try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image


width = int(input("Give the width of black photo (E.g, 512): "))
height = int(input("Give the height of the black photo (E.g, 768): "))


black = (0, 0, 0)


image = Image.new("RGB", (width, height), black)


image.save("black_photo.png")

print("Black photo generated and saved as black_photo.png")
