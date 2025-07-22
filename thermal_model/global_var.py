import os, sys

abspath = os.path.abspath(__file__)
file_path = os.path.dirname(abspath)
package_path = os.path.dirname(file_path)
cmr_path = f"C:{os.sep}Users{os.sep}hen367{os.sep}OneDrive - The University of Texas at Austin{os.sep}01_RESEARCH{os.sep}05_CMBS4{os.sep}Cryogenic_Material_Properties" # os.path.join(package_path, "Cryogenic_Material_Properties")
path_to_mat_lib = os.path.join(cmr_path, "thermal_conductivity", "lib")

if cmr_path == "":
    print("Please set the correct local path to the Cryogenic Material Properties repository in global_var.py")
    print("Exiting...")
    sys.exit(1)

if not os.path.exists(cmr_path):
    print("ERROR : path to Cryogenics Material Properties repository is not found.")
    print("Exiting...")
    sys.exit(1)