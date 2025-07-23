import os, sys
from gui_init import define_CMR_path

abspath = os.path.abspath(__file__)
file_path = os.path.dirname(abspath)
package_path = os.path.dirname(file_path)

path_to_cmr_definition = os.path.join(file_path, "cmr_path.txt")
if not os.path.exists(path_to_cmr_definition):
    print("cmr_path.txt not found. Please define the path to CMR.")
    path_to_cmr = define_CMR_path()
else:
    path_to_cmr = path_to_cmr_definition

with open(path_to_cmr, "r") as f:
    cmr_path = f.read().strip()

path_to_mat_lib = os.path.join(cmr_path, "thermal_conductivity", "lib")

if cmr_path == "":
    print("Please set the correct local path to the Cryogenic Material Properties repository in global_var.py")
    print("Exiting...")
    sys.exit(1)

if not os.path.exists(cmr_path):
    print("ERROR : path to Cryogenics Material Properties repository is not found.")
    print("Exiting...")
    define_CMR_path()
    sys.exit(1)