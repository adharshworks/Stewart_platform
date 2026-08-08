import numpy as np

def rotation_matrix(roll,pitch,yaw):
    #roll abt x axis
    #yaw abt z
    #pitch abt y
    Rx=np.array([[1,0,0],
        [0,np.cos(roll),-np.sin(roll)],
        [0,np.sin(roll),np.cos(roll)]
                 ])
    Ry = np.array([
        [ np.cos(pitch), 0, np.sin(pitch)],
        [0,1,0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    Rz = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw),  np.cos(yaw), 0],
        [0,            0,           1]
    ])

    return Rz @ Ry @Rx

def transform_platform(robot,pose):
    #pose na array [x,y,z,r,p,y]
    x,y,z,roll,pitch,yaw=pose
    roll=np.deg2rad(roll)
    pitch=np.deg2rad(pitch)
    yaw=np.deg2rad(yaw)

    R=rotation_matrix(roll,pitch,yaw)

    t=np.array([x,y,z])

    platform_world=(R @ robot.P.T).T
    platform_world+=t

    return platform_world



def inverse_kinematics(robot,pose):
    platform_world=transform_platform(robot,pose)
    base_points=robot.B[robot.leg_pairing]
    leg_vectors=platform_world-base_points
    lengths=np.linalg.norm(leg_vectors,axis=1)
   
    return(lengths,leg_vectors,platform_world)