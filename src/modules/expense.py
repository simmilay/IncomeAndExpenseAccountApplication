import datetime
import src.ui_uix.main_page as main
import src.core.utilts as utilts
import src.core.module_procces as moduleProcces
from src.ui_uix.user import users
from prettytable import PrettyTable


def addExpense():
    print("\n<--------GİDER EKLE-------->")

    while True:
        expenseName = input("Gider Adı: ").strip().lower()
        if expenseName == "":
            print(" Gider Adı boş bırakılamaz.")
        else:
            break

    while True:
        expenseAmount_str = input("Gider Tutarı: ").strip()
        try:
            expenseAmount = float(expenseAmount_str)
            if expenseAmount <= 0:
                print("Gider Tutarı pozitif bir sayı olmalıdır.")
            else:
                break
        except ValueError:
            print("Gider Tutarı sadece sayısal bir değer olabilir.")

    while True:
        expenseDate = input(
            "Gider Tarihi (YYYY/MM/DD): ").strip()
        try:
            datetime.datetime.strptime(expenseDate, '%Y/%m/%d')
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatını kullanın.")

    expenseDesc = input("Gider Açıklaması: ").strip()

    expenseCat = moduleProcces.selectCategory("expense")
    addExpenseProcces(expenseName, expenseAmount,
                     expenseDate, expenseDesc, expenseCat)


def addExpenseProcces(xpName, xpAmount, xpDate, xpDesc, xpCat):
    try:
        expenses = utilts.jsonRead("expenses.json")
    except:
        print("Dosya Bulunamadı.")
        expenses = []
    actvUser = users.active_user

    # for expense in expenses:
    #     if actvUser["userId"] and expense["expenseName"] == xpName and expense["expenseAmount"] == xpAmount and expense["expenseDate"] == xpDate and expense["expenseDesc"] == xpDesc and expense["expenseCategory"] == xpCat:
    #         print("Bu Gider işlemi Zaten Kayıtlı")
    #         return main.expense()
    expenseId = utilts.uniqeId()
    while True:
        controlId = utilts.uniqeCheck(expenses, "expenseId", expenseId)
        if controlId == True:
            expenseId = utilts.uniqeId()
        else:
            break
    data = {
        "expenseId": expenseId,
        "userId": actvUser["userId"],
        "expenseName": xpName,
        "expenseAmount": xpAmount,
        "expenseDate": xpDate,
        "expenseDesc": xpDesc,
        "expenseCat": xpCat
    }

    expenses.append(data)
    utilts.jsonWrite(expenses, "expenses.json")
    print("Gider Başarıyla KAydedildi")
    return main.expense()


def updateExpense():
    print("\n<--------GİDER DÜZENLE-------->")
    expenseList, data = listExpense()
    selectedId = None
    if expenseList == True:
        while True:
            select = input(
                "Güncellemek İstediğiniz Giderin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Gider Seçilmedi")
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["expenseId"]
                print(f"{data[index]["expenseName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")

    updateTable = PrettyTable()
    updateTable.field_names = [
        "Gider Adı", "Gider Tutarı", "Gider Tarihi", "Gider Açıklaması", "Gider Kategiorisi"]

    updateTable.add_row([data[index]["expenseName"], data[index]["expenseAmount"],
                        data[index]["expenseDate"], data[index]["expenseDesc"], data[index]["expenseCat"]])
    updateTable.add_autoindex("No")
    print("\n<--------GÜNCELLENİLECEK GİDER-------->")
    print(updateTable)

    while True:
        expenseName = input("Gider Adı: ").strip().lower()
        if expenseName == "":
            print(" Gider Adı boş bırakılamaz.")
            return
        else:
            break

    while True:
        expenseAmount_str = input("Gider Tutarı: ").strip()
        try:
            expenseAmount = float(expenseAmount_str)
            if expenseAmount <= 0:
                print("Gider Tutarı pozitif bir sayı olmalıdır.")
                return
            else:
                break
        except ValueError:
            print("Gider Tutarı sadece sayısal bir değer olabilir.")

    while True:
        expenseDate = input(
            "Gider Tarihi (YYYY/MM/DD): ").strip()
        try:
            datetime.datetime.strptime(expenseDate, '%Y/%m/%d')
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY/MM/DD formatını kullanın.")
            return

    expenseDesc = input("Gider Açıklaması: ").strip()
    while True:
        catQest = input(
            "KategoriYİ Değiştirecek Misiniz (Y/N)? ").strip().lower()
        if catQest == "y":
            expenseCat = moduleProcces.selectCategory("expense")
            break
        elif catQest == "n":
            expenseCat = data[index]["expenseCat"]
            break
        else:
            print("Lütfen Geçerli bir Değer Giriniz")
            return

    updateProcces(selectedId, expenseName, expenseAmount,
                  expenseDate, expenseDesc, expenseCat)


def updateProcces(xpId, xpName, xpAmount, xpDate, xpDesc, xpCat):
    expenses = utilts.jsonRead("expenses.json")
    actvUser = users.active_user
    for xp in expenses:
        if xp["expenseId"] == xpId:
                xp["expenseName"] = xpName
                xp["expenseAmount"] = xpAmount
                xp["expenseDate"] = xpDate
                xp["expenseDesc"] = xpDesc
                xp["expenseCat"] = xpCat
                utilts.jsonWrite(expenses, "expenses.json")
                print("Gider Güncellendi")
                return main.expense()
        
    print("Gider Bulunamadı")



def removeExpense():
    print("\n<--------GİDER SİL-------->")
    try:
        expenses = utilts.jsonRead("expenses.json")
    except:
        print("Dosya Bulunamadı.")
        expenses = []
    expenseList, data = listExpense()
    selectedId = None
    if expenseList == True:
        while True:
            select = input(
                "Silmek İstediğiniz Giderin Numarasının Giriniz: ")
            if select == "":
                selectedId = None
                print("Gider Seçilmedi")
            index = int(select) - 1
            if 0 <= index < len(data):
                selectedId = data[index]["expenseId"]
                print(f"{data[index]["expenseName"]} Seçildi")
                break
            else:
                print("Lütfen Geçerli Bir Değer Giriniz.")
    
    for xp in expenses:
        if xp["expenseId"] == selectedId:
            expenses.remove(xp)
            utilts.jsonWrite(expenses, "expenses.json")
            print("Gider Başarılı Şekilde Silindi.")
            return main.expense()
    
    print("Gider Bulunamadı/Silinemedi")

def listExpense():
    actvUser = users.active_user
    myList = utilts.jsonRead("expenses.json")
    data = [
        x for x in myList
        if x["userId"] == actvUser["userId"]
    ]
    if data:
        dataTable = PrettyTable()
        dataTable.field_names = [
            "Gider Adı", "Gider Tutarı", "Gider Tarihi", "Gider Açıklaması", "Gider Kategiorisi"]
        for dt in data:
            dataTable.add_row([dt["expenseName"], dt["expenseAmount"],
                              dt["expenseDate"], dt["expenseDesc"], dt["expenseCat"]])
        dataTable.add_autoindex("No")
        print(dataTable)
        return True, data
    else:
        print("Mevctut Gider Listesi Bulunmamaktadır.")

def listAllExpense():
    print("\n<--------GİDER LİSTELE-------->")
    listExpense()
    main.expense()    