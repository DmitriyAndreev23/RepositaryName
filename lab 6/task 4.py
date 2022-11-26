import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        table = []
        for index, line in enumerate(f):
            u = line.strip(new_line).split(delimiter)
            if index == 0:
                headers = u
                continue
            table.append({})
            for i, _ in enumerate(headers):
                table[-1][headers[i]] = u[i]
        return table

    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))