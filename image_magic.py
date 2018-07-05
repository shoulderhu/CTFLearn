from PIL import Image

if __name__ == '__main__':
    image_in = Image.open("image/image_magic_in.jpg")
    (width_in, height_in) = image_in.size
    k = 0

    width_out = 304
    height_out = width_in // width_out
    image_out = Image.new("RGB", (width_out, height_out))
    out = image_out.load()

    for i in range(width_out):
        for j in range(height_out):
            out[i, j] = image_in.getpixel((k, 0))
            k += 1

    image_out.show()
    image_out.save("image/image_magic_out.jpg")

############################################################
#                       flag{cool_right?}                  #
############################################################


