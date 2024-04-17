class Ray():
    """ 
    Equation
        P(t) = A + t(b)  

        where
        A is the orgin of the ray
        b is the direction of the ray 
        P(t) is a point in 3D space
    """
    def __init__(self, origin, direction):
        self.__A = origin
        self.__b = direction 

    def at(self, t):
        return self.__A + self.__b**t

    def origin(self):
        return self.__A 

    def direction(self):
        return self.__b




