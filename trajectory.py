import numpy as np

def straight_line(start_pose,end_pose,duration=1.0,num_points=100):
    start_pose=np.asarray(start_pose,dtype=float)
    end_pose=np.asarray(end_pose,dtype=float)

    trajectory=np.linspace(start_pose,end_pose,num_points)
    time=np.linspace(0,duration,num_points)
    return trajectory,time

def cubic(start_pose,end_pose,duration=1.0,num_points=100):
    start_pose=np.asarray(start_pose,dtype=float)
    end_pose=np.asarray(end_pose,dtype=float)
    time=np.linspace(0,duration,num_points)
    u=time/duration
    s=3*u**2-2*u**3
    trajectory=np.zeros((num_points,6))
    for i in range(num_points):
        trajectory[i]=start_pose+s[i]*(end_pose-start_pose)
    return trajectory,time

def bezier(start_pose,end_pose,duration=1.0,num_points=100,height=50):
    start_pose=np.asarray(start_pose,dtype=float)
    end_pose=np.asarray(end_pose,dtype=float)
    time=np.linspace(0,duration,num_points)

    trajectory=np.zeros((num_points,6))
    #posn
    P0 = start_pose[:3]
    P2 = end_pose[:3]

    # Control point
    P1 = (P0 + P2) / 2
    P1[2] += height

    #orientation
    R0 = start_pose[3:]
    R2 = end_pose[3:]

    for i, u in enumerate(time / duration):

        # Quadratic Bezier Position

        position = (
            (1 - u) ** 2 * P0 +
            2 * (1 - u) * u * P1 +
            u ** 2 * P2
        )
        #linear orientation
        orientation = R0 + u * (R2 - R0)

        trajectory[i, :3] = position
        trajectory[i, 3:] = orientation
    return trajectory,time
