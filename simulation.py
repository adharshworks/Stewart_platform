import numpy as np

from kinematics import inverse_kinematics
from jacobian import compute_jacobian
from metric import (
    actuator_velocity,
    actuator_acceleration,
    actuator_stroke,
    manipulability,
    condition_number
)


def run_simulation(robot, trajectory, time):

    length_history = []
    manip_history = []
    condition_history = []

    for i, pose in enumerate(trajectory):

        lengths, leg_vectors, platform_world = inverse_kinematics(
            robot,
            pose
        )

        length_history.append(lengths)

        J = compute_jacobian(
            robot,
            pose,
            platform_world,
            leg_vectors,
            lengths
        )

        # Print diagnostics only for the first pose
        if i == 0:

            print("\n========== Jacobian Diagnostics ==========\n")

            print("Pose:")
            print(pose)

            print("\nJacobian:")
            print(np.round(J, 3))

            print("\nRank:")
            print(np.linalg.matrix_rank(J))

            print("\nDeterminant:")
            print(np.linalg.det(J))

            print("\nCondition Number:")
            print(np.linalg.cond(J))

            print("\nSingular Values:")
            print(np.linalg.svd(J, compute_uv=False))

        manip_history.append(
            manipulability(J)
        )

        condition_history.append(
            condition_number(J)
        )

    # Convert lists to arrays
    length_history = np.array(length_history)
    manip_history = np.array(manip_history)
    condition_history = np.array(condition_history)

    # Compute actuator metrics
    velocity = actuator_velocity(
        length_history,
        time
    )

    acceleration = actuator_acceleration(
        velocity,
        time
    )

    stroke = actuator_stroke(
        length_history
    )

    return {
        "lengths": length_history,
        "velocity": velocity,
        "acceleration": acceleration,
        "stroke": stroke,
        "manipulability": manip_history,
        "condition_number": condition_history
    }