# IsEverythingInstalled.py

import importlib.util

REQUIRED_PACKAGES = [
    'qiskit',
    'qiskit_aer',
    'matplotlib',
    'numpy',
    'jupyter',
]

def check_packages(packages):
    missing = []
    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    return missing

if __name__ == "__main__":
    print("Checking for required packages...\n")
    missing = check_packages(REQUIRED_PACKAGES)
    if not missing:
        print("✅ All required packages are installed.")
    else:
        print("❌ The following packages are missing:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nYou can install them using:")
        print(f"pip install {' '.join(missing)}")
