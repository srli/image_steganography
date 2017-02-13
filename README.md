
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

There are multiple ways to hide things within other things, but today we will be working with images. Typical images are composed of three color channels (RGB), with pixel values of 0-255 for each pixel. So a pixel with the value (255,255,255) would be entirely white while (0,0,0) would be black. The upper range is 255 because it is the largest value that can be represented by an 8 bit binary number. Binary is a base-two paradigm, in contrast to decimal which is in base-ten.

Here's an example of counting in binary from 0 to 32
![Binary counter. Source: Wikipedia](https://en.wikipedia.org/wiki/Binary_number#/media/File:Binary_counter.gif)

So if we wanted to convert the number `10001011` from binary into decimal, it would look something like:

`2^8 + 2^4 + 2^2 + 2^1 = 139`

You can test this out with any [RGB color wheel](http://www.colorspire.com/rgb-color-wheel/) to get a sense of


## Completing the Toolbox Exercise

To turn in your assignment, push your code and screenshots to GitHub and
submit a pull request.
