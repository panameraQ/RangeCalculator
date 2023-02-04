import math

# given constants
velocity = 5000 # m/s
angle = 45 # degrees 
air_resistance = 0.2 # N/m/s 
gravitational_acceleration = 9.81 # m/s^2 

# calculate the horizontal component of the velocity 
vx = velocity * math.cos(math.radians(angle)) 
# calculate the vertical component of the velocity 
vy = velocity * math.sin(math.radians(angle)) 
# calculate time of flight 
time_of_flight = (-vy + math.sqrt((vy**2) + (2 * gravitational_acceleration * air_resistance))) / (gravitational_acceleration - air_resistance) 
# calculate the range of the balloon 
range = vx * time_of_flight  
print("The range of the balloon is", range, "meters.")
