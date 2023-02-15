# Importing sin() and cos() functions from math module
from math import sin, cos, pi

# Defining constant g
g = 9.81

def deg2rad(a):
	"""
	Converts degrees to radians
	:param a: Angle in degrees
	:return: Angle in radians
	"""
	return a / 180 * pi

def height(v, a, t):
	"""
	Calculates and returns the height at a given time
	:param v: Velocity in meters per second
	:param a: Angle in degrees
	:param t: Time in seconds
	:return: Height in meters
	"""
	# Extract y component of the combined velocity
	Vy = v * sin(deg2rad(a))
	# Using the formula to calculate height
	return Vy * t - g * t ** 2 / 2

def horizontal(v, a, t):
	"""
	Calculates and returns the horizontal distance at a given time
	:param v: Velocity in meters per second
	:param a: Angle in degrees
	:param t: Time in seconds
	:return: Horizontal distance in meters
	"""
	# Extract x component of the combined velocity
	Vx = v * cos(deg2rad(a))
	# Using the formula to calculate horizontal distance
	return Vx * t

def print_table(v, a):
	"""
	Prints the horizontal and vertical distance at any point in time
	:param v: Initial velocity in meters per second
	:param a: Throwing angle in degrees
	"""

	# Initialize values
	step = 0.1
	cur_time = 0
	height_t = 0

	# Print table
	while height_t >= 0:
		cur_time += step
		height_t = height(v, a, cur_time)
		# Print one row of the table
		print("Time: %.1f....S=%.2f H=%.2f" % (cur_time, horizontal(v, a, cur_time), height_t))
	print('Fallen!')

def main():
	velocity = 0
	angle = 0

	# First iteration's only job is to get user input
	first_iter = True
	while 0 <= velocity <= 100 and 0 <= angle <= 90:

		# Starting from second iteration, print time/distance table
		if not first_iter:
			print_table(velocity, angle)

		# Get input
		velocity = float(input('Enter speed 0-100 (m/s): '))
		# Validate input
		if 0 <= velocity <= 100:
			# Get input
			angle = float(input('Enter angle 0-90 (degrees): '))

		first_iter = False
	print('Finish')

main()