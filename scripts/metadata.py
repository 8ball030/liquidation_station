import json
import os
import subprocess
import sys


def generate(package, index):
    # Your code to generate the package goes here
    cmd = f"python3 /home/tom/Desktop/Fun/auto_dev/scripts/metadata.py generate --strict . {package} {index}"
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    if result.returncode != 0:
        print(f"Failed to generate {package}")
        sys.exit(1)


def generate_components(package_data):
    index = 1
    for package in package_data:
        print(f"Processing: {package} {index}")
        generate(package, index)
        index += 1


def main():
    with open("packages/packages.json", "r") as packages_file:
        data = json.load(packages_file)
        dev_packages = data["dev"]
        package_names = list(dev_packages.keys())

        generate_components(package_names)


if __name__ == "__main__":
    main()
