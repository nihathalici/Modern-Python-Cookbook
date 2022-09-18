# Exer-03-Forcing-keyword-only-arguments-with-the-*-separator

import pathlib
import csv

def Twc(T, V):
    return 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16

def wind_chill(start_T, stop_T, step_T, start_V, stop_V, step_V, path):
    """Wind Chill Table."""
    with path.open('w', newline='') as target:
        writer = csv.writer(target)
        heading = [None] + list(range(start_T, stop_T, step_T))
        writer.writerow(heading)
        for V in range(start_V, stop_V, step_V):
            row = [V] + [Twc(T, V) for T in range(start_T, stop_T, step_T)]
            writer.writerow(row)
