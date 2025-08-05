# Python Thermal Model

A Python package to aid in constructing thermal models of cryogenic systems. This code was developed by Henry Nachman based on work by Nicholas Galitzki and others.

In its current form, the package is not Debian based. This means that installing via regular pip may throw an error as it is not recommended to install a non-Debian package system-wide as it may interfere with other installs and the OS. This is remedied by installing in a conda environment or virtual environment.

To install in a conda environment you must first install pip within that conda environment.
```
conda install pip
```
Then, install the package using.
```
pip install git+https://github.com/henry-e-n/python_thermal_model.git
```

To run the streamlit gui:
```
from thermal_model.gui_init import init_gui
init_gui()
```

Explore the wiki:
https://github.com/henry-e-n/python_thermal_model/wiki/0.-Thermal-Model-Wiki