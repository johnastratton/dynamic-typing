import Tkinter
import tkFileDialog
import os
import sys

root = None

__author__ = 'Michael Hay, Joel Sommers'
__doc__ = '''A library for image objects.'''


try:
    import png
except ImportError:
    raise ImageException("Can't find png.py file.  Make sure this file is in same folder as image.py")

class ImageException(Exception):
    pass

class InvalidImageTypeException(Exception):
    pass

class Pixel(object):
    def __init__(self, x, y, rgb):
        self.x = x
        self.y = y
        self.__set_rgb(*rgb)
        self.rgb = rgb
    def get_rgb(self):
        return tuple(self.rgb) 
    def get_red(self):
        return self.rgb[0]
    def get_green(self):
        return self.rgb[1]
    def get_blue(self):
        return self.rgb[2]
    def set_rgb(self, r, g, b):
        self.__set_rgb(r, g, b)
    def set_red(self, new_r):
        r, g, b = self.rgb
        self.__set_rgb(new_r, g, b)
    def set_green(self, new_g):
        r, g, b = self.rgb
        self.__set_rgb(r, new_g, b)
    def set_blue(self, new_b):
        r, g, b = self.rgb
        self.__set_rgb(r, g, new_b)
    def __set_rgb(self, r, g, b):
        if not (type(r) == int and type(g) == int and type(b) == int):
            raise ImageException("RGB values must be of type int: " + ':'.join(map(str,[r, g, b])))
        if not (0 <= r < 256 and 0 <= g < 256 and 0 <= b < 256):
            raise ImageException("RGB value out of range: " + ':'.join(map(str,[r, g, b])))
        self.rgb = (r, g, b)
    def __repr__(self):
        return "Pixel object with (x, y) = (%d, %d) with RGB = %s at %s" % \
        (self.x, self.y, self.rgb, hex(id(self)))

