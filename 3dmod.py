from vpython import *

class customObj:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def getObj(self):
        return self.model

    def getName(self):
        return self.name

class customBody:
    def __init__(self, list, name):
        self.list = list
        self.name = name
    
    def getName(self):
        return self.name

    def getBodyParts(self):
        return self.list

def createBox(name, posVector, axisVector, rotationVector, l, w, h):
    '''
    position and rotation starts at 0,0,0 x,y,z
    axis x and y for a slanted look
    '''
    model = box(pos=posVector, axis=axisVector, up=rotationVector, length=l, width=w, height=h)
    return customObj(model, name)

def createSphere(name, posVector, r):
    '''
    position is based of x,y,z
    '''
    model = sphere(pos=posVector, radius=r)
    return customObj(model, name)

def createBodyList(name, args):
    body = []
    for arg in args:
        body.append(args)
    return customBody(name, body)



def getCorners(obj):
    obj = obj.getObj()
    edges = []
    # need to find the edges of the box
    # positin is the center of the object
    center = obj.pos
    height = obj.height
    width = obj.width
    length = obj.length
    print(center, height, width, length)
    '''
    e  _______ f
c   _/_|___ /| d
    |  |  |  | 
    | g|__|__|h
    |/____| /
a          b
    '''
    a = vector(-length/2, -height/2, width/2) + center
    b = vector(length/2, -height/2, width/2) + center
    c = vector(-length/2, height/2, width/2) + center
    d = vector(length/2, height/2, width/2) + center
    e = vector(-length/2, height/2, -width/2) + center
    f = vector(length/2, height/2, -width/2) + center
    g = vector(-length/2, -height/2, -width/2) + center
    h = vector(length/2, -height/2, -width/2) + center
    return {
        'bottomFrontLeft': a,
        'bottomFrontRight': b,
        'bottomBackLeft': g,
        'bottomBackRight': h,
        'topFrontLeft': c,
        'topFrontRight': d,
        'topBackLeft': e,
        'topBackRight': f
    }

# attempt to create a four legged creatue with a head and body

body = createBox("mainBody", vector(0, 0, -5), vector(0, 0, 0), vector(0, 0, 0), 10, 3, 1)

corners = getCorners(body)
for c in corners:
    print(c, corners[c])
    s = createSphere('sphere', corners[c], 0.25)
