
from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.98

def turn_red(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        pixel.green = 0
        pixel.blue = 0
    return my_image

def turn_blue(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        pixel.red = 0
        pixel.green = 0
    return my_image

def turn_green(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        pixel.red = 0
        pixel.blue = 0
    return my_image

def turn_idkwhat(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        pixel.green = 0
    return my_image

def compute_luminoisity(blue,green,red):
    luminiosity = (blue*0.114 + green * 0.587 + red * 0.299)
    return luminiosity

def grey_scale(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        luminiosity = compute_luminoisity( pixel.blue, pixel.green, pixel.red)
        pixel.blue=luminiosity
        pixel.green=luminiosity
        pixel.red=luminiosity
    return my_image

def  half_grey(filename):
    my_image = SimpleImage(filename)
    for pixel in my_image:
        if pixel.x >= my_image.width//2:
            luminiosity = compute_luminoisity(pixel.blue, pixel.green, pixel.red)
            pixel.blue = luminiosity
            pixel.green = luminiosity
            pixel.red = luminiosity
    return my_image
def green_screened(foreground_object , background_object):
    front = SimpleImage(foreground_object)
    back = SimpleImage(background_object)
    for pixel in front:
        average = (pixel.red + pixel.green + pixel.blue)// 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            x=pixel.x
            y=pixel.y
            front.set_pixel(x,y, back.get_pixel(x,y))
    return front

def mirrored(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width*2 , height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x,y,pixel)
            mirror.set_pixel((width*2)-(x+1),y,pixel)
    return mirror


def main():
    #real_image = SimpleImage("D:\haha.png")
    #real_image.show()
    #red_image = turn_red("D:\haha.png")
    #red_image.show()
    #blue_image = turn_blue("D:\haha.png")
    #blue_image.show()
    #green_image = turn_green("D:\haha.png")
    #green_image.show()
    #idk_image = turn_idkwhat("D:\yb2.png")
    #idk_image.show()
    #grey_image = grey_scale("D:\haha.png")
    #grey_image.show()
    #half_grey_image = half_grey("D:\haha.png")
    #half_grey_image.show()
    #greened_image = green_screened("D:\yb2.png","D:\sandip.png")
    #greened_image.show()
    mirrored_image = mirrored("D:\swastiks.png")
    mirrored_image.show()





if __name__ == '__main__':
    main()



