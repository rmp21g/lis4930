# Ryan Michael Parks (rmp21g)
import pkg_resources

# List of packages
packages = [
    "jupyterlab",
    "pandas",
    "numpy",
    "scikit-learn",
    "django",
    "tensorflow",
    "scipy",
    "matplotlib",
    "keras"
]

# Print Python version
import sys
print(f"Python version:\n{sys.version}\n")

# Print each package version
for package in packages:
    try:
        version = pkg_resources.get_distribution(package).version
        print(f"{package}: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{package}: not installed")
