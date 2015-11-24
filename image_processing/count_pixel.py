from PIL import Image
image = Image.open("icons.png")

WIDTH = 15
HEIGHT = 16

out = 'var pixels = ['
first = True

for y in range(6):
    for x in range(10):
        pixel_sum = 0

        for pixel_y in range(HEIGHT):
            for pixel_x in range(WIDTH):
                pixel = image.getpixel((x * WIDTH + pixel_x, y * HEIGHT + pixel_y))
                pixel_sum += pixel[3]
        if first:
            first = False
        else:
            out += ", "
        out += str(round(pixel_sum/(WIDTH*HEIGHT)))
out += '];'

print(out)