class Image(object):
    
    def __init__(self, pixels):
        """Expects pixels in boxed row boxed pixel format (from py.png):
            list([ (R,G,B), (R,G,B), (R,G,B) ],
                  [ (R,G,B), (R,G,B), (R,G,B) ])
        """
        self.__height = len(pixels)
        self.__width = len(pixels[0])
        self.pixels = [] 
        for y in range(len(pixels)):
            row = pixels[y]
            row_copy = []
            for x in range(len(row)):
                r, g, b = row[x]
                row_copy.append(Pixel(x, y, (r,g,b)))
            self.pixels.append(row_copy)
                
    def _get_flat_pixel_list(self):
        for y in range(self.height()):
            for x in range(self.width()):
                yield self.get_red(x, y)
                yield self.get_green(x, y)
                yield self.get_blue(x, y)

    def height(self):
        """Returns the height of the image."""
        return self.__height

    def width(self):
        """Returns the width of the image."""
        return self.__width

    def get_red(self, x, y):
        """Returns the red value of the pixel at position (x,y) in the image."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].get_red()

    def get_green(self, x, y):
        """Returns the green value of the pixel at position (x,y) in the image."""
        #self.__check_dimensions(x, y)
        return self.pixels[y][x].get_green()

    def get_blue(self, x, y):
        """Returns the blue value of the pixel at position (x,y) in the image."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].get_blue()

    def get_rgb(self, x, y):
        """Returns three numbers, the red, green, and blue value of the pixel at position (x,y) in the image."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].get_rgb()

    def set_red(self, x, y, newval):
        """Set the red value of the pixel at position (x,y) in the image to newval."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].set_red(newval)

    def set_green(self, x, y, newval):
        """Set the green value of the pixel at position (x,y) in the image to newval."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].set_green(newval)

    def set_blue(self, x, y, newval):
        """Set the blue value of the pixel at position (x,y) in the image to newval."""
        self.__check_dimensions(x, y)
        return self.pixels[y][x].set_blue(newval)

    def set_rgb(self, x, y, *rgb):
        """Expects as input five parameters: x, y, r, g, b.  Sets the red, green, and 
        blue value of the pixel at position (x,y) in the image to r, g, b respectively."""
        self.__check_dimensions(x, y)
        if len(rgb) == 1:
            rgb = rgb[0]
            if not( (type(rgb) == list or type(rgb) == tuple) and len(rgb) == 3 ):
                raise ImageException("Expecting an RGB triple, got this instead: ({0}) out of range".format(rgb))
            r, g, b = rgb
        elif len(rgb) == 3:
            r, g, b = rgb
        else:
            raise ImageException("Expecting an RGB triple, got this instead: ({0}) out of range".format(rgb))
        return self.pixels[y][x].set_rgb(r, g, b)

    def __check_dimensions(self, x, y):
        if x >= self.width() or x < 0:
            raise ImageException("x dimension ({0}) out of range".format(x))

        if y >= self.height() or y < 0:
            raise ImageException("y dimension ({0}) out of range".format(y))

    def pixel_list(self):
        for y in range(self.height()):
            for x in range(self.width()):
                yield self.pixels[y][x]

def box(L):
    """ 
    boxes the flat pixels in row L
    assumes three channels!
    """
    newL = []
    STRIDE = 4  # since we're using RGBA!
    for i in range(len(L)/STRIDE):
        newL.append( L[STRIDE*i:STRIDE*i+3] ) # since we're providing RGB
    return newL

def new_image(width, height):
    '''Create and return a new Image object of the specified width and height.'''
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append( (0,0,0) )
        pixels.append(row)
    return Image(pixels)

def copy_image(image):
    '''Make and return a complete copy of the given image object.'''
    w, h = image.width(), image.height()
    img_copy = new_image(w, h)
    for y in range(h):
        for x in range(w):
            img_copy.set_rgb(x, y, image.get_rgb(x, y))
    return img_copy

def save_to_file(image, filename):
    '''Save the image to a file of the given name.'''
    f = open(filename, 'wb')      # binary mode is important
    w = png.Writer( image.width(), image.height() )
    w.write_array(f, list(image._get_flat_pixel_list()))
    f.flush()
    os.fsync(f.fileno())
    f.close()

def load_from_file(filename):
    '''
    Load an image from the file named filename.  Return
    a new image if the file is found.  
    
    The supported file type is .png.
    '''
    fcomponent = os.path.basename(filename)      
    (fbase, ext) = os.path.splitext(fcomponent)

    # check the file format and attempt to convert if possible
    if not ext in ['.png']:
        print >>sys.stderr,"Can't handle image of type {0}.  You'll need to manually convert to .png in order to use this image. You can find free image converters online.".format(ext)
        sys.exit(0)
    
    # we'll only get here if we have an image we can actually work with
    # print "Opening the", filename, " file (each dot is a row)",
    reader = png.Reader(filename)
    #data = reader.read()
    data = reader.asRGBA()
    width = data[0]
    height = data[1]
    pixels = data[2]  # this is an iterator...
    PIXEL_LIST = []
    while True:
        try:
            a = pixels.next()    # one row of boxed row flat pixel format w/ alpha channel
            # print ".",
            sys.stdout.flush()
            PIXEL_LIST.append( box( a.tolist() ) )
        except StopIteration:
            # print "\nFile read."
            break
    
    return Image(PIXEL_LIST)


class ImageFilterFrame(Tkinter.Frame):
    '''
    The main graphical frame that wraps up the buttons and canvas for
    drawing the image.  Implemented in straight Tkinter.
    '''
    def __init__(self, images):
        self.root = Tkinter.Tk()
        self.imagelist = [self.__translate(img) for img in images]

        Tkinter.Frame.__init__(self, self.root)
        self.root.title('COSC 101 image display')
        self.grid()
        self.__createWidgets()

    def __createWidgets(self):
        '''
        Create on-screen widgets.
        '''
        self.quitbutton = Tkinter.Button(self, text="Quit", command=self.quit)
        self.quitbutton.grid(column=0, row=0)

        rowval = 1
        colval = 0
        for image in self.imagelist:
            self.canvas = Tkinter.Canvas(self)
            self.canvas["width"] = image.width()
            self.canvas["height"] = image.height()
            self.canvas["relief"] = 'raised'
            self.canvas.create_image((0, 0), anchor='nw', image=image, state=Tkinter.DISABLED)
            self.canvas.grid(column=colval, row=rowval)

            if colval == 0:
                colval = 1
            else:
                colval = 0
                rowval += 1

    def display(self):
        '''
        Display the images and go into the tk mainloop.
        '''
        self.root.mainloop()
        try:
            self.root.destroy()
        except:
            pass

    def __translate(self, img):
        """
        Takes an Image object and returns a Tkinter.PhotoImage
        """
        if not isinstance(img, Image):
            raise InvalidImageTypeException("display_images only accepts objects of type Image")

        w = img.width()
        h = img.height()
        tkimg = Tkinter.PhotoImage(width=w, height=h)
        for x in range(w):
            for y in range(h):
                tkimg.put('#%02x%02x%02x' % img.get_rgb(x, y), (x, y))
        return tkimg


def display_images(*images):
    '''
    Display images in a window.  This function accepts any number of Image
    objects, separated by commas.
    '''
    frame = ImageFilterFrame(images)
    frame.display()


if __name__ == "__main__":
    print >>sys.stderr, '''You should not run this file directly.  It should only be imported.'''
    print >>sys.stderr, '''Read the instructions carefully on how to use this code.'''
