import json
import random

def load_json():

    with open("json/safety_equipment.json", "r") as file:
        json_object = json.load(file)

    return json_object

def write_json(json_object):

    with open("json/safety_equipment.json", "w") as file:
            json.dump(json_object, file, indent="\t")

def make_equip_combination(json_object):

    combination = {}

    for part in list(json_object.keys()):

        equipments = list(json_object[part].keys())
        equipment_chosen = random.choice(equipments)
        combination[part] = equipment_chosen
        json_object[part][equipment_chosen] += 1


    # print(all_equipment_count)
    print(combination)
    print("-")

    return json_object

if __name__ == "__main__":

    json_object = load_json()
    print(json_object)
    print("-")

    while True:

        cmd = input("Make combination? [y]/[n]...")

        if cmd == "y":
            json_result = make_equip_combination(json_object)
        else:
            print("exit...")
            break

        cmd = input("Save? [y]/[n]...")

        if cmd == "y":
            write_json(json_result)
            print("saved!")
            break
        else:
            continue
