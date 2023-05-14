import subprocess

# Execute Linux command
command = "ls"
output = subprocess.check_output(command, shell=True)

# Print output
print(output.decode())
