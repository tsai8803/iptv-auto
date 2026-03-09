import requests

input_file = "source.txt"
output_file = "tv.txt"

timeout = 5

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

working = []

for line in lines:
    if "," not in line:
        continue

    name, url = line.strip().split(",", 1)

    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code == 200:
            working.append(line)
            print("OK:", name)
        else:
            print("FAIL:", name)
    except:
        print("ERROR:", name)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(working)
