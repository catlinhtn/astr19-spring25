import math

def main():
    start = 0
    end = 2
    entries = 1000
    step = (end - start) / (entries - 1) 

    print("x\t\tsin(x)")
    print("-" * 20)

    for i in range(entries):
        x = start + i * step
        sin_x = math.sin(x)
        print(f"{x:.6f}\t{sin_x:.6f}")

main()

