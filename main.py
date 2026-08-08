import numpy as np
import matplotlib.pyplot as plt
from geometry import StewartPlatform
from kinematics import inverse_kinematics
from trajectory import straight_line
from metric import (actuator_acceleration,actuator_stroke,actuator_velocity)

robot=StewartPlatform()

#start pose
start=[0,0,robot.height,0,0,0]

#end pose
end=[50,30,robot.height,5,3,10]

#Generate trajectory
trajectory,time=straight_line(start,end,duration=1.0,num_points=100)

#IK
length_history=[]
for pose in trajectory:
    lengths, _, _=inverse_kinematics(robot,pose)
    length_history.append(lengths)
length_history=np.array(length_history)

#compute timestep
dt=time[1]-time[0]

#print(length_history)
#####
##########
###########
#Compute metrics
velocity=actuator_velocity(length_history,time)
acceleration=actuator_acceleration(velocity,time)
stroke=actuator_stroke(length_history)

##############################################################
#print results
print('trajector shape')
print(trajectory.shape)
print("length history shape")
print(length_history.shape)
print("Velocity Shape")
print(velocity.shape)
print("Acceleration Shape")
print(acceleration.shape)
print("Stroke (mm)")
print(np.round(stroke, 3))

#############################################################
#plot actuator lengths
plt.figure(figsize=(10,6))

for i in range(robot.num_legs):

    plt.plot(
        time,
        length_history[:, i],
        label=f"Leg {i+1}"
    )

plt.title("Actuator Lengths")

plt.xlabel("Time (s)")

plt.ylabel("Length (mm)")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()

####################################################
#plot velocities
plt.figure(figsize=(10,6))

for i in range(robot.num_legs):

    plt.plot(
        time,
        velocity[:, i],
        label=f"Leg {i+1}"
    )

plt.title("Actuator Velocities")

plt.xlabel("Time (s)")

plt.ylabel("Velocity (mm/s)")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()

# Plot Accelerations
# =====================================================

plt.figure(figsize=(10,6))

for i in range(robot.num_legs):

    plt.plot(
        time,
        acceleration[:, i],
        label=f"Leg {i+1}"
    )

plt.title("Actuator Accelerations")

plt.xlabel("Time (s)")

plt.ylabel("Acceleration (mm/s²)")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()

#robot.print_geometry()