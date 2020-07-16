from vpython import *
from random import *
from models import *

def createHead(obj):
    obj = obj.getObj()
    center = obj.pos
    width = obj.width
    height = obj.height
    length = obj.length
    
    neckLength = randrange(2, 4, 1)/2
    a = sqrt((neckLength*neckLength)/2)
    neckStart = vector((-length/2)-(a/2), (height/2)+(a/2), 0) + center
    neck = createBox("neck", neckStart, vector(-1, 1, 0), vector(0,0,0), neckLength, 0.25, 0.25)
    
    headSpot = neckStart + vector(-a/2, a/2, 0) 
    headSize = randrange(2, 4, 1)
    head = createSphere('head', headSpot, headSize/6)
    
    beakLength = randrange(1, 4, 1)/4
    beakHeight = randrange(1, headSize, 1)/4
    beakWidth = randrange(1, headSize, 1)/4
    beakStart = headSpot + vector(-headSize/10, -headSize/10, 0)
    beak = createPyramid('beak', beakStart, vector(-1, -1, 0), beakLength, beakWidth, beakHeight)
    return neck, head, beak

def getCorners(obj):
    obj = obj.getObj()    
    center = obj.pos
    height = obj.height
    width = obj.width
    length = obj.length
    
    neck = vector(-length/2, height/2, 0) + center
    leftWing = vector(-length/4, height/2, width/2) + center
    rightWing = vector(-length/4, height/2, -width/2) + center
    backLeftFoot = vector(length/4, -height/2, width/2) + center
    backRightFoot = vector(length/4, -height/2, -width/2) + center
    tail = vector(length/2, height/2, 0) + center
    return {
        'neck':neck,
        'leftWing':leftWing,
        'rightWing':rightWing,
        'backLeftFoot':backLeftFoot,
        'backRightFoot':backRightFoot,
        'tail':tail
    }

def makeWings(obj, joints):
    wingArmLength = randrange(1, obj.model.length*2, 1)
    wingArmWidth = randrange(1, 4, 1)/4
    wingArmHeight = randrange(1, 4, 1)/8
    limbs = []
    for joint in joints:
        name = joint.getName()
        if 'Wing' in name:
            jointObj = joint.obj
            # wing arm            
            if 'left' in name:
                a = sqrt((wingArmLength*wingArmLength)/2)
                wingArmPos = jointObj.pos + vector(0, a/2, a/2)
                wing = createBox(name+"Limb", wingArmPos, vector(0,1,1), vector(0,0,0), wingArmLength, wingArmWidth, wingArmHeight)
            elif 'right' in name: 
                a = sqrt((wingArmLength*wingArmLength)/2)
                wingArmPos = jointObj.pos + vector(0, a/2, -a/2)
                wing = createBox(name+"Limb", wingArmPos, vector(0,1,-1), vector(0,0,0), wingArmLength, wingArmWidth, wingArmHeight)
            limbs.append(wing)
    return limbs

def createBird():
    length = randrange(2, 5, 1)
    width = randrange(1, 4, 1)/4
    height = randrange(1, 4, 1)/4

    body = createBox("body", vector(0, 0, -2), vector(0, 0, 0), vector(0, 0, 0), length, width, height)
    joints = addJoints(body, getCorners)
    [neck, head, beak] = createHead(body)
    limbs = makeWings(body, joints)

createBird()

