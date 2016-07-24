import math

class Vector3D(object):
### START YOUR CLASS IMPLEMENTATION HERE ###

    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z;
        pass

    def r(self):
        return (self.x**2+self.y**2+self.z**2)**0.5;

    def theta(self):
        return math.acos(self.z/self.r());

    def phi(self):
        return math.atan2(self.y,self.x);

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
print 'v1 in spherical coordinate: (%.4f, %4f, %.4f)' % (v1.r(), v1.theta(), v1.phi())

v2 = Vector3D(5.2,7.4,-2.5)
print 'v2 in spherical coordinate: (%.4f, %4f, %.4f)' % (v2.r(), v2.theta(), v2.phi())

