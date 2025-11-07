from src.ui_uix.user import users
import src.core.utilts as utils
from prettytable import PrettyTable


def selectCategory(catType):
    catTypeList = utils.jsonRead("categories.json")
    actvUser = users.active_user

    categories = [
        cat for cat in catTypeList
        if cat["userId"] == actvUser["userId"] and cat["catType"] == catType
    ]

    selectedId = None
    if categories:
        categoriesTable = PrettyTable()
        categoriesTable.field_names = ["Kategori Adı"]

        for cat in categories:
            categoriesTable.add_row([cat["catName"]])
        categoriesTable.add_autoindex("Seçim No")
        print(f"\n--- {catType} KATEGORİLERİ ---")
        print(categoriesTable)
        

        while True:
            select = input(
                "Seçmek İstediğiniz Kategorinin Numarasını Giriniz: ").strip()
            if select == "":
                selectedId = None
                print("Kategori Seçilmedi")
                return selectedId

            index = int(select) - 1
            if 0 <= index < len(categories):
                selectedId = categories[index]["catName"]
                print(f"{selectedId} kategorisi seçildi")
                return selectedId
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
    else:
        print(f"Mevcut {catType} Kategoriniz Bulunmamaktadır.")

""" 
def selectProcces(procType):
    #  categories = data
    actvUser = users.active_user
    if procType == "income":
        myList = utils.jsonRead("incomes.json")
        data = [
            x for x in myList
            if x["userId"] == actvUser["userId"]
        ]
    elif procType == "expense":
        myList = utils.jsonRead("incomes.json")
        data = [
            x for x in myList
            if x["userId"] == actvUser["userId"]
        ]

    selectedId = None
    if data:
        dataTable = PrettyTable()
        if procType == "income":
            dataTable.field_names = [
                "Gelir Adı", "Gelir Tutarı", "Gelir Tarihi" "Gelir Açıklaması"]
        elif procType == "expense":
            dataTable.field_names = [
                "Gider Adı", "Gider Tutarı", "Gider Tarihi" "Gider Açıklaması"]
# buradan sonra
        for x in data:
            dataTable.add_row([cat["catName"]])
        dataTable.add_autoindex("Seçim No")

        print(f"\n--- {catType} KATEGORİLERİ ---")
        print(dataTable)

        while True:
            select = input(
                "Seçmek İstediğiniz Kategorinin Numarasını Giriniz: ").strip()
            if select == "":
                selectedId = None
                print("KAtegori Seçilmedi")
                return selectedId

            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["catName"]
                print(f"{selectedId} kategorisi seçildi")
                return selectedId
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
    else:
        print(f"Mevcut {catType} Kategoriniz Bulunmamaktadır.")
 """