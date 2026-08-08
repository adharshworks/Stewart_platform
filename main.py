from geometry import StewartPlatform
from trajectory import straight_line, cubic, bezier
from simulation import run_simulation
from visualize import animate
from plots import print_results, plot_results, plot_scalar
from export import export_results
from diag import check_jacobian


# Create robot
robot = StewartPlatform()

# Start and End Pose
start = [0, 0, robot.height, 0, 0, 0]
end = [50, 30, robot.height, 30, 60, 10]

# ----------------------------------------------------
# Choose ONE trajectory
# ----------------------------------------------------

# trajectory, time = straight_line(
#     start,
#     end,
#     duration=1.0,
#     num_points=100
# )

trajectory, time = cubic(
    start,
    end,
    duration=1.0,
    num_points=100
)

# trajectory, time = bezier(
#     start,
#     end,
#     duration=1.0,
#     num_points=100,
#     height=150
# )

# ----------------------------------------------------
# Run Simulation
# ----------------------------------------------------

results = run_simulation(
    robot,
    trajectory,
    time
)

# ----------------------------------------------------
# Print Results
# ----------------------------------------------------

print_results(
    trajectory,
    results["lengths"],
    results["velocity"],
    results["acceleration"],
    results["stroke"],
    results["manipulability"],
    results["condition_number"]
)

# ----------------------------------------------------
# Plot Results
# ----------------------------------------------------

plot_results(
    time,
    results["lengths"],
    results["velocity"],
    results["acceleration"]
)

plot_scalar(
    time,
    results["manipulability"],
    "Manipulability",
    "Manipulability"
)

plot_scalar(
    time,
    results["condition_number"],
    "Condition Number",
    "Condition Number"
)

# ----------------------------------------------------
# Export CSV
# ----------------------------------------------------

export_results(
    "cubic.csv",
    time,
    results
)

# ----------------------------------------------------
# Animate
# ----------------------------------------------------

animate(
    robot,
    trajectory
)
#check_jacobian(robot, start)