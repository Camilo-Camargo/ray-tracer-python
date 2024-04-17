import math


class PPM():
    """ PPM file format structure
        P3
        width height
        255 # is the max color
    """

    def __init__(self, path, width, height):
        self.__path = path
        self.__file = open(path, "w+")
        self.__file.write("P3\n{0} {1}\n255\n".format(width, height))

    def __str__(self):
        return self.path

    def __del__(self):
        self.__file.close()

    def __clamp(self, value, min, max):
        if (value < min):
            return min
        elif(value > max):
            return max
        return value

    def write(self, red, green, blue):
        """ Write the next color pixels until exhausted """
        min = 0
        max = 1

        red = math.floor(self.__clamp(red, min, max) * 255)
        green = math.floor(self.__clamp(green, min, max) * 255)
        blue = math.floor(self.__clamp(blue, min, max) * 255)

        self.__file.write("{0} {1} {2}\n".format(red, green, blue))

    def write(self, red, green, blue, samples_per_pixels):
        """ Write the next color pixels until exhausted """ 
        min = 0
        max = 1  

        scale = 1 / samples_per_pixels 
        red   = math.sqrt(red*scale)
        green = math.sqrt(green*scale)
        blue  = math.sqrt(blue*scale)

        red = math.floor(self.__clamp(red, min, max) * 255)
        green = math.floor(self.__clamp(green, min, max) * 255)
        blue = math.floor(self.__clamp(blue, min, max) * 255) 

        self.__file.write("{0} {1} {2}\n".format(red, green, blue))




