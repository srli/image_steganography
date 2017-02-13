
# Image Steganography
In this toolbox exercise you will delve a bit deeper into the specifics of how images are created in addition to learning about bitwise operations. This exercise was modified from [Interactive Python](http://interactivepython.org/runestone/static/everyday/2013/03/1_steganography.html), though this version encodes an image into another image instead of ASCII text.

To complete this toolbox, you will need to write two functions. The first is a decoding function that can extract secret information from an image file, while the second is a function that can encode secret messages into images.

## Get Set
This toolbox uses the [Python Pillow library](https://pillow.readthedocs.io/en/4.0.x/reference/Image.html). You should already have this installed on your system from the Computational Art mini-project, but go ahead and install it using pip3 if it's missing.

Fork and clone the [image_steganography] toolbox from Github.

## What is steganography?
In a nutshell, the main goal of [steganography](https://en.wikipedia.org/wiki/Steganography) is to hide information within data that doesn't appear to be secret at a glance. For example, this sentence:

`Since everyone can read, encoding text in neutral sentences is definitely effective`

turns into

`Secret inside`

if you take the first letter of every word. Steganography is really handy to use, because people won't even suspect that they're looking at a secret message--making it less likely that they'll want to try to crack your code. In the past, you may have tried to accomplish this kind of subterfuge using invisible inks or using special keywords with your friends. However, as fearless coders we have access to fancier ways to sneak data around.

## The value of one pixel

There are multiple ways to hide things within other things, but today we will be working with images. Typical images are composed of three color channels (RGB), with pixel values of 0-255 for each pixel. So a pixel with the value (255,255,255) would be entirely white while (0,0,0) would be black. The upper range is 255 because it is the largest value that can be represented by an 8 bit binary number. Binary is a base-two paradigm, in contrast to decimal which is in base-ten, which means you calculate the value of a binary number by summing the 2s exponent of each place where a 1 appears.

So if we wanted to convert the number `10001011` from binary into decimal, it would look something like:

`2^8 + 2^4 + 2^2 + 2^1 = 139`

From this, you can quickly see that the leftmost bit place matters a lot more than rightmost bit because that rightmost bit only modifies the value of the number by 1. To test:
`10001011 = 139` while `00001011 = 11`
`10001011 = 139` while `10001010 = 138`

Because of this, we describe the leftmost bit as the "most significant bit"(MSB) while the rightmost bit is called the "least significant bit"(LSB).

Since changing the LSB doesn't drastically change the overall value of the of 8 bit number, we can hide our data there without modifying a source image in any detectable sort of way. You can test this out with any [RGB color wheel](http://www.colorspire.com/rgb-color-wheel/) to get a sense of how little difference there is between a color like (150, 50, 50) and (151, 50, 50)

## Decoding the sample image

Provided in this toolbox is a picture of a cute dog. This dog is also 
## Completing the Toolbox Exercise

To turn in your assignment, push your code and screenshots to GitHub and
submit a pull request.
