import uuid
import json
import os


def uniqeCheck(myList, prop, userInput):
    print('myList= ', myList)
    print('prop= ', prop)
    print('userInput=> ', userInput)
    for element in myList:
        print('element=> ', element)
        if userInput == element[prop]:
            return True
    return False


def find(myList, prop, userInput):
    for element in myList:
        if userInput == element[prop]:
            return True

    return False


def uniqeId():
    customer_id = str(uuid.uuid4())
    return customer_id


def getJsonFile(fileName: str):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = os.path.join(base_dir, "data")
    full_name = os.path.join(data_path, fileName)
    print(f" : {full_name}")
    return full_name


def jsonWrite(listName, jsonName):
    data_dir = None
    try:
        data_dir = getJsonFile(jsonName)
        json_str = json.dumps(listName, ensure_ascii=False, indent=3)
        with open(data_dir, "w", encoding='utf-8') as f:
            f.write(json_str)
        print("dosya yazıldı")
    except:
        print(f'Error occurred when opening {listName} to read')
        return None


def jsonRead(jsonName):

    try:
        data_dir = getJsonFile(jsonName)
        with open(data_dir, "r", encoding='utf-8') as file:
            listUser = json.load(file)
            print("dosya okundu")
            print("list user burda", listUser)
            return listUser
    except FileNotFoundError:
        print(f'{data_dir} Dosya Bulunamadı')
        return []
    except Exception as e:
        print(
            f'Error occurred when reading JSON file: {data_dir}. Details: {e}')
        return []
