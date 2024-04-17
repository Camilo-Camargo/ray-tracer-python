## Standard libraries
import math
import sys 
import random  
import png

## Developer Libarries
from formats.ppm import PPM
from la.vec3 import Vec3
from tracer.camera import Camera
from tracer.ray import Ray
from tracer.hittable import Hittable, HitRecord, HittableList
from objects.sphere import Sphere


def ray_color(r, world, depth):  

    if(depth <= 0):
        return Vec3(0,0,0)

    rec = HitRecord(Vec3(0,0,0), Vec3(0,0,0), 0) 
    #if(world.hit(r, 0, math.inf, rec)):  
        #target = rec.p() + rec.n() + Vec3.random() 
        #print(target)
        #return (ray_color(Ray(rec.p(), target - rec.p()), world, depth-1)) ** 0.5 


    if(world.hit(r, 0, math.inf, rec)):
        return (Vec3(1,1,1) + rec.n()) ** 0.5

    u = r.direction().unit()
    t = 0.5 * (u.y() + 1.0)
    #lerp here
    return Vec3(1,1,1)**(1 - t) + Vec3(0.5,0.7, 1.0)**t


 


def main():   
    ## Vec3 List
    img = []

    width = 720
    depth = 1
    aspect_ratio = 16.0/9.0
    height = math.floor(width / aspect_ratio) 
    samples_per_pixels = 1
    ppm = PPM("render/image.ppm", width, height)    


    ## Camera
    camera = Camera(100, 16/9, Vec3(0,0,0))

    ## World
    world = HittableList()
    world.append(Sphere(Vec3(0,-100.5,-1), 100))
    world.append(Sphere(Vec3(0,0,-1), 0.5))   
    world.append(Sphere(Vec3(0,0,-1), 0.2))   


    ## Tracing
    for y in reversed(range(height)):
        print(f"Scalines remaining: {y}", end="\r")
        sys.stdout.flush() 
        for x in range(width):  
            c = Vec3(0,0,0)
            for s in range(samples_per_pixels):
                u = (x + random.random()) / (width-1)
                v = (y + random.random()) / (height-1)   
                r = camera.get_ray(u,v)
                c = c + ray_color(r, world, depth)
                ppm.write(c.x(), c.y(), c.z(), samples_per_pixels);
                #img.append(c)
    for c in img:
        pass
        


if(__name__ == "__main__"): 
    main()
