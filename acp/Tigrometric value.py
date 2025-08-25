import math
import random


random_angle_degrees = random.uniform(0, 360)


random_angle_radians = math.radians(random_angle_degrees)


sine_value = math.sin(random_angle_radians)
cosine_value = math.cos(random_angle_radians)
tangent_value = math.tan(random_angle_radians)

# Print the results
print(f"Random angle (degrees): {random_angle_degrees:.2f}")
print(f"Random angle (radians): {random_angle_radians:.2f}")
print(f"Sine of the angle: {sine_value:.4f}")
print(f"Cosine of the angle: {cosine_value:.4f}")
print(f"Tangent of the angle: {tangent_value:.4f}")