import math
import random


class Vec3:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z   

    def __getitem__(self, key):
        return {
                0: self.__x,
                1: self.__y,
                2: self.__z
                }.get(key)

    ## Mathematical Overriding 
    def __neg__(self): 
        return Vec3(
            self.__x * -1,
            self.__y * -1,
            self.__z * -1 
            ) 

        ## Vec3 color = Vec3(1,1,1) 
        ## -color 

    def __add__(self, other):
        return Vec3(
                self.x() + other.x(),
                self.y() + other.y(),
                self.z() + other.z()
                ) 

    def __sub__(self, other):
        return Vec3(
                self.x() - other.x(),
                self.y() - other.y(),
                self.z() - other.z() 
                )

    def __isub__(self, t):
        return Vec3(
                self.__x - t,
                self.__y - t,
                self.__z - t
                )

    def __iadd__(self, t):
        return Vec3(
                self.__x + t,
                self.__y + t,
                self.__z + t
                )

    def __mul__(self, other):
        return Vec3(
                self.x() * other.x(),
                self.y() * other.y(),
                self.z() * other.z() 
                ) 

    def __pow__(self, t):
        return Vec3(
                self.x() * t,
                self.y() * t,
                self.z() * t 
                )  

    def __xor__(self, t):
        return Vec3(
                self.x() ** t,
                self.y() ** t,
                self.z() ** t 
                )  



    def __imul__(self, t): 
        self.__x *= t
        self.__y *= t
        self.__z *= t
        return self

    def __idiv__(self, t): 
        self.__x /= t
        self.__y /= t
        self.__z /= t
        return self 

    def __truediv__(self, other):
        return Vec3(
                self.__x / other.x(),
                self.__y / other.y(), 
                self.__z / other.z()
                ) 

    def __floordiv__(self, t):
         return Vec3(
                self.__x / t,
                self.__y / t, 
                self.__z / t
                ) 

    def __str__(self):
        return f"[{self.__x},{self.__y},{self.__z}]"   

    def len_sqr(self):
        return (self.__x * self.__x + 
                self.__y * self.__y + 
                self.__z * self.__z) 

    def dot(self, other):
        v = self * other 
        return v.x() + v.y() + v.z()

    def cross(self, other):
        return Vec3(
                self.__y*other.z() - self.__z * other.y(),
                self.__x*other.z() - self.__z * other.x(),
                self.__x*other.y() - self.__y * other.x()
                ) 

    def unit(self):
        return Vec3(
                    self.__x/self.len(),
                    self.__y/self.len(),
                    self.__z/self.len()
                    ) 

    def __le__(self, other):
            self.__x = other.x()
            self.__y = other.y()
            self.__z = other.z()

    @staticmethod
    def random():
        return Vec3(random.randrange(0, 1), random.randrange(0, 1), random.randrange(0,1))
                 
    def len(self):
        return math.sqrt(self.len_sqr()) 

    def x(self):
        return self.__x 

    def y(self):
        return self.__y 

    def z(self):
        return self.__z
