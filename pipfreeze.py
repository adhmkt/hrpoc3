import subprocess

def update_requirements():
    # Run 'pip freeze' and capture its output
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)

    # Write the output to requirements.txt
    with open('requirements.txt', 'w') as file:
        file.write(result.stdout.decode('utf-8'))

if __name__ == "__main__":
    update_requirements()
