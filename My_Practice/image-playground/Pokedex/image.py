from PIL import Image, ImageFilter

img = Image.open("luke-miller-5OjiVFkZl-w-unsplash.jpg")
print(img.size)
img.thumbnail((672, 900))
img.save("custom_size.png", "png")
img.show()
