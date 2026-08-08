import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def animate(robot, trajectory):
    """
    Animate the Stewart platform.

    Parameters
    ----------
    robot : StewartPlatform

    trajectory : ndarray (N,6)
    """

    plt.ion()

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    for pose in trajectory:

        ax.cla()

        # -----------------------------
        # Current platform position
        # -----------------------------

        from kinematics import transform_platform

        platform = transform_platform(robot, pose)

        # -----------------------------
        # Base polygon
        # -----------------------------

        B = np.vstack((robot.B, robot.B[0]))

        ax.plot(
            B[:, 0],
            B[:, 1],
            B[:, 2],
            'bo-',
            linewidth=2,
            label="Base"
        )

        # -----------------------------
        # Platform polygon
        # -----------------------------

        P = np.vstack((platform, platform[0]))

        ax.plot(
            P[:, 0],
            P[:, 1],
            P[:, 2],
            'ro-',
            linewidth=2,
            label="Platform"
        )

        # -----------------------------
        # Legs
        # -----------------------------

        for i in range(robot.num_legs):

            ax.plot(
                [robot.B[i,0], platform[i,0]],
                [robot.B[i,1], platform[i,1]],
                [robot.B[i,2], platform[i,2]],
                'k'
            )

        # -----------------------------
        # Plot settings
        # -----------------------------

        ax.set_xlim(-300,300)
        ax.set_ylim(-300,300)
        ax.set_zlim(0,700)

        ax.set_xlabel("X (mm)")
        ax.set_ylabel("Y (mm)")
        ax.set_zlabel("Z (mm)")

        ax.set_title("Stewart Platform Animation")

        ax.set_box_aspect([1,1,1])

        plt.pause(0.03)

    plt.ioff()
    plt.show()