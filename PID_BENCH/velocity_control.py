import matplotlib.pyplot as plt
import math


velocity_max = 2000 #32.4
velocity_min = 4
position = 0
velocity=velocity_min
time=0
distance_gr=[]
velocity_gr=[]
acceleration_gr=[]
time_gr=[]
temp = 0
setpoint_in = 100*4096/(6*3.1415)
#setpoint_me= setpoint_in*.0254


d1 =1/5
d2 =1/5

distance1 = setpoint_in*d1
distance2 = setpoint_in*3.0/5.0+distance1
distance3 = setpoint_in*d2+distance2

time1=(2*distance1)/(velocity_min+velocity_max)
time2=(2*(distance2-distance1))/(velocity_max+velocity_max)
time3=(2*distance1)/(velocity_min+velocity_max)
time_total=time1+time2+time3
acceleration=velocity_max/time1
'''
acceleration=(velocity_max*velocity_max)/(2*distance1)
time1=(velocity_max)/(acceleration)
time2=(distance2)/(velocity_max)
time3=(velocity_max)/(acceleration)
time_total=time1+time2+time3
#acceleration=velocity_max/(time1)
'''

while(position<setpoint_in):
	if(position<distance1):
		position+=velocity
		velocity+=acceleration
		print("pos:",position)
		print("vel:",velocity)
	elif(position+velocity_max<distance2):
		position+=velocity
		temp = velocity
	else:
		if(velocity<velocity_min):
			position+=velocity_min
		else:
			position+=velocity
			velocity-=acceleration
	time+=1
	distance_gr.append(position)
	velocity_gr.append(velocity)
	acceleration_gr.append(acceleration)
	time_gr.append(time)

plt.subplot(3,1,1)
plt.plot(time_gr,distance_gr)
plt.subplot(3,1,2)
plt.plot(time_gr,velocity_gr)
plt.subplot(3,1,3)
plt.plot(time_gr,acceleration_gr)

print(temp," velocity_achieved")
print(setpoint_in/time," velocity_avg")
print(acceleration,"acceleration")
print(time_total,"time_total")
plt.show()