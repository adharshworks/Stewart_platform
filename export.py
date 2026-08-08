import pandas as pd
from pathlib import Path


def export_results(filename, time, results):

    data = {
        "Time": time,
        "Manipulability": results["manipulability"],
        "ConditionNumber": results["condition_number"]
    }

    # Actuator lengths
    for i in range(6):
        data[f"L{i+1}"] = results["lengths"][:, i]

    # Actuator velocities
    for i in range(6):
        data[f"V{i+1}"] = results["velocity"][:, i]

    # Actuator accelerations
    for i in range(6):
        data[f"A{i+1}"] = results["acceleration"][:, i]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save in the project folder
    output_path = Path(__file__).parent / filename

    df.to_csv(output_path, index=False)

    print(f"\nResults saved to:\n{output_path}")