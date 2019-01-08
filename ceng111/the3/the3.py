from evaluator import *


"""Use get_data() to Get the initial state of the particles & the environment
    * Returns [G, Dt, [m1, x1, y1, vx1, vy1], ...., [mn, xn, yn, vxn, vyn]]"""




"""Function that calculates the position updates.
   * Returns [[Delta_x1, Delta_y2], ..., [Delta_xm, Delta_ym]]"""
data=[]

def new_move():
    global data
    if data == []:
        data = get_data()



    masses = data[2:]
    gforce = data[0]
    time = data[1]

    positions=[]


    for m in range(len(masses)):
        mass = masses[m]

        velX = mass[3]
        velY = mass[4]

        dposX = velX*time
        dposY = velY*time

        data[m+2][1]=mass[1]+dposX
        data[m+2][2]=mass[2]+dposY

        positions.append([dposX,dposY])


    masses = data[2:]
    forces = findForce(masses,gforce)
    for m in range(len(masses)):
        mass = masses[m]
        force = forces[m]
        accelerationX = force[0]/mass[0]
        accelerationY = force[1]/mass[0]
        velX = mass[3]
        velY = mass[4]

        data[m+2][3] = velX + accelerationX * time
        data[m+2][4] = velY + accelerationY * time



    return positions


def findForce(list,g):
    forceList=[]
    for e in list:
        totalForceX=0
        totalForceY=0
        for i in list:
            if e==i:
                currentForceX=0
                currentForceY=0
            else:
                currentDistance = ((e[1]-i[1])**2 + (e[2]-i[2])**2)**0.5

                direction = [i[1]-e[1],i[2]-e[2]]
                currentForceX = (g*e[0]*i[0]/(currentDistance)**2) * convertToUnit(direction)[0]
                currentForceY = (g*e[0]*i[0]/(currentDistance)**2) * convertToUnit(direction)[1]
                totalForceX += currentForceX
                totalForceY += currentForceY
        forceList.append([totalForceX,totalForceY])

    return forceList


#here it converts a vector to its unit notation
def convertToUnit(vector):
    magnitude = (vector[0]**2 + vector[1]**2)**0.5
    return [vector[0]/magnitude,vector[1]/magnitude]
