import src.ui_uix.main_page as main
import src.core.utilts as utilts
from src.ui_uix.user import users


def addCategory():
    print("\n<--------KATEGORİ EKLE-------->")
    catName = input("Kategori Adı: ").lower()
    # if catName == "" or " ":
    #     print("Boş Değer Kabul Edilemez.")
    #     return addCategory()
    while True:
        catTypeOpt = input(
            "1.Gelir Kategorisi\n2.Gider Kategorsi\nKategori Türünü Seçiniz: ")
        if catTypeOpt == "1":
            catType = "income"
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
            
    except :
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
    while True:
        catTypeOpt = input(
            "1.Gelir Kategorisi\n2.Gider Kategorsi\nKategori Türünü Seçiniz: ")
        if catTypeOpt == "1":
            catType = "income"
            break
        elif catTypeOpt == "2":
            catType = "expense"
            break
        else:
            print("Lütfen Geçerli Bir Değer Giriniz. (1/2)")

    while True:
        catName = input("Mevcut Kategori Adı: ").lower()
        newCatName = input("Yeni Kategori Adı: ").lower()
        # if (catName and newCatName) == ("" or " "):
        #     print("Boş Değer Kabul Edilemez.")
        #     return updateCategory()
        break

    updateCategoryProcces(catName, newCatName, catType).lower()


def updateCategoryProcces(catName, newCatName, catType):
    categories = utilts.jsonRead("categories.json")
    actvUser = users.active_user

    for cat in categories:
        print(f"catName {cat["catName"]}")
        if cat["catType"] == catType:
            if actvUser == cat["userId"]:
                if cat["catName"] != newCatName:
                    if cat["catName"] == catName:
                        cat["catName"] = newCatName
                        utilts.jsonWrite(categories, "categories.json")
                        print(f"{catName} ismine sahip kategori {newCatName} olarak güncellendi.")
                        return main.category()
                else:
                    print("\nBu İsim ve Kategori Türünde Kategori Mevcuttur.")
                    return main.category()
            
    print("\n\nBu İsimde veya Kategori Türünde Bir  Kategoriniz Bulunmaktadır.")
    return main.category()

    


def removeCategory():
    print("\n<--------KATEGORİ SİL-------->")


def listCategory():
    print("\n<--------KATEGORİ LİSTELE------->")
