import src.ui_uix.main_page as main
import src.core.utilts as utilts
from src.ui_uix.user import users
from prettytable import PrettyTable


def addCategory():
    print("\n<--------KATEGORİ EKLE-------->")
    while True:
        catName = input("Kategori Adı: ").strip().lower()

        if catName == "":
            print(" Lütfen geçerli bir ad girin.")
        else:
            break

    while True:
        catTypeOpt = input(
            "1.Kategori Kategorisi\n2.Gider Kategorsi\nKategori Türünü Seçiniz: ")
        if catTypeOpt == "1":
            catType = "category"
            break
        elif catTypeOpt == "2":
            catType = "expense"
            break
        else:
            print("Lütfen Geçerli Bir Değer Giriniz. (1/2)")
    addCategoryProcces(catName, catType)


def addCategoryProcces(name, catType):
    try:
        categories = utilts.jsonRead("categories.json")

    except:
        print("Dosya Bulunamadı\n")
        categories = []
    actvUser = users.active_user
    print(categories)

    for cat in categories:
        print(f"kName {cat["catName"]}")
        if cat["catName"] == name and cat["catType"] == catType and actvUser["userId"]:
            print("Bu Kategori Mevcut! ")
            return main.category()

    # cat id ekle onu unuttum
    catId = utilts.uniqeId()
    print(catId)
    while True:
        controlId = utilts.uniqeCheck(categories, "catId", catId)
        if controlId == True:
            catId = utilts.uniqeId()
        else:
            break

    data = {
        "catId": catId,
        "userId": actvUser["userId"],
        "catType": catType,
        "catName": name
    }
    categories.append(data)
    print(data)
    utilts.jsonWrite(categories, "categories.json")
    print("Kategori Başarıyla Oluşturuldu.")
    return main.category()


def updateCategory():
    print("\n<--------KATEGORİ DÜZENLE-------->")
    categoryList, data = listAllCategories()
    selectedId = None
    if categoryList == True:
        while True:
            select = input(
                "Güncellemek İstediğiniz Kategorinin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Kategori Seçilmedi")
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["categoryId"]
                print(f"{data[index]["categoryName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
    updateTable = PrettyTable()
    updateTable.field_names = ["Kategori Türü","Kategori Adı"]

    updateTable.add_row([data[index]["catType"], data[index]["catName"]])
    updateTable.add_autoindex("No")
    print("\n<--------GÜNCELLENİLECEK KATEGORİ-------->")
    print(updateTable)
    
    while True:
        catTypeOpt = input(
            "1.Kategori Kategorisi\n2.Gider Kategorsi\nKategori Türünü Seçiniz: ")
        if catTypeOpt == "1":
            catType = "category"
            break
        elif catTypeOpt == "2":
            catType = "expense"
            break
        else:
            print("Lütfen Geçerli Bir Değer Giriniz. (1/2)")

    while True:
        catName = input("Kategori Adı: ").strip().lower()
        if catName == "":
            print(" Kategori Adı boş bırakılamaz.")
        else:
            break
    updateCategoryProcces(selectedId,catName, catType)


def updateCategoryProcces(catId ,catName, catType):
    categories = utilts.jsonRead("categories.json")
    actvUser = users.active_user
    
    for cat in categories:
        if cat["catName"] == catName and cat["catType"] == catType and actvUser["userId"]:
            print("Bu Kategori Mevcut! ")
            return main.category()

    for cat in categories:
        if cat["catId"] == catId:
            cat["catType"] = catType
            cat["catName"] = catName
            utilts.jsonWrite(categories ,"categories.json")
            print("Kategori Güncellendi")
            return main.category()

    print("\n\nBu İsimde ve Kategori Türünde Bir  Kategoriniz Bulunmaktadır.")
    return main.category()


def removeCategory():
    print("\n<--------KATEGORİ SİL-------->\n")
    try:
        categories = utilts.jsonRead("categories.json")
        incomes = utilts.jsonRead("incomes.json")
        
    except:
        print("Dosya Bulunamadı.")
        categories = []
    try:
        incomes = utilts.jsonRead("incomes.json")
        
    except:
        print("Dosya Bulunamadı.")
        categories = []
    try:
        expenses = utilts.jsonRead("expense.json")
        
    except:
        print("Dosya Bulunamadı.")
        categories = []
    actvUser = users.active_user 
    categoryList, data = listAllCategories()
    selectedId = None
    if categoryList == True:
        while True:
            select = input(
                "Güncellemek İstediğiniz Kategorinin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Kategori Seçilmedi")
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["catId"]
                print(f"{data[index]["catName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
    for ic in incomes:
        if actvUser["userId"] and ic["incomeCat"] == selectedId:
            print("\n\nBu kategoriye bağlı  gelir bulunduğundan  kategoriyi silemezsiniz")
            return main.category
        
    for xp in expenses:
        if actvUser["userId"] and ic["expenseCat"] == selectedId:
            print("\n\nBu kategoriye bağlı  gelir bulunduğundan  kategoriyi silemezsiniz")
            return main.category
        
    for ic in categories:
        if ic["catId"] == selectedId:
            categories.remove(ic)
            utilts.jsonWrite(categories, "categoréies.json")
            print("Kategori Başarılı Şekilde Silindi.")
            return main.category()

    print("kategori Bulunamadı/Silinemedi")
   

def removeCategoryProcces(catName, catType):
    try:
        categories = utilts.jsonRead("categories.json")

    except:
        print("Dosya Bulunamadı\n")
        categories = []
    actvUser = users.active_user
    
    catList ,data =listAllCategories()
    selectedId = None
    if catList == True:
        while True:
            select = input(
                "Silmek İstediğiniz Kategorinin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("KAtegori Seçilmedi")
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["catId"]
                print(f"{data[index]["catName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")

    for cat in categories:
        if cat["catId"] == selectedId:
            categories.remove(cat)
            utilts.jsonWrite(categories, "categories.json")
            print("KAtegori Başarılı Şekilde Silindi.")
            return main.category()

    print("Kategori Bulunamadı/Silinemedi")


def listCategory():
    print("\n<--------KATEGORİ LİSTELE------->")
    categories = utilts.jsonRead("categories.json")
    actvUser = users.active_user

    income_table = PrettyTable()
    expense_table = PrettyTable()
    
    income_table.field_names = ["Kategori Türü", "Kategori Adı"]
    expense_table.field_names = ["Kategori Türü", "Kategori Adı"]
    for cat in categories:
        if cat["userId"] == actvUser["userId"]:
            if cat["catType"] == "income":
                income_table.add_row(["Gelir", cat["catName"]])
    income_table.add_autoindex("")

    for cat in categories:
        if cat["userId"] == actvUser["userId"]:
            if cat["catType"] == "expense":
                expense_table.add_row(["Gider", cat["catName"]])
    expense_table.add_autoindex("")

    print("\n<--------GELİR KATEGORİLERİ------->")
    print(income_table)
    print("\n<--------GİDER KATEGORİLERİ------->")
    print(expense_table)
    return main.category()


def listAllCategories():
    actvUser = users.active_user
    myList = utilts.jsonRead("categories.json")
    data = [
        x for x in myList
        if x["userId"] == actvUser["userId"]
    ]
    if data:
        dataTable = PrettyTable()
        dataTable.field_names = [
            "Kategori Türü","Kategori Adı"]
        for dt in data:
            dataTable.add_row([dt["catType"],dt["catName"] ])
        dataTable.add_autoindex("No")
        print(dataTable)
        return True, data
    else:
        print("Mevctut Kategori Bulunmamaktadır.")
