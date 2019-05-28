import matplotlib.pyplot as plt
import random



setpoint = 100.0
initvalueR=0
initvalueL=0
maxpwr = setpoint/100
if maxpwr>.8:
	maxpwr =.8
kp=.8/setpoint
ki=1/1000000.0
t_error=0
position1 = []
position2=[]
changes = []
R_diff = []
L_diff = []
diff=[]
time = []
time2 = []

a=0

def PID(inputval):
	global t_error
	if(abs(inputval/setpoint) >=.75):
		t_error = t_error+ (setpoint-inputval)
	return kp*(setpoint-inputval)#+ki*t_error
def diff_PID(R,L):
	kp=1
	if(R>L):
		setpoint=R
		init=L	
		return 0,kp*(setpoint-init)
	elif(L>R):
		setpoint=L
		init=R
		return kp*(setpoint-init),0
	else:
		return kp,kp

while(abs((initvalueR+initvalueL)/2-setpoint)>1):
	change=PID(initvalueR)
	diffR,diffL= diff_PID(initvalueR,initvalueL)
	a+=1
	initvalueR+=change+diffR+random.random()
	initvalueL+=change+diffL
	position1.append(initvalueR)
	position2.append(initvalueL)
	L_diff.append(change+diffL)
	R_diff.append(change+diffR)
	diff.append(initvalueR-initvalueL)
	changes.append(change)
	time.append(a)
	time2.append(a*a)

plt.subplot(3,1,1)
plt.plot(time,position1,color="blue")
plt.plot(time,position2,color="red")
plt.subplot(3,1,2)
plt.plot(time,R_diff,color="blue")
plt.plot(time,L_diff,color="red")
plt.subplot(3,1,3)
plt.plot(time,diff)
#plt.plot(time,changes)
plt.show()











