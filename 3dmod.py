from vpython import *

class customObj:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def getObj(self):
        return self.model

    def getName(self):
        return self.name

def createBox(name, posVector, rotationVector, l, w, h):
    '''
    position and rotation starts at 0,0,0 x,y,z
    axis x and y for a slanted look
    '''
    model = box(pos=posVector, axis=rotationVector, length=l, width=w, height=h)
    return customObj(model, name)

armSegment = createBox("arm1", vector(-3,0,-2), vector(3,3,0), 0.5, 0.5, 6)
print(armSegment.getName())