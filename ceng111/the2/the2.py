
def isOnAxis(rect1):
    e=0.001
    if abs(rect1[1])<e:
        return True
    elif abs(rect1[3])<e:
        return True
    else:
        return False

def coincide(rect1,rect2):
    e=0.001
    if abs(rect1[1]-rect2[1])<e or abs(rect1[1]-rect2[3])<e:
        return True
    elif abs(rect1[3]-rect2[1])<e or abs(rect1[3]-rect2[3])<e:
        return True
    else:
        return False

def centerOfMass(rect1,rect2):
    rect1y=[rect1[1],rect1[3]]
    rect2y=[rect2[1],rect2[3]]
    rect1x=[rect1[0],rect1[2]]
    rect2x=[rect2[0],rect2[2]]

    if max(rect1y)>max(rect2y):
        if (sum(rect1x)/2)<=max(rect2x) and (sum(rect1x)/2)>=min(rect2x):
            return True
        else:
            return False
    else:
        if (sum(rect2x)/2)<=max(rect1x) and (sum(rect2x)/2)>=min(rect1x):
            return True
        else:
            return False



def calculateArea(rect1,rect2):
    rect1x=[rect1[0],rect1[2]]
    rect1y=[rect1[1],rect1[3]]
    rect2x=[rect2[0],rect2[2]]
    rect2y=[rect2[1],rect2[3]]

    area1=abs(rect1[0]-rect1[2])*abs(rect1[1]-rect1[3])
    area2=abs(rect2[0]-rect2[2])*abs(rect2[1]-rect2[3])
    xLine=min(max(rect1y),max(rect2y))-max(min(rect1y),min(rect2y))
    yLine=min(max(rect1x),max(rect2x))-max(min(rect1x),min(rect2x))
    if xLine>0 and yLine>0:
        area3=xLine*yLine
    else:
        area3=0

    return area1+area2-area3;


def is_firmus(rect1,rect2):
    rect1x=[rect1[0],rect1[2]]
    rect1y=[rect1[1],rect1[3]]
    rect2x=[rect2[0],rect2[2]]
    rect2y=[rect2[1],rect2[3]]


    if (isOnAxis(rect1) and not isOnAxis(rect2)) or (isOnAxis(rect2) and not isOnAxis(rect1)):
        if coincide(rect1,rect2):
            if centerOfMass(rect1,rect2):
                return ["FIRMUS",calculateArea(rect1,rect2)]
            else:
                if max(rect1y)>max(rect2y):
                    center=float(sum(rect1x))/2
                    if center>max(rect2x):
                        newx=min(rect1x)-(center-max(rect2x))*2
                        block=[min(rect1x),min(rect1y),newx,max(rect1y)]
                        return ["ADDENDUM",block]
                    else:
                        newx=max(rect1x)+(min(rect2x)-center)*2
                        block=[max(rect1x),min(rect1y),newx,max(rect1y)]
                        return ["ADDENDUM",block]

                else:
                    center=float(sum(rect2x))/2
                    if center>max(rect1x):
                        newx=min(rect2x)-(center-max(rect1x))*2
                        block=[min(rect2x),min(rect2y),newx,max(rect2y)]
                        return ["ADDENDUM",block]
                    else:
                        newx=max(rect2x)+(min(rect1x)-center)*2
                        block=[max(rect2x),min(rect2y),newx,max(rect2y)]
                        return ["ADDENDUM",block]

        else:
            return ["DAMNARE",calculateArea(rect1,rect2)]

    else:
        return ["DAMNARE",calculateArea(rect1,rect2)]
