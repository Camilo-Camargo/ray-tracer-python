import math


class Sphere():

    def __init__(self, center, radius):
        self.__center = center
        self.__radius = radius

    def append(self, other):
        self.__hittable

    def __str__(self):
        return f"Sphere center: ({self.__center} radius: {self.__radius})"

    def hit(self, r, t_min, t_max, hit_rec):
        C = r.origin() - self.__center
        a = r.direction().len_sqr()
        half_b = C.dot(r.direction())
        c = C.len_sqr() - (self.__radius * self.__radius)
        discriminant = half_b*half_b - a*c

        if(discriminant < 0):
            return False
        sqrtd = math.sqrt(discriminant)

        # Find the nearest root
        root = (-half_b - sqrtd) / a

        if((root < t_min) or (t_max < root)):
            root = (-half_b + sqrtd) / a
            if(root < t_min or t_max < root):
                return False

        hit_rec.t(root)
        hit_rec.p(r.at(hit_rec.t()))  
        outward_normal = (hit_rec.p() - self.__center) // self.__radius
        hit_rec.set_face_normal(r,outward_normal)

        return True
