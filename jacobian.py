import numpy as np

#gpt
def compute_jacobian(robot,
                     pose,
                     platform_world,
                     leg_vectors,
                     lengths):
    """
    Compute the Stewart Platform Jacobian.

    Parameters
    ----------
    robot : StewartPlatform

    pose : [x,y,z,roll,pitch,yaw]

    platform_world : (6,3)

    leg_vectors : (6,3)

    lengths : (6,)

    Returns
    -------
    J : (6,6)
    """

    # Platform centre
    center = np.array(pose[:3])

    # Unit vectors along each leg
    unit_vectors = leg_vectors / lengths[:, None]

    # Vectors from platform centre to platform joints
    r = platform_world - center

    # Jacobian
    J = np.zeros((6, 6))
    Lc=robot.platform_radius

    for i in range(robot.num_legs):

        # Translational part
        J[i, :3] = unit_vectors[i]

        # Rotational part
        
        J[i, 3:] = np.cross(
            r[i],
            unit_vectors[i]
        )/Lc

    return J
