import json
import os
import subprocess
import sys
from collections import defaultdict

YEAR = sys.argv[1]


def run_script(filepath):
    process = subprocess.run(["python", filepath], stderr=subprocess.PIPE)
    output = process.stderr.decode()

    return float(output.split()[-1])


def get_year_solution_scripts(year):
    scripts = []

    for root, dirs, _ in os.walk(os.path.abspath(f"../{year}/")):
        for _dir in dirs:
            for _file in os.listdir(os.path.join(root, _dir)):
                if _file.endswith(".py"):
                    scripts.append(os.path.join(root, _dir, _file))

    return scripts


results = defaultdict(dict)

for script in get_year_solution_scripts(YEAR):
    exec_time = run_script(script)

    if exec_time > 10:
        duration = exec_time
    else:
        duration = sum([run_script(script) for _ in range(10)]) / 10

    split = script.split("/")
    results[split[-2]][split[-1][:-3]] = round(duration, 3)

with open(f"{YEAR}.json", "w") as f:
    f.write(json.dumps(results, indent=4))
