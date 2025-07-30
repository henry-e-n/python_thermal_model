import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px

from global_var import cmr_path, path_to_mat_lib

for path in [cmr_path]:
    if path not in sys.path:
        sys.path.append(path)

from thermal_conductivity.tc_tools import *
from thermal_conductivity.tc_utils import *
from thermal_conductivity.fit_types import *

#%% Plot integral
def plot_integral(selected_component, stage):
    """
    Description:
        This function plots the thermal conductivity of a selected component over the temperature range defined by the stage.

    Args:
        selected_component : The component whose thermal conductivity is to be plotted.
        stage              : The stage object containing temperature information.

    Returns:
        fig, ax : The figure and axis objects for the plot.
    """

    all_files       = os.listdir(cmr_path)
    T_low, T_high = [stage.low_temp, stage.high_temp]
    # Plotting
    fill_between_range = np.arange(T_low, T_high)
    
    fig, ax = plt.subplots()

    if not selected_component.properties["Interpolate"]:
        exist_files     = [file for file in all_files if file.startswith("tc_fullrepo")]
        tc_file_date    = exist_files[0][-12:-4]

        material_of_interest = selected_component.properties["Material"]
        TCdata = np.loadtxt(os.path.join(cmr_path, "thermal_conductivity", "lib", material_of_interest, "all_fits.csv"), dtype=str, delimiter=',') # imports compilation file csv
        mat_parameters = get_parameters(TCdata, selected_component.properties["Fit Choice"])
        func_type = get_func_type(mat_parameters["fit_type"])
        fit_range = mat_parameters["fit_range"]

        # Let's make our plotting range the listed fit range
        T_range = np.linspace(fit_range[0], fit_range[1], 1000)

        # Now let's use the fit to get the thermal conductivity values over the range
        # Luckily, every function type is defined in such a way to readily accept the parameter dictionary as it was defined above
        y_vals = func_type(T_range, mat_parameters)
        ax.fill_between(fill_between_range, np.zeros(len(fill_between_range)), func_type(fill_between_range, mat_parameters),
                    hatch="////", alpha = 0.5, edgecolor = 'b', facecolor="w",
                    label="Integration Area")
    else:
        interp_func = get_interpolation(os.path.join(path_to_mat_lib, selected_component.properties["Material"]))
        T_range = np.linspace(interp_func.x[0], interp_func.x[-1], 1000)
        y_vals = interp_func(T_range)

        ax.fill_between(fill_between_range, np.zeros(len(fill_between_range)), interp_func(fill_between_range),
                    hatch="////", alpha = 0.5, edgecolor = 'b', facecolor="w",
                    label="Integration Area")

    ax.plot(T_range, y_vals, color="b")
    
    ax.semilogy()
    ax.semilogx()
    ax.legend()
    ax.set_title(f"Plot of  {selected_component.name}")
    ax.set_xlabel("T [K]")
    ax.set_ylabel("Thermal Conductivity : k [W/m/K]")
    return fig, ax

#%% Plot Pie Chart
def plot_pie_chart(stage, streamlit=True):
    
    # Prepare data for the pie chart
    try:
        data = {
            "Component": [component.name for component in stage.components],
            "Power (W)": [
                float(component.properties.get("Power Total (W)", 0)) for component in stage.components
            ],
        }
    except:
        data = {
            "Component": [component for component in stage.components],
            "Power (W)": [
                float(stage.components[component]["Power Total (W)"]) for component in stage.components
            ],
        }

    df = pd.DataFrame(data)
    # Plot the pie chart using Plotly with hover showing power in scientific notation
    fig = px.pie(
        df, 
        names="Component", 
        values="Power (W)", 
        title=f"Power Distribution for {stage.name}", 
        color_discrete_sequence=px.colors.sequential.RdBu,
        hover_data={"Power (W)": ":e"},  # Format hover data in scientific notation
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    if streamlit:
        st.plotly_chart(fig)
    return fig