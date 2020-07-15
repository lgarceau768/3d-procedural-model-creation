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

def createBox(name, posVector, rotationVector, l, w, h):
    '''
    position and rotation starts at 0,0,0 x,y,z
    axis x and y for a slanted look
    '''
    model = box(pos=posVector, axis=rotationVector, length=l, width=w, height=h)
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


armSegment = createBox("arm1", vector(-3,0,-2), vector(0,0,0), 0.5, 0.5, 6)
sphereSegment = createSphere("head", vector(-3, 3.5, -2), 0.5)
body1 = createBodyList("body1", [armSegment, sphere])

