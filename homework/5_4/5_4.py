class Vector3D(object):
### START YOUR CLASS IMPLEMENTATION HERE ###

    def __init__(self,x=0.,y=0.,z=0.):
        self.x, self.y, self.z = x,y,z;
        pass

    def __str__(self):
        return '(%g,%g,%g)' % (self.x, self.y, self.z);

    def __add__(self, input):
        return Vector3D(self.x+input.x, self.y+input.y, self.z+input.z)

    def __sub__(self, input):
        return Vector3D(self.x-input.x, self.y-input.y, self.z-input.z)

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
v2 = Vector3D(5.2,7.4,-2.5)
v3 = Vector3D(2.1,4.2,0.0)

print 'v1+v2 =', v1+v2
print 'v1-v2 =', v1-v2
print 'v1+v3 =', v1+v3
print 'v1-v3 =', v1-v3

