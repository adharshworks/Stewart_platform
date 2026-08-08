from pathlib import Path
import matplotlib.pyplot as plt 
import pandas as pd

# Folder where analysis.py is located
BASE = Path(__file__).resolve().parent

straight = pd.read_csv(BASE / "straightline.csv")
cubic = pd.read_csv(BASE / "cubic.csv")
bezier = pd.read_csv(BASE / "bezier.csv")

def summarize(df):

    summary = {}

    summary["Mean Manipulability"] = df["Manipulability"].mean()
    summary["Min Manipulability"] = df["Manipulability"].min()

    summary["Mean Condition"] = df["ConditionNumber"].mean()
    summary["Max Condition"] = df["ConditionNumber"].max()

    summary["Max Velocity"] = (
        df.filter(regex="^V")
        .abs()
        .max()
        .max()
    )

    summary["RMS Velocity"] = (
        (df.filter(regex="^V")**2)
        .mean()
        .mean()**0.5
    )

    summary["Max Acceleration"] = (
        df.filter(regex="^A")
        .abs()
        .max()
        .max()
    )

    summary["RMS Acceleration"] = (
        (df.filter(regex="^A")**2)
        .mean()
        .mean()**0.5
    )

    summary["Max Stroke"] = (
        df.filter(regex="^L")
        .max()
        -
        df.filter(regex="^L")
        .min()
    ).max()

    return summary

# =====================================================
# Build Comparison Table
# =====================================================

comparison = pd.DataFrame({

    "Straight" : summarize(straight),

    "Cubic" : summarize(cubic),

    "Bezier" : summarize(bezier)

})

print("\n")
print("="*70)
print("Trajectory Comparison")
print("="*70)
print(comparison)
print("="*70)

comparison.to_csv("comparison.csv")

# =====================================================
# Overlay Plot Function
# =====================================================

def overlay(column, ylabel):

    plt.figure(figsize=(9,5))

    plt.plot(
        straight["Time"],
        straight[column],
        label="Straight",
        linewidth=2
    )

    plt.plot(
        cubic["Time"],
        cubic[column],
        label="Cubic",
        linewidth=2
    )

    plt.plot(
        bezier["Time"],
        bezier[column],
        label="Bezier",
        linewidth=2
    )

    plt.title(ylabel)

    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)

    plt.grid(True)
    plt.legend()

# =====================================================
# Overlay Plots
# =====================================================

overlay(
    "Manipulability",
    "Manipulability"
)

overlay(
    "ConditionNumber",
    "Condition Number"
)

plt.show()