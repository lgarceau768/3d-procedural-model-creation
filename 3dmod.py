from vpython import *
import random

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

def getCorners(obj):
    '''
    inherit traits
    neck y/n
    tail y/n
    quadrapetal y/n
    bipedal y/n
    wings y/n
    '''
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
    neck = vector(-length/2, height/2, 0) + center
    tail = vector(length/2, -height/2, 0) + center
    return {
        'bottomFrontLeft': a,
        'bottomFrontRight': b,
        'bottomBackLeft': g,
        'bottomBackRight': h,
        'topFrontLeft': c,
        'topFrontRight': d,
        'topBackLeft': e,
        'topBackRight': f,
        'neck': neck,
        'tail': tail

    }

def addJoints(obj):
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

def createHead(obj):
    obj = obj.getObj()
    center = obj.pos
    width = obj.width
    height = obj.height
    length = obj.length
    '''
    inherit traits
    head size #
    neck length #
    neck y/n
    '''
    neckLength = random.randrange(2, 4, 1) 
    a = sqrt((neckLength*neckLength)/2)
    neckStart = vector((-length/2)-(a/2), (height/2)+(a/2), 0) + center
    neck = createBox("neck", neckStart, vector(-1, 1, 0), vector(0,0,0), neckLength, 0.25, 0.25)
    headSpot = neckStart + vector(-a/2, a/2, 0) 
    headSize = random.randrange(1, neckLength, 1)/2
    head = createSphere('head', headSpot, headSize)
    return [neck, head]

def createLimbs(obj, joints):
    '''
    inherit traits
    jointsToCreateLimbs list
    limbHeight
    limbWidth
    limbLength
    '''
    jointsToCreateLimbs = ['bottomFrontLeftJoint', 'bottomBackLeftJoint', 'bottomFrontRightJoint', 'bottomBackRightJoint']
    limbHeight = random.randrange(1, 6, 1)
    limbWidth = random.randrange(1, 4)/4
    limbLength = random.randrange(1, 4)/4
    limbs = []
    for joint in joints:
        name = joint.getName()
        jointObj = joint.obj
        if name in jointsToCreateLimbs:
            limbPos = jointObj.pos + vector(0, (-limbHeight/2), 0)
            # limbs will go straight down
            limb = createBox(name+'Limb', limbPos, vector(0,0,0), vector(0,0,0), limbLength, limbWidth, limbHeight)
            limbs.append(limb)
            print(joint)
    return limbs

def createMonster():
    '''
    inherit traits
    length #
    width #
    height #
    tail y/n
    neck y/n
    wings y/n
    quadrapetal y/n
    bipedal y/n
    '''
    length = random.randrange(1, 10, 1)
    width = random.randrange(1, 7, 1)
    height = random.randrange(1, 3, 1)
    body = createBox("mainBody", vector(0, 0, -5), vector(0, 0, 0), vector(0, 0, 0), length, width, height)
    joints = addJoints(body)
    [neck, head] = createHead(body)
    limbs = createLimbs(body, joints)
    print('done')

# attempt to create a four legged creatue with a head and body
createMonster()
