import numpy as np

def straight_line(start_pose,end_pose,duration=1.0,num_points=100):
    start_pose=np.asarray(start_pose,dtype=float)
    end_pose=np.asarray(end_pose,dtype=float)

    trajectory=np.linspace(start_pose,end_pose,num_points)
    time=np.linspace(0,duration,num_points)
    return trajectory,time
