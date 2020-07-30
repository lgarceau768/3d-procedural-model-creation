from vpython import *
from random import *
from models import *
import time

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
    # need to find the edges of the box
    # positin is the center of the object
    center = obj.pos
    height = obj.height
    width = obj.width
    length = obj.length
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
    neckLength = randrange(2, 4, 1) 
    a = sqrt((neckLength*neckLength)/2)
    neckStart = vector((-length/2)-(a/2), (height/2)+(a/2), 0) + center
    neck = createBox("neck", neckStart, vector(-1, 1, 0), vector(0,0,0), neckLength, 0.25, 0.25)
    headSpot = neckStart + vector(-a/2, a/2, 0) 
    headSize = randrange(1, neckLength, 1)/2
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
    limbHeight = randrange(1, 6, 1)
    limbWidth = randrange(1, 4)/4
    limbLength = randrange(1, 4)/4
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

def createQuad(id):
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
    length = randrange(1, 10)
    width = randrange(1, 7)
    height = randrange(1, 3)
    body = createBox("mainBody", vector(0, 0, -5), vector(0, 0, 0), vector(0, 0, 0), length, width, height)
    joints = addJoints(body, getCorners)
    [neck, head] = createHead(body)
    limbs = createLimbs(body, joints)
    parts = [head, neck, body]
    for limb in limbs: 
        parts.append(limb)
    creatureBody = customBody(parts, joints, 'customQuad#'+id)
    print('done')
    return creatureBody




# attempt to create a four legged creatue with a head and bodyW
model = createQuad(str(time.time()).split('.')[0])
createSTL(model)