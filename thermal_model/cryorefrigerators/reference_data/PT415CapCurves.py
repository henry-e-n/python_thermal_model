import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


# Data for PT415 Cryorefrigerator Capacity Curves

# Import the csv data
data = np.genfromtxt('PT415_CapCurveData.csv', delimiter=',')
# Convert the data that is a list of tuples into an array
data_array = np.array([list(row) for row in data])
first_stage_temp = data_array[:, 0]
second_stage_temp = data_array[:, 1]
# The data columns are First Stage Temp (K), Second Stage Temp (K)

big_data_array = np.empty((0,4))
# Split the data into 6 curves based on the cooling power levels
first_stage_load = [0, 0.5, 1.35, 5, 8, 10] # W

# Each data point corresponds to a second stage cooling power level
second_stage_load = [0, 25, 50, 75, 100] # W


index = 0
for i in range(len(first_stage_load)):
    for j in range(len(second_stage_load)):
        i_first_stage_temp = first_stage_temp[index]
        i_second_stage_temp = second_stage_temp[index]
        i_first_stage_load = first_stage_load[i]
        i_second_stage_load = second_stage_load[j]
        # print(i_first_stage_temp, i_second_stage_temp, i_first_stage_load, i_second_stage_load)
        big_data_array = np.vstack([big_data_array, [i_first_stage_temp, i_second_stage_temp, i_first_stage_load, i_second_stage_load]])
        index += 1

min_x = np.min(big_data_array[:,0])
max_x = np.max(big_data_array[:,0])
min_y = np.min(big_data_array[:,1])
max_y = np.max(big_data_array[:,1])

grid_x, grid_y = np.meshgrid(np.linspace(min_x, max_x, 5), np.linspace(min_y, max_y, 6))

grid_z0 = griddata((big_data_array[:,0], big_data_array[:,1]), big_data_array[:,2], (grid_x, grid_y), method='nearest')
grid_z1 = griddata((big_data_array[:,0], big_data_array[:,1]), big_data_array[:,3], (grid_x, grid_y), method='nearest')

plt.imshow(grid_z0.T, extent=(min_x,max_x,min_y,max_y), origin='lower')
plt.scatter(big_data_array[:,0], big_data_array[:,1], c='r')
plt.show()
plt.imshow(grid_z1.T, extent=(min_x,max_x,min_y,max_y), origin='lower')
plt.scatter(big_data_array[:,0], big_data_array[:,1], c='r')
plt.show()

# Now use the two grids to estimate the x and y values for given z0 and z1 values
def estimate_temps(first_stage_load, second_stage_load):
    # Find the closest points in the grid
    dist = (grid_z0 - first_stage_load)**2 + (grid_z1 - second_stage_load)**2
    min_index = np.unravel_index(np.argmin(dist, axis=None), dist.shape)
    est_first_stage_temp = grid_x[min_index]
    est_second_stage_temp = grid_y[min_index]
    return est_first_stage_temp, est_second_stage_temp

# Example usage
first_stage_load_input = 5 # W
second_stage_load_input = 50 # W
est_first_stage_temp, est_second_stage_temp = estimate_temps(first_stage_load_input, second_stage_load_input)
print(f"Estimated First Stage Temp: {est_first_stage_temp} K")
print(f"Estimated Second Stage Temp: {est_second_stage_temp} K")