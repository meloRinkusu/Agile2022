# 1. Compute the distance between 2 points by using their coordinates (and an altitud parameter in feet if implemented). Returns the distance in kilometers, meters and feet.
# 2. Check the autonomy by using an autonomy value set by the user. Returns True if the autonomy value is superior to the distance between the 2 points, False otherwise.

# Caution for 1. : the coordinates are decimal degrees
# Caution for 2. : the autonomy value set by the user is a distance in kiliometers

import numpy as np

# Compute the distance between 2 points
def distance(long_dep, long_arr, lat_dep, lat_arr, alt):
	pi = np.pi
	# feet in kilometer
	ft_const = 0.3048
	# Conversion of coordinates from degree to radian
	long_dep = long_dep * pi / 180
	long_arr = long_arr * pi / 180
	lat_dep = lat_dep * pi / 180
	lat_arr = lat_arr * pi / 180
	# Computing global radius of Earth from the equatorial and the polar radius
	R_eq_earth = 6378.1370
	R_pol_earth = 6356.7523	
	R_approx = (2 * R_eq_earth + R_pol_earth) / 3
	# Default value of the altitude for now	
	alt = 0
	# Computing the difference between the longitude of departure and arrival, then computing the cosine of this difference
	diff_long = long_arr - long_dep
	cos_diff_long = np.cos(diff_long)
	# Computing the sine and cosine of the latitude of departure and arrival
	cos_lat_dep = np.cos(lat_dep)
	cos_lat_arr = np.cos(lat_arr)
	sin_lat_dep = np.sin(lat_dep)
	sin_lat_arr = np.sin(lat_arr)
	# Flight path total angle 
	total_angle = np.arccos(sin_lat_arr * sin_lat_dep + cos_lat_arr * cos_lat_dep * cos_diff_long)
	total_angle_deg = total_angle * 180 / pi
	# Computing the distance in kilometer, meter and feet
	total_distance = total_angle * (R_approx + alt * ft_const)
	total_distance_m = total_distance * 1000
	total_distance_ft = total_distance_m / ft_const
	return [total_distance, total_distance_m, total_distance_ft]

# Autonomy check
def autonomy(total_distance, user_autonomy):
	if total_distance < user_autonomy:
		autonomy_check = True
	else:
		autonomy_check = False
	return autonomy_check

