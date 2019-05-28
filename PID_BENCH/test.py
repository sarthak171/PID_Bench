import matplotlib.pyplot as plt
import math
import copy
import time
from matplotlib.animation import FuncAnimation

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x, y):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

# class Robot:


def distanceForm(xi, yi, xii, yii): #distanc formula
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)
 
def smoothing(path, a, b, tolerance, length): #path, random nums, length of array
    newPath = copy.deepcopy(path) #copy original path
    change = tolerance # okay worthless

    while(change >= tolerance): 
        change = 0.0 
        for i in range(1, length-1):
            for j in range(0, 2):
                # print(str(path[j][i]) + " " + str(newPath[j][i]))
                add = a * (path[j][i] - newPath[j][i])
                add2 = b * (newPath[j][i-1] + newPath[j][i+1] - (2.0 * newPath[j][i]))


                aux = newPath[j][i]
                newPath[j][i] += add
                newPath[j][i] += add2
                change += math.fabs(aux - newPath[j][i])


                # print(str(i)+" "+str(j)+" "+str(add)+" "+str(add2)+" "+str(change))

        # plt.scatter(array[0], array[1])

    return newPath

array = [0] * 4 #original path if draw straight line between points
array[0] = [0] * 50
array[1] = [0] * 50
array[2] = [0] * 50 
array[3] = [0] * 50 #final path points

spacing = 15 #distance between points on graph
p1 = Point(90, 20) #points on path
p2 = Point(100, -50)
p3 = Point(160, 20) 
p4 = Point(190, -40) 
# start_point = 100

deltaY = p2.y - p1.y #differences in y and x between points
deltaX = p2.x - p1.x
deltaYY = p3.y - p2.y
deltaXX = p3.x - p2.x
deltaYYY = p4.y - p3.y
deltaXXX = p4.x - p3.x

distance = distanceForm(p1.x, p1.y, p2.x, p2.y) #distances between points 
distance2 = distanceForm(p2.x, p2.y, p3.x, p3.y)
distance3 = distanceForm(p3.x, p3.y, p4.x, p4.y)

num_points_that_fit = (int)(math.ceil(distance / spacing)) #num of points on graph
num_points_that_fit2 = (int)(math.ceil(distance2 / spacing))
num_points_that_fit3 = (int)(math.ceil(distance3 / spacing))

# vector = vector.normalize() * spacing
X = (int)(deltaX/distance * spacing) #distance in x or y divided by distance between points * space
Y = (int)(deltaY/distance * spacing)
XX = (int)(deltaXX/distance2 * spacing)
YY = (int)(deltaYY/distance2 * spacing)
XXX = (int)(deltaXXX/distance3 * spacing)
YYY = (int)(deltaYYY/distance3 * spacing)

length = 0 #length

for i in range(0, num_points_that_fit): #point1-2
    array[0][i] = (p1.x + X * i) #x compenent of point to graph
    array[1][i] = (p1.y + Y * i) #y component 


for i in range(0, num_points_that_fit2): #point2-3
    array[0][num_points_that_fit + i] = (p2.x + XX * i)
    array[1][num_points_that_fit + i] = (p2.y + YY * i)

for i in range(0, num_points_that_fit3): #point3-4
    array[0][num_points_that_fit2 + num_points_that_fit + i] = (p3.x + XXX * i)
    array[1][num_points_that_fit2 + num_points_that_fit + i] = (p3.y + YYY * i)

#graph
fig, ax = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)
fig2, ax2 = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)
fig3, ax3 = plt.subplots()


# vector = end_point - start_point
#print(num_points_that_fit2+num_points_that_fit)

ax.scatter(array[0], array[1]) #path 
array = smoothing(array, .7, .3, 0.01, num_points_that_fit3 + num_points_that_fit2 + num_points_that_fit) #the good shit
ax2.scatter(array[0], array[1]) #path on second graph

#graphing circles
distance = [0] * len(array[0])
for k in range (1, len(distance)):
    if(array[0][k] == 0): break
    last = length
    length += distanceForm(array[0][k-1], array[1][k-1], array[0][k], array[1][k]) #distance between each point on path
    distance[k] = distance[k-1] + distanceForm((int)(array[0][k-1]), (int)(array[1][k-1]), (int)(array[0][k]), (int)(array[1][k])) #last distance + new length
    if(k == len(distance)-1):
         break
    x1 = array[0][k-1]+0.00001 #past, present, future points
    x2 = array[0][k]
    x3 = array[0][k+1]
    y1 = array[1][k-1]
    y2 = array[1][k]+0.00001
    y3 = array[1][k+1]
    c1 = (x1*x1 + y1*y1 - x2*x2 - y2*y2)/(2*(x1 - x2)) 
    c2 = (y1-y2)/(x1-x2)
    b = (x2*x2 - 2*x2*c1 + y2*y2 - x3*x3 + 2*x3*c1 - y3*y3)/(2*(x3*c2 - y3 + y2 - x2*c2))
    a = c1 - c2*b
    r = math.sqrt((x1-a)**2 + (y1-b)**2)
    array[2][k] = r
    array[3][k] = length
    if(r<10):
        circle1 = plt.Circle((a, b), r, color='r')
        ax2.add_artist(circle1)
    # print("X: " + str(array[0][k] - array[0][k-1]) + "Y: " + str(str(array[1][k] - array[1][k-1])) + "Length: " + str(length - last))
    # print("Curvature: " + str(1/r) + "   Radius: " + str(r))
    # print("Distance of " + str(k) + ": " + str(distance[k]))

#stupid velocity stuff
distance_gr=[]
velocity_gr=[]
acceleration_gr=[]
time_gr=[]
VELOCITY_MIN = 10
VELOCITY_MAX = 40
velocity = VELOCITY_MIN
setPoint = length
distance1 = setPoint/5.0
distance2 = 3.0*setPoint/5.0+distance1
distance3 = setPoint/5.0+distance2
time1=(2*distance1)/(VELOCITY_MAX+VELOCITY_MIN)
time2=(2*(distance2-distance1))/(VELOCITY_MAX*2)
time3=(2*(distance3-distance2))/(VELOCITY_MAX+VELOCITY_MIN)
time_total=time1+time2+time3
acceleration = (VELOCITY_MAX-VELOCITY_MIN)/time1

# print("total: " + str(setPoint) + " 1: " + str(distance1) + " 2: " + str(distance2) + " 3: " + str(distance3))
# print(" T1: " , time1 , " T2: " , time2 , " T3: " , time3)

lastT = 0
t1 = time.time()
position = 0
aT = 0
i = 0
k = 3
j = 1

while(position < setPoint):
    lastT = t1
    t1 = time.time()
    t = (t1 - lastT)
    aT += t
    i += 1
    if(position > array[3][j]):
        j = j+1

    v = array[2][j]
    error = setPoint-position;

    if(position <= distance1):
        position += min(velocity, k*v)*t
        velocity += acceleration*t
    elif(position <= distance2):
        velocity = VELOCITY_MAX
        position += min(velocity*t, k*v)
    elif(error < 0):
        velocity = -VELOCITY_MIN
    else:
        if(velocity<VELOCITY_MIN):
            velocity = VELOCITY_MIN
            position += min(veloctity ,k*v)*t
        else:
            position += min(velocity, k*v)*t
            velocity -= (acceleration * t)
    if(i%10000 == 0):
        distance_gr.append(position)
        velocity_gr.append(min(velocity, k*v))
        acceleration_gr.append(acceleration)
        time_gr.append(aT)
print(array)
plt.subplot(3,1,1)
plt.plot(time_gr,distance_gr)
plt.subplot(3,1,2)
plt.plot(time_gr,velocity_gr)
plt.subplot(3,1,3)
plt.plot(time_gr,acceleration_gr)


# Scatter plot

# fig4, axes = plt.subplots()
fig4 = plt.figure(figsize = (5,5))
axes = fig4.add_subplot(111)
axes.scatter(time_gr, distance_gr)

'''fig5 = plt.figure(figsize = (5,5))
axes1 = fig4.add_subplot(111)
axes1.scatter(time_gr, velocity_gr)'''

# axes.scatter(Acc_11, Acc_12)

axes.set_xlim(min(time_gr), max(time_gr))
axes.set_ylim(min(distance_gr), max(distance_gr))
point, = axes.plot([time_gr[0]],[distance_gr[0]], 'go')

def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    return point

def frames():
    for acc_11_pos, acc_12_pos in zip(time_gr, distance_gr):
        yield acc_11_pos, acc_12_pos

ani = FuncAnimation(fig4, ani, frames=frames, interval=1)

plt.show()