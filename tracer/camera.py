from la.vec3 import Vec3
from tracer.ray import Ray


class Camera:
    ## Camera
 

    def __init__(self, width, aspect_ratio, origin): 
        self.__origin = origin
        self.__width = width
        self.__height = width / aspect_ratio
        self.__vw_height = 2.0
        self.__vw_width =  aspect_ratio * self.__vw_height 
        self.__horizontal = Vec3(self.__vw_width, 0, 0)
        self.__vertical = Vec3(0, self.__vw_height, 0)  
        self.__focal_length = 1.0
        
        self.__lower_left_corner = self.__origin - self.__horizontal//2 - self.__vertical//2 - Vec3(0,0,self.__focal_length)     
 
    def get_ray(self, u, v):
        return Ray(self.__origin, self.__lower_left_corner + (self.__horizontal**u) + (self.__vertical**v) - self.__origin)

