def defining_dictionaries():
    print("----------------------------------------")
    dictio = {
        "Car":"BMW",
        "Model": "2020"
    }
    print(dictio)

    new_dict = dict(
        car = "bwm"
    )
    print(new_dict)


def update_dictionaries():
    print("----------------------------------------")
    dict = {"car":"bmw", "model":"2020"}
    dict_updated = {"car": "Ford"}
    print(dict)
    dict.update(dict_updated)
    print(dict)

def merge_dictionaries():
    print("----------------------------------------")
    print("Merge two dictionaries ")
    dict = {"car":"BMW", "model": "2020"}
    dict2 = {"plane": "Fighter", "cycle": "racing"}
    dict.update(dict2)
    print(dict)

def delete_dictionary_element():
    print("----------------------------------------")
    print("Deleting dictionary item")
    dict = {"car": "BMW", "model": "2020"}
    print(dict)
    del dict['car']
    print(dict)

def find_length_dict():
    print("----------------------------------------")
    print("Find length dictionaries")
    dict = {"car": "BMW", "model": "2020"}
    print(len(dict))

def check_if_key_exists():
    print("----------------------------------------")
    print("Checking if a key exist in the dictionary")
    dict = {"car": "BMW", "model": "2020"}
    if "car" in dict:
        print("Yes")

def sort_dictionationaries():
    print("----------------------------------------")
    print("Sorting dictionaries")
    dict = {
        "BMW":2020,
        "Ford": 2019,
        "Toyota": 2018,
        "BMW": 2012,
        "Honda": 2015 ,
    }
    # Sort by Key
    for key in sorted(dict):
        print("%s : %s " % (key, dict[key]))

    #Sort by Values
    for key in sorted(dict, key=dict.get):
        print("%s : %s " %(key, dict[key]))


if __name__ == '__main__':
    defining_dictionaries()
    update_dictionaries()
    merge_dictionaries()
    sort_dictionationaries()
    delete_dictionary_element()
    find_length_dict()
    check_if_key_exists()