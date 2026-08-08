import matplotlib.pyplot as plt
import numpy as np


def plot_metric(time, data, title, ylabel):

    plt.figure(figsize=(10,6))

    for i in range(data.shape[1]):

        plt.plot(
            time,
            data[:, i],
            label=f"Leg {i+1}"
        )

    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()


def plot_results(time,
                 length_history,
                 velocity,
                 acceleration):

    plot_metric(
        time,
        length_history,
        "Actuator Lengths",
        "Length (mm)"
    )

    plot_metric(
        time,
        velocity,
        "Actuator Velocities",
        "Velocity (mm/s)"
    )

    plot_metric(
        time,
        acceleration,
        "Actuator Accelerations",
        "Acceleration (mm/s²)"
    )

    plt.show()


def print_results(trajectory,
                  length_history,
                  velocity,
                  acceleration,
                  stroke,
                  manipulability,
                  condition_number):

    print("\n========== Simulation Results ==========\n")

    print(f"Trajectory Shape      : {trajectory.shape}")
    print(f"Length History Shape  : {length_history.shape}")
    print(f"Velocity Shape        : {velocity.shape}")
    print(f"Acceleration Shape    : {acceleration.shape}")

    print("\nStroke (mm)")
    print(np.round(stroke,3))

    print("\nMaximum Velocity (mm/s)")
    print(np.round(np.max(np.abs(velocity),axis=0),3))

    print("\nMaximum Acceleration (mm/s²)")
    print(np.round(np.max(np.abs(acceleration),axis=0),3))
def plot_scalar(time, data, title, ylabel):

    plt.figure(figsize=(10,6))

    plt.plot(time, data, linewidth=2)

    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)

    plt.grid(True)
    plt.tight_layout()

    plt.show()
def plot_overlay(time,
                 data1,
                 data2,
                 data3,
                 label1,
                 label2,
                 label3,
                 title,
                 ylabel):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,6))

    plt.plot(time, data1, linewidth=2, label=label1)
    plt.plot(time, data2, linewidth=2, label=label2)
    plt.plot(time, data3, linewidth=2, label=label3)

    plt.title(title)

    plt.xlabel("Time (s)")

    plt.ylabel(ylabel)

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()