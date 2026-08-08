import numpy as np

def actuator_velocity(length_history,time):
    velocity=np.gradient(length_history,time,axis=0)
    return velocity
def actuator_acceleration(velocity,time):
    acceleration=np.gradient(velocity,time,axis=0)
    return acceleration
def actuator_stroke(length_history):
    stroke=np.max(length_history,axis=0)-np.min(length_history,axis=0)
    return stroke

def manipulability(J):
    return np.sqrt(
        np.linalg.det(J@J.T)
    )

def condition_number(J):
    return np.linalg.cond(J)

