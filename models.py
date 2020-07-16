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
    def __init__(self, parts, joints, name):
        self.name = name
        self.parts = parts 
        self.joints = joints

    def addJoint(self, joint):
        self.joints.append(joint)

    def addPart(self, part):
        self.parts.append(part)

    def getJoints(self):
        return self.joints
    
    def getName(self):
        return self.name

    def getBodyParts(self):
        return self.parts

class customJoint:
    name = ''
    obj = ''
    def __init__(self, initialPart, name, obj):
        self.part1 = initialPart
        self.name = name
        self.obj = obj
        self.compound = compound([initialPart, obj])

    def connect(self, part2):
        self.compound = compound([self.part1, self.obj, part2])
        self.part2 = part2

    def getName(self):
        return self.name
    
    def getObj(self):
        self.obj

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

def createPyramid(name, posVector, axisVector, l, w, h):
    '''
    position and rotation starts at 0,0,0 x,y,z
    axis x and y for a slanted look
    '''
    model = pyramid(pos=posVector, size=vector(l,w,h), axis=axisVector)
    return customObj(model, name)

def addJoints(obj, getCorners):
    '''
    inherit traits
    neck y/n
    tail y/n
    quadrapetal y/n
    bipedal y/n
    wings y/n
    '''
    corners = getCorners(obj)
    joints = []
    for c in corners:
        s = createSphere(c+'Joint', corners[c], 0.25)
        joints.append(customJoint(obj.getObj(), c+'Joint', s.getObj()))
    return joints