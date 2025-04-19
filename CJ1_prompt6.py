import math

def sin_function(x):
    return math.sin(x)

def cos_function(x):
    return math.cos(x)

# tabulate x, sinx, cosx with defs above
x_values = []
sin_values = []
cos_values = []

num_points = 1000
start = 0
end = 2
step = (end - start) / (num_points - 1)

for i in range(num_points):
    x = start + i * step
    x_values.append(x)
    sin_values.append(sin_function(x))
    cos_values.append(cos_function(x))

#print table with values above
print("x\t\tsin(x)\t\tcos(x)")
print("-" * 35)
for i in range(10):
    print(f"{x_values[i]:.6f}\t{sin_values[i]:.6f}\t{cos_values[i]:.6f}")
    