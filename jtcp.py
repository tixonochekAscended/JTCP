import json, sys, os, random
from typing import NoReturn

def error(text: str) -> NoReturn:
    print(f"{text}")
    sys.exit(-1)

def run() -> None:
    file_name: str = ""
    if len(sys.argv) == 1:
        error("No file provided to process.")
    elif len(sys.argv) >= 2:
        file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        error("The file you provided doesn't exist.")
    if not file_name.endswith(".json"):
        error("The file you provided isn't a JSON file.")

    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if type(data) is not list:
        error("Invalid format for JTCP: the JSON isn't a list-only file.")

    res_file_name: str = ''.join(file_name.split('.')[:-1])+str(random.randint(1,1000))+'.css'
    print(f'Compiling {file_name} into {res_file_name}...')
    final_css: str = ""
    for el in data:
        if type(el) is not dict:
            error("Invalid format for JTCP: element should have been a dictionary.")

        has_name: bool = False
        has_body: bool = False
        to_add: str = ""
        for j in el.items():
            if j[0] == "name":
                has_name = True
                if type(j[1]) is not str:
                    error("Invalid format for JTCP: element should have been a string.")
                if j[1] == "_":
                    continue
                to_add += j[1] + " "
            elif j[0] == "class":
                if type(j[1]) is not list:
                    error("Invalid format for JTCP: element should have been a list of classes (strings).")
                for i in j[1]:
                    if type(i) is not str:
                        error("Invalid format for JTCP: element should have been a class name (string).")
                    to_add += f".{i} "
            elif j[0] == "id":
                if type(j[1]) is not list:
                    error("Invalid format for JTCP: element should have been a list of IDs (strings).")
                for i in j[1]:
                    if type(i) is not str:
                        error("Invalid format for JTCP: element should have been an ID (string).")
                    to_add += f"#{i} "
            elif j[0] == "other_attr":
                if type(j[1]) is not list:
                    error("Invalid format for JTCP: element should have been a list of other attributes (strings).")
                for i in j[1]:
                    if type(i) is not str:
                        error("Invalid format for JTCP: element should have been a different attribute (string).")
                    to_add += f":{i} "
            elif j[0] == "style":
                has_body = True
                to_add_body: str = ""
                if type(j[1]) is not dict:
                    error("Invalid format for JTCP: element should have been a dictionary.")
                for i in j[1].items():
                    to_add_body += f"  {i[0]}: {i[1]};\n"
                to_add += "{\n%s}\n" % to_add_body
            else:
                error(f"Invalid format for JTCP: {j[0]} is not defined.")
        if not has_name:
            error("Invalid format for JTCP: no name found.")
        if not has_body:
            error("Invalid format for JTCP: no body (\"style\") found.")
        final_css += to_add + "\n"

    try:
        with open(res_file_name, "w", encoding="utf-8") as f:
            f.write(final_css)
    except:
        error("Couldn't open (or create) a file and write the resulting CSS into it.")

    print('Compiled successefully!')

if __name__ == "__main__":
    run()
