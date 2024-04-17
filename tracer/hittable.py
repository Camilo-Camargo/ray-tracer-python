import math
from multipledispatch import dispatch

from la.vec3 import Vec3
from tracer.ray import Ray



class HitRecord:
    def __init__(self, p, normal, t):
        self.__p = p
        self.__n = normal
        self.__t = t  

    def set_face_normal(self, r, outward_normal):
        self.__front_face = r.direction().dot(outward_normal) 
        if(self.__front_face): 
            self.__n = outward_normal
        else:
            self.__n = -outward_normal

    def __le__(self, other):
        self.__p <= other.p()
        self.__n <= other.n()
        self.__t = other.t()

    @dispatch()
    def p(self):
        return self.__p

    @dispatch()
    def n(self):
        return self.__n

    @dispatch()
    def t(self):
        return self.__t

    @dispatch(Vec3)
    def p(self, p):
        self.__p = p

    @dispatch(Vec3)
    def n(self, n):
        self.__n = n

    @dispatch(int)
    def t(self, t):
        self.__t = t

    @dispatch(float)
    def t(self, t):
        self.__t = t

class Hittable:
        def __init__(self):
            pass

        def hit(self, r, t_min, t_max, hit_rec):
            pass

class HittableList(Hittable):

    def __init__(self):
        self.__hittable_list = []
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.__index == len(self.__hittable_list)):
            self.__index = 0
            raise StopIteration

        ret = self.__hittable_list[self.__index]   
        self.__index = self.__index + 1 
        return ret

    def __str__(self):
        return f"{self.__hittable_list[self.__index]}"

    def append(self, other):
        self.__hittable_list.append(other) 

    def hit(self, r, t_min, t_max, hit_rec: HitRecord):
        temp_rec = HitRecord(Vec3(0,0,0), Vec3(0,0,0), 0)
        hit_anything = False

        for obj in self.__hittable_list:
            if (obj.hit(r, t_min, t_max, temp_rec)):
                hit_anything = True
                closest_so_far = temp_rec.t
                hit_rec <= temp_rec 
        return  hit_anything

