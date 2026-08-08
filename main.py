from geometry import StewartPlatform
from trajectory import straight_line,cubic,bezier
from simulation import run_simulation
from visualize import animate
from plots import print_results, plot_results,plot_scalar

robot = StewartPlatform()

start = [0,0,robot.height,0,0,0]

end = [50,30,robot.height,30,60,10]

trajectory, time = bezier(
    start,
    end,
    duration=1.0,
    num_points=100,
    height=-50
)

results = run_simulation(
    robot,
    trajectory,
    time
)

print_results(
    trajectory,
    results["lengths"],
    results["velocity"],
    results["acceleration"],
    results["stroke"],
    results["manipulability"],
    results["condition_number"] 

)

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
    "w"
)

plot_scalar(
    time,
    results["condition_number"],
    "Condition Number",
    "Condition Number"
)
animate(
    robot,
    trajectory
)