import pandas as pd


def export_results(filename, time, results):

    data = {
        "Time": time,
        "Manipulability": results["manipulability"],
        "ConditionNumber": results["condition_number"]
    }

    # Lengths
    for i in range(6):
        data[f"L{i+1}"] = results["lengths"][:, i]

    # Velocities
    for i in range(6):
        data[f"V{i+1}"] = results["velocity"][:, i]

    # Accelerations
    for i in range(6):
        data[f"A{i+1}"] = results["acceleration"][:, i]

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print(f"\nResults saved to {filename}")