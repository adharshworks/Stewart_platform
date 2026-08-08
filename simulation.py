import numpy as np

from kinematics import inverse_kinematics
from metric import(actuator_acceleration,actuator_stroke,actuator_velocity,manipulability,condition_number)
from jacobian import compute_jacobian


def run_simulation(robot,trajectory,time):
    length_history=[]
    manip_history=[]
    condition_history=[]
    for pose in trajectory:
        lengths,leg_vectors,platform_world=inverse_kinematics(robot,pose)
        length_history.append(lengths)
    

        J=compute_jacobian(robot,pose,platform_world,leg_vectors,lengths)
        manip_history.append(manipulability(J))
        condition_history.append(condition_number(J))
    


    length_history=np.array(length_history)
    velocity=actuator_velocity(length_history,time)
    acceleration=actuator_acceleration(velocity,time)
    stroke=actuator_stroke(length_history)
    manip_history=np.array(manip_history)
    condition_history=np.array(condition_history)
    return {"lengths":length_history,"velocity":velocity,"acceleration":acceleration,"stroke":stroke,"manipulability": manip_history,
    "condition_number": condition_history}

