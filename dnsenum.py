import subprocess

a = ["www", "users", "es"]
b = []
for i in a:
    # Use subprocess.run to capture output and potential errors
    result = subprocess.run(f"host -t a {i}.pja.edu.pl", shell=True, capture_output=True)
    print(result)
    # Check for errors and handle them appropriately
    if result.returncode == 0:
        b.append(result.stdout.decode("utf-8").strip())
    else:
        print(f"Error occurred for {i}.pja.edu.pl: {result.stderr.decode('utf-8')}")
print("\n")
for i in b:
    print(i)