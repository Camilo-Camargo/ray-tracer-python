##Recreation a implementation: 
## Credits: https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt


from inspect import getfullargspec

class Function(object):
    """ Wrap all functions """
    def  __init__(self, fn):
        self.fn = fn

    def __call__ (self, *args, **kwargs):
        """ Invoke internally the desired function """
        return self.fn(*args, **kwargs)

    def key(self, args=None):
        """ Return the key of the function """
        if args is None:
            args = getfullargspec(self.fn).args

        return tuple(
                [
                self.fn.__module__,
                self.fn.__class__,
                self.fn.__name__,
                len(args or []),
                ])  


class Namespace(object):
    """ holding all the functions """

    __instance = None

    def __init__(self):
        if(self.__instance is None):
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception("Cannot instantiate a virtual Namespace again");
        @staticmethod
        def get_instance(): 
            if Namespace.__instance is None:
                Namespace()
            return Namespace.__instance

        def register(self, fn):
            func = Function(fn)
            self.function_map[func.key()] = fn
            return func


def override(fn):
    """ Overload each function with  the same name """

    return Namespace.get_instance.register(fn)


@override
def main(a,b):
    print (a,b) 

@override
def main(a):
    print(a)

main()






