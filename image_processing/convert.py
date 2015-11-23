from PIL import Image
image = Image.open("small_jobs.bmp")

out = 'var image = ['
first = True

for y in range(image.height):
    for x in range(image.width):
        color = image.getpixel((x, y))

        if first:
            first = False
        else:
            out += ", "
        out += str(round(sum(color)/3))
out += '];'

print(out)
