"""A program that encodes and decodes hidden messages in images through LSB steganography"""
from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/encoded.png"):
    """Decodes the hidden message in an image

    file_location: the location of the image file to decode. By default is the provided encoded image in the images folder
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size()[0]
    y_size = encoded_image.size()[1]

    decoded_image = Image.new("RGB", encoded_image.size())
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            pass #TODO: Fill in decoding functionality

    decoded_image.save("images/decoded_image.png")

def write_text(text_to_write):
    """Writes text to an RGB image. Automatically line wraps

    text_to_write: the text to write to the image
    """
    image_text = Image.new("RGB", (x_size, y_size))
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encoded_image(text_to_encode, template_image="images/samoyed.jpg"):
    """Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    pass #TODO: Fill out this function

if __name__ == '__main__':
    decoded_image()
