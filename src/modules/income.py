import datetime
import src.ui_uix.main_page as main
import src.core.utilts as utilts
import src.core.module_procces as moduleProcces
from src.ui_uix.user import users
from prettytable import PrettyTable


def addIncome():
    print("\n<--------GELİR EKLE-------->")

    
    # değerlerin kontrollerini detaylandır vakit kalırsa.
    # https://www.reddit.com/r/learnpython/comments/wqxzdl/stuck_on_datetime_with_tryexcept_error_handling/
    while True:
        incomeName = input("Gelir Adı: ").strip().lower()
        if incomeName == "":
            print(" Gelir Adı boş bırakılamaz.")
            return
        else:
            break

    while True:
        incomeAmount_str = input("Gelir Tutarı: ").strip()
        try:
            incomeAmount = float(incomeAmount_str)
            if incomeAmount <= 0:
                print("Gelir Tutarı pozitif bir sayı olmalıdır.")
                return False
            else:
                break
        except ValueError:
            print("Gelir Tutarı sadece sayısal bir değer olabilir.")
            

    while True:
        incomeDate = input(
            "Gelir Tarihi (YYYY/MM/DD): ").strip()
        try:
            datetime.datetime.strptime(incomeDate, "%Y/%m/%d")
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatını kullanın.")

    incomeDesc = input("Gelir Açıklaması: ").strip()

    if incomeName == "" or incomeAmount == "" or incomeDate == "":
        print(" Lütfen geçerli bir değer girin.")
        return addIncome()
    else:
        incomeCat = moduleProcces.selectCategory("income")
        addIncomeProcces(incomeName, incomeAmount,
                     incomeDate, incomeDesc, incomeCat)

def addIncomeProcces(icName, icAmount, icDate, icDesc, icCat):
    try:
        incomes = utilts.jsonRead("incomes.json")
    except:
        print("Dosya Bulunamadı.")
        incomes = []
    actvUser = users.active_user

    # for income in incomes:
    #     if actvUser["userId"] and income["incomeName"] == icName and income["incomeAmount"] == icAmount and income["incomeDate"] == icDate and income["incomeDesc"] == icDesc and income["incomeCategory"] == icCat:
    #         print("Bu Gelir işlemi Zaten Kayıtlı")
    #         return main.income()
    incomeId = utilts.uniqeId()
    while True:
        controlId = utilts.uniqeCheck(incomes, "incomeId", incomeId)
        if controlId == True:
            incomeId = utilts.uniqeId()
        else:
            break
    data = {
        "incomeId": incomeId,
        "userId": actvUser["userId"],
        "incomeName": icName,
        "incomeAmount": icAmount,
        "incomeDate": icDate,
        "incomeDesc": icDesc,
        "incomeCat": icCat
    }

    incomes.append(data)
    utilts.jsonWrite(incomes, "incomes.json")
    print("Gelir Başarıyla KAydedildi")
    return main.income()


def updateIncome():
    print("\n<--------GELİR DÜZENLE-------->")
    incomeList, data = listIncome()
    selectedId = None
    if incomeList == True:
        while True:
            select = input(
                "Güncellemek İstediğiniz Gelirin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Gelir Seçilmedi")
                return
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["incomeId"]
                print(f"{data[index]["incomeName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
                return

    updateTable = PrettyTable()
    updateTable.field_names = [
        "Gelir Adı", "Gelir Tutarı", "Gelir Tarihi", "Gelir Açıklaması", "Gelir Kategiorisi"]

    updateTable.add_row([data[index]["incomeName"], data[index]["incomeAmount"],
                        data[index]["incomeDate"], data[index]["incomeDesc"], data[index]["incomeCat"]])
    updateTable.add_autoindex("No")
    print("\n<--------GÜNCELLENİLECEK GELİR-------->")
    print(updateTable)

    while True:
        incomeName = input("Gelir Adı: ").strip().lower()
        if incomeName == "":
            print(" Gelir Adı boş bırakılamaz.")
        else:
            break

    while True:
        incomeAmount_str = input("Gelir Tutarı: ").strip()
        try:
            incomeAmount = float(incomeAmount_str)
            if incomeAmount <= 0:
                print("Gelir Tutarı pozitif bir sayı olmalıdır.")
            else:
                break
        except ValueError:
            print("Gelir Tutarı sadece sayısal bir değer olabilir.")

    while True:
        incomeDate = input(
            "Gelir Tarihi (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(incomeDate, '%Y-%m-%d')
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatını kullanın.")
            return

    incomeDesc = input("Gelir Açıklaması: ").strip()
    while True:
        catQest = input(
            "KategoriYİ Değiştirecek Misiniz (Y/N)? ").strip().lower()
        if catQest == "y":
            incomeCat = moduleProcces.selectCategory("income")
            break
        elif catQest == "n":
            incomeCat = data[index]["incomeCat"]
            break
        else:
            print("Lütfen Geçerli bir Değer Giriniz")
            return

    updateProcces(selectedId, incomeName, incomeAmount,
                  incomeDate, incomeDesc, incomeCat)


def updateProcces(icId, icName, icAmount, icDate, icDesc, icCat):
    incomes = utilts.jsonRead("incomes.json")
    actvUser = users.active_user
    for ic in incomes:
        if ic["incomeId"] == icId:
            ic["incomeName"] = icName
            ic["incomeAmount"] = icAmount
            ic["incomeDate"] = icDate
            ic["incomeDesc"] = icDesc
            ic["incomeCat"] = icCat
            utilts.jsonWrite(incomes, "incomes.json")
            print("gelir Güncellendi")
            return main.income()

    print("Gelir Bulunamadı")
    return main.income()


def removeIncome():
    print("\n<--------GELİR SİL-------->")
    try:
        incomes = utilts.jsonRead("incomes.json")
    except:
        print("Dosya Bulunamadı.")
        incomes = []
    incomeList, data = listIncome()
    selectedId = None
    if incomeList == True:
        while True:
            select = input(
                "Silmek İstediğiniz Gelirin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Gelir Seçilmedi")
                return
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["incomeId"]
                print(f"{data[index]["incomeName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
                return

    for ic in incomes:
        if ic["incomeId"] == selectedId:
            incomes.remove(ic)
            utilts.jsonWrite(incomes, "incomes.json")
            print("Gelir Başarılı Şekilde Silindi.")
            return main.income()

    print("Gelir Bulunamadı/Silinemedi")


def listIncome():
    actvUser = users.active_user
    myList = utilts.jsonRead("incomes.json")
    data = [
        x for x in myList
        if x["userId"] == actvUser["userId"]
    ]
    if data:
        dataTable = PrettyTable()
        dataTable.field_names = [
            "Gelir Adı", "Gelir Tutarı", "Gelir Tarihi", "Gelir Açıklaması", "Gelir Kategiorisi"]
        for dt in data:
            dataTable.add_row([dt["incomeName"], dt["incomeAmount"],
                              dt["incomeDate"], dt["incomeDesc"], dt["incomeCat"]])
        dataTable.add_autoindex("No")
        print(dataTable)
        return True, data
    else:
        print("Mevctut Gelir Listesi Bulunmamaktadır.")
        return


def listAllIncome():
    print("\n<--------GELİR LİSTELE-------->")
    listIncome()
    main.income()
