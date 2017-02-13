from PIL import Image, ImageFont, ImageDraw
import textwrap

#samoyed from: http://puppytoob.com/wp-content/uploads/sites/3/2015/01/samoyed.jpg
#opening image, preparing channel
template_image = Image.open("samoyed.jpg")
red_template = template_image.split()[0]
green_template = template_image.split()[1]
blue_template = template_image.split()[2]

x_size = template_image.size[0]
y_size = template_image.size[1]
# print "img size: ", x_size, y_size

#text draw
text_to_encode = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."

image_to_encode = Image.new("RGB", (x_size, y_size))
font = ImageFont.load_default().font
d = ImageDraw.Draw(image_to_encode)
margin = offset = 10
for line in textwrap.wrap(text_to_encode, width=60):
    d.text((margin,offset), line, font=font)
    offset += 10
bw_encode = image_to_encode.convert('1')
bw_encode.save("w2.png")

#encode text into image
encoded_image = Image.new("RGB", (x_size, y_size))
pixels = encoded_image.load()
for i in range(x_size):
    for j in range(y_size):
        red_template_pix = bin(red_template.getpixel((i,j)))
        old_pix = red_template.getpixel((i,j))
        tencode_pix = bin(bw_encode.getpixel((i,j)))

        if tencode_pix[-1] == '1':
            red_template_pix = red_template_pix[:-1] + '1'
        else:
            red_template_pix = red_template_pix[:-1] + '0'
        pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))

encoded_image.save("encoded.png")

#decode portion
encoded_channel = encoded_image.split()[0]
dec = Image.new("RGB", (x_size, y_size))
pixels = dec.load()
for i in range(x_size):
    for j in range(y_size):
        if bin(encoded_channel.getpixel((i, j)))[-1] == '1':
            pixels[i, j] = (255, 255, 255)
        else:
            pixels[i, j] = (0,0,0)

dec.save("jw.png")


# mask =

#im.show()
