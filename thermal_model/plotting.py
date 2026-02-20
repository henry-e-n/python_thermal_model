import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
from matplotlib.patches import Patch

from global_var import cmr_path, path_to_mat_lib

for path in [cmr_path]:
    if path not in sys.path:
        sys.path.append(path)

# from thermal_conductivity.tc_tools import *
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

    mat = get_material(selected_component.properties["Material"])
    if not selected_component.properties["Interpolate"]:
        fit_obj = get_fit_by_name(selected_component.properties["Material"], selected_component.properties["Fit Choice"])
        fit_obj.plot()
        ax.fill_between(fill_between_range, np.zeros(len(fill_between_range)), fit_obj.function()(fill_between_range, *fit_obj.parameters),
                    hatch="////", alpha = 0.5, edgecolor = 'b', facecolor="w",
                    label="Integration Area")
    else:
        interp_func = mat.interpolate_function
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

def allocation_plot(allocation_dictionary):
    diff_array = []
    for key, value in allocation_dictionary.items():
        diff = value[1] - value[0]
        diff_array.append(diff)
    labels = list(allocation_dictionary.keys())
    x = np.arange(len(labels))
    width = 0.5
    allocation_fig, ax = plt.subplots()
    # plot the positive and negative values in different colors
    colors = ['red' if x < 0 else 'green' for x in diff_array]
    rects1 = ax.bar(x - width/2, diff_array, width, label='Allocation', color=colors)
    # ax.bar_label(rects1, label_type='center', color='white', fontsize=8)
    # for i, (name, height) in enumerate(zip(labels, diff_array)):
    #     print(i, name, height)
    #     ax.text(i, height, f"{name}", ha='right', va='top', color='black', fontsize=8, rotation=90)
    ax.set_ylabel('Power (W)')
    ax.set_title('Allocation vs Predicted Power')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    # Make a custom legend, 
    legend_elements = [Patch(facecolor='green', label='Under-budget'),
                          Patch(facecolor='red', label='Over-budget')]
    ax.legend(handles=legend_elements)
    plt.xticks(rotation=75)
    # plt.tight_layout()
    return allocation_fig, ax    