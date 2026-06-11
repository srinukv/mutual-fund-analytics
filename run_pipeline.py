"""
Master Pipeline Script

Runs all major project stages in sequence.
"""

import subprocess
import sys


def run_script(script_path):
    print(f"\nRunning: {script_path}")

    result = subprocess.run(
        [sys.executable, script_path]
    )

    if result.returncode != 0:
        print(f"Error running {script_path}")
        sys.exit(1)


def main():

    scripts = [
        "scripts/data_ingestion.py",
        "scripts/amfi_validation.py",
        "scripts/data_cleaning.py",
        "scripts/create_database.py",
        "scripts/load_data.py"
    ]

    for script in scripts:
        run_script(script)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()