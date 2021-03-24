def defining_dictionaries():
    print(" Finding a dictonary --------------------")
    dictio = {
        "Car":"BMW",
        "Model": "2020"
    }
    print(dictio)

    new_dict = dict(
        car = "bwm"
    )
    print(new_dict)

def converting_dict_into_list():
    print("Converting Dictionary to List")
    dict= {
        "BMW": "2012",
        "FORD": "2010"
    }
    list  = []
    for element in dict:
        b=(element, dict)
        list.append(b)
    print(list)


def update_dictionaries():
    print("Updating Dictionary")
    dict = {"car":"bmw", "model":"2020"}
    dict_updated = {"car": "Ford"}
    print(dict)
    dict.update(dict_updated)
    print(dict)

def merge_dictionaries():
    print("Merging Dictionaries")
    print("Merge two dictionaries ")
    dict = {"car":"BMW", "model": "2020"}
    dict2 = {"plane": "Fighter", "cycle": "racing"}
    dict.update(dict2)
    print(dict)

def delete_dictionary_element():
    print("Delete Dictionary Elements")
    print("Deleting dictionary item")
    dict = {"car": "BMW", "model": "2020"}
    print(dict)
    del dict['car']
    print(dict)

def delete_dictionary_element_pop():
    print("Delete dictionary elements with pop")
    print("Deleting dictionary item with pop")
    dict = {"car": "BMW", "model": "2020"}
    print(dict)
    dict.pop("car")
    print(dict)
    dict.popitem()
    print(dict)

def find_length_dict():
    print("Fiding the Dictionary Length")
    print("Find length dictionaries")
    dict = {"car": "BMW", "model": "2020"}
    print(len(dict))

def check_if_key_exists():
    print("Checking if a element exists")
    print("Checking if a key exist in the dictionary")
    dict = {"car": "BMW", "model": "2020"}
    if "car" in dict:
        print("Yes")

def dict_comprehension():
    print("Dictionary comprehension")
    print("Dictionarie comprehension")
    dict = {i:i**2 for i in range(5)}
    print(dict)

def sort_dictionationaries():
    print("Sorting Dictionaries ")
    print("Sorting dictionaries")
    dict = {
        "BMW":2020,
        "Ford": 2019,
        "Toyota": 2018,
        "BMW": 2012,
        "Honda": 2015 ,
    }
    print("Sorting")
    print("Sorting", sorted(dict))
    # Sort by Key
    for key in sorted(dict):
        print("%s : %s " % (key, dict[key]))

    #Sort by Values
    for key in sorted(dict, key=dict.get):
        print("%s : %s " %(key, dict[key]))


def adding_elements():
    print("Adding element to dictionaries")
    person = {
        'name': 'Andres',
        'phone_number': '111 - 222 - 333',
        'age': 25
    }
    person['lastname'] = 'Montoya'
    print(person)


def iterating_with_items():
    print("Playing with items()")
    cars = {
        "BMW": 2020,
        "Ford": 2019,
        "Toyota": 2018,
        "BMW": 2012,
        "Honda": 2015,
    }

    for key, value in cars.items():
        print("%s : %s " %(key, value))


def all_deletion_together():
    print("All Deletion")
    person = {
        'name': 'Andres',
        'last_name': 'Montoya',
        'age': 25,
        'phone': '123-32122',
    }
    print(person)
    del person['name']
    person.pop('last_name')
    person.popitem()
    print(person)


if __name__ == '__main__':
    defining_dictionaries()
    adding_elements()
    update_dictionaries()
    merge_dictionaries()
    sort_dictionationaries()
    delete_dictionary_element()
    all_deletion_together()
    find_length_dict()
    check_if_key_exists()
    converting_dict_into_list()
    delete_dictionary_element_pop()
    dict_comprehension()
    iterating_with_items()