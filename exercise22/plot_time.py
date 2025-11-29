import subprocess
import matplotlib.pyplot as plt

process_counts = [1, 2, 3, 4]
times = []

for p in process_counts:
    print(f"Running with {p} process(es)...")

    cmd = f"mpiexec -n {p} python Ex22.py"
    output = subprocess.check_output(cmd, shell=True).decode()

    for line in output.split("\n"):
        if "Rank 0:" in line and "Time taken" in line:

            # Example line: Rank 0: Time taken = 2.140633 seconds for N=5000 ...
            # Step 1: split on '='
            number_part = line.split("=")[1].strip()

            # Step 2: first token after '=' is the time value
            time_value = float(number_part.split()[0])

            times.append(time_value)
            break

# ---- plotting ----
plt.figure(figsize=(7,5))
plt.plot(process_counts, times, marker='o', linewidth=2)
plt.xlabel("Number of Processes")
plt.ylabel("Time (seconds)")
plt.title("Time Taken vs Number of Processes for N = 5000")
plt.grid(True)
plt.savefig("Ex22_time.png", dpi=150)

print("Figure saved as Ex22_time.png")
