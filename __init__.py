import os
import sys

module_path = [os.path.dirname(os.path.abspath(__file__))]
for path in module_path:
    if path not in sys.path:
        sys.path.append(path)

if __name__ == "__main__":
    print("Welcome to the Thermal Model package...")
    print("This package was created by Henry Nachman for use by the BLAST Collaboration")
    from setup import VERSION
    print(f"Current version is v{VERSION}")

    print("""Summary__________
    The Thermal Model package is designed to enable the full suite of calculations and modeling described in the `Forecasting Pipeline' notes. While these codes have existed in some capacity for a while, this is the first time they have been integrated into a single package for simplified use. A summary of the modeling capabilities is listed below.

    Thermal model - (author: Henry Nachman & Nicholas Galitzki and others): enables accurate estimation of thermal loading and cryogenic performance based on component geometry and material. Can be coupled to the filter transfer calculation to incorporate the thermal load from the optical stack.
     """)