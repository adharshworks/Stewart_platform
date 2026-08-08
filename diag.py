import numpy as np
from kinematics import inverse_kinematics
from jacobian import compute_jacobian


def check_jacobian(robot, pose):

    lengths, leg_vectors, platform_world = inverse_kinematics(robot, pose)

    J = compute_jacobian(
        robot,
        pose,
        platform_world,
        leg_vectors,
        lengths
    )

    print("\n========== Jacobian Diagnostics ==========\n")

    print("Pose:")
    print(pose)

    print("\nRank:", np.linalg.matrix_rank(J))
    print("Determinant:", np.linalg.det(J))
    print("Condition Number:", np.linalg.cond(J))
    print("Singular Values:")
    print(np.linalg.svd(J, compute_uv=False))