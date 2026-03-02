## About
This is an interactive GUI designed to help model the thermal properties of cryogenic systems.
It allows users to add components to cryogenic stages, and visualize the thermal properties of the system.
The development of this tool was done in support of the Balloon-borne Large Aperture Sub-millimeter Telescopes (BLAST) collaboration.
### Features:
- Add and edit components and stages.
- Calculate total thermal power requirements.
- Optimize liquid helium cryogenic stage temperatures (when applicable).
- Calculate liquid helium and balloon specific parameters and/or compare to system allocation requirements.
- Visualize power distribution and temperature variance parameters.

___

## Getting Started:

This section will help guide you through how to make your first thermal model. 

### Adding a Stage
Each `system` must begin with a `stage`. A stage in this context is defined as a group of components that share a temperature level. Each stage has a `Low Temperature` and a `High Temperature`. The low temperature is generally the ideal temperature of that set of components, the high temperature defines the temperature of the environment the stage is launched from.

To add your first stage:
1. Define a name for the `stage`.
2. Choose a `Low Temperature` in K.
3. Choose a `High Temperature` in K.
4. Click the **Add** button.

To add a subsequent stage:
1. Select the `Stage` component type.
2. Follow the above instructions just like you are adding your first stage.

### Adding a Component
Once you have added a `stage`, you can add your first `component`. A component defines the properties of an object that you wish to add to your model. Each component has a number of relevant properties including (but not limited to): name, material, geometry, number.

To add a component:
1. Specify the stage to which the component will be added.
2. Select the type of component from the dropdown.
    - Standard - These components are cylindrically symmetric. Define the geometry with an outer diameter, inner diameter, and length.
    - A/L - These components use a specified A/L (in units of m). This is good for atypical geometries.
    - Coax - These components are designed for coaxial cables with (up to) three different materials for the outer conductor, dielectric, and inner conductor. 
    - Power per Part - These components are a catch-all for components with unknown or complicated geometries, as well as other sources of thermal power that should be accounted for (for example radiation).
3. Choose a name for the component. **NOTE:** Each component name within a given stage must be unique. If a component with that name is already present in that stage, the component will not be added. However, duplicate names can exist if the components are in different stages.
4. Select (or deselect) the `default upper stage`. When selected, the component is added with the same high temperature and low temperature of the stage. If deselected, you will be prompted to select from which stage this component is being launched. This is useful if a component plans to skips a stage. For example, if your wiring will not be thermally connected to every stage.
5. Choose a `Material`. These materials are selected from those available on the Cryogenic Materials Repository.
6. Choose whether to use the `Interpolation`. Each material has an interpolation function that tries to cover the largest possible range of temperatures given the available data and fits for the material. Sometimes, these interpolations have strange behavior, especially if there is little data available for a material. If you do not wish to use the interpolation function, deselect the check box. You will then be prompted to select a fit from the list of available fits for the given material on the Cryogenic Materials Repository. To help you select the best fit for your application, explore the available fits in the <font color="red">Libary</font> tab.

7. Define the geometry of the component (see step 2 for notes on the different types of geometries).
8. Define the number of parts.
9. The 'providing vapor' option can be used if operating a liquid helium cryostat (that cools the warmer stages via vapor pressure).
10. Click the **Add** button.

### Calculating Power
To update the calculated power for each component, and the sum power for each stage, click the big red <font color="red">Calculate Power</font> button. This button should also be pressed after importing a json file to finish properly loading it into the buffer of the gui. The Result Tables tab will remain empty until this button is pressed.

### Optimize
This gui is equipped with a liquid helium optimization function. More information can be found about that function in the `stage_calc.py` file. To run the optimization, choose how many optimization points you want from the slider, then click the <font color="red">Optimize</font> button.

### Saving and Loading from a File
One of the great beauties of this code is the ability to download the model (and results) as a .json file. This allows the model to be easily manipulated or incorporated in other programs or python scripts. 

This is also how you can save your model for later. Once you have added your stages and components, hit the <font color="red">Download JSON</font> button and your File Explorer will open to allow you to specify a save location. To load a saved model, click the <font color="red">Browse files</font> button, select and file, and open. Then you must click the <font color="red">Click to load JSON</font> button, and finally, <font color="red">Calculate Power</font>.

___

For more guidance, please refer to the [documentation](https://github.com/henry-e-n/python_thermal_model/wiki/0.-Thermal-Model-Wiki).

## Creators:
This tool is a culmination of decades of various similar efforts by researchers across experimental cosmology, and other cryogenic experimental fields. 
        The development of this Python-based tool, package, and GUI was led by Henry Nachman at the University of Texas at Austin.

If you have any questions, suggestions, or issues, please feel free to reach out:

Henry Nachman : (henry.nachman@utexas.edu)