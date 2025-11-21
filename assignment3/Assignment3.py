def parseGroundMotionData(filename: str):


    data = []
    dt = None
    read_data = False

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if "*** Begin data ***" in line:
                read_data = True
                continue

            if "*** End data ***" in line:
                break

            if not read_data:
                continue

            if "NPTS" in line and "DT" in line:
                words = line.split()
                for i in range(len(words)):
                    if "DT=" in words[i]:
                        part = words[i].split("=")
                        if len(part) > 1 and part[1]:
                            dt = float(part[1])
                        else:
                            dt = float(words[i + 1])
                        break
                continue

            words = line.split()
            for w in words:
                try:
                    data.append(float(w))
                except Exception:
                    continue

    return data, dt


def saveGroundMotionData(data, dt):
 
    g = 9.81
    with open('elCentro.out', 'w') as file:
        for i in range(len(data)):
            t = i * dt
            a = data[i] * g
            file.write(f"{t}, {a}\n")


import json

def saveGroundMotionDataJSON(data, dt):


    g = 9.81
    json_data = {"acceleration": []}

    # Build the list of (time, acceleration) tuples
    for i in range(len(data)):
        t = i * dt
        a = data[i] * g
        json_data["acceleration"].append((t, a))

    # Write JSON data to file
    with open('elCentro.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    return json_data
