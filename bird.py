from vpython import *
from random import *
from models import *
import time

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

def createTail(obj, joints):
    tailLength = randrange(1, 4, 1)/3
    tailWidth = randrange(1, 4, 1)/3
    tailHeight = randrange(1, 4, 1)/8
    for joint in joints:
        name = joint.getName()
        if 'tail' in name:
            jointObj = joint.obj
            # wing arm           
            a = sqrt((tailLength*tailLength)/2)
            tailPos = jointObj.pos + vector((a/2)+0.10, (a/2)+0.10, 0)
            tail = createBox(name+"Tail", tailPos, vector(1,1,0), vector(0,0,0), tailLength, tailWidth, tailHeight)
    return tail

def createFeet(obj, joints):
    feetLength = randrange(1, 4, 1)/4
    feetWidth = randrange(1, 4, 1)/4
    feetHeight = randrange(1, 4, 1)/4
    feet = []
    for joint in joints:
        name = joint.getName()
        if 'Foot' in name:
            jointObj = joint.obj
            # wing arm           
            a = sqrt((feetLength*feetLength)/2)
            feetPos = jointObj.pos + vector(-(a/2), -(a/2), 0)
            foot = createBox(name+"foot", feetPos, vector(0,0,0), vector(0,0,0), feetLength, feetWidth, feetHeight)
            feet.append(foot)
    return feet

def createBird(id):
    length = randrange(2, 5, 1)
    width = randrange(1, 4, 1)/4
    height = randrange(1, 4, 1)/4

    body = createBox("body", vector(0, 0, -2), vector(0, 0, 0), vector(0, 0, 0), length, width, height)
    joints = addJoints(body, getCorners)
    [neck, head, beak] = createHead(body)
    limbs = makeWings(body, joints)
    tail = createTail(body, joints)
    feet = createFeet(body, joints)
    parts = [neck, head, beak, body, tail, feet[0], feet[1]]
    bird = customBody(parts, joints, 'customBird#'+id)
    return bird


createBird(str(time.time()))