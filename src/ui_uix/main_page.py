
import src.modules.category as ctg
import src.modules.expense as xp
import src.modules.income as ic
import src.modules.report as rp


def main_page():
    print("\n<--------ANASAYFA-------->")
    print("1.Gelir İşlemleri\n2.Gider İşlemleri\n3.Kategori İşlemleri\n4.Rapor İşlemleri\n5.Uygulamadan Çıkış Yap")

    userProcces = input("Yapmak istediğiniz işlemi seçiniz  --->   ").lower()
    if userProcces == "1":
        income()
    elif userProcces == "2":
        expense()
    elif userProcces == "3":
        category()
    elif userProcces == "4":
        report()
    elif userProcces == "5":
        exit()
    else:
        print("Lütfen Geçerli bir Değer Giriniz.")
        return main_page()


def income():
    print("\n<--------GELİR İŞLEMLERİ-------->")
    print("1.Gelir Ekle\n2.Gelir Düzenle\n3.Gelir Sil\n4.Gelir Listele\n5.Geri")
    userChoice = input("Yapmak istediğiniz işlemi seçiniz  --->   ").lower()
    if userChoice == "1":
        return ic.addIncome()
    elif userChoice == "2":
        return ic.updateIncome()
    elif userChoice == "3":
        return ic.removeIncome()
    elif userChoice == "4":
        ic.listAllIncome()
    elif userChoice == "5":
        backToMenu()


def expense():
    print("\n<--------GİDER İŞLEMLERİ-------->")
    print("1.Gelir Ekle\n2.Gelir Düzenle\n3.Gelir Sil\n4.Gelir Listele\n5.Geri")
    userChoice = input("Yapmak istediğiniz işlemi seçiniz  --->   ").lower()
    if userChoice == "1":
        return xp.addExpense()
    elif userChoice == "2":
        return xp.updateExpense()
    elif userChoice == "3":
        return xp.removeExpense()
    elif userChoice == "4":
        xp.listAllExpense()
    elif userChoice == "5":
        backToMenu()

#TAMAMLANDI 00.30
def category():
    print("\n<--------KATEGORİ İŞLEMLERİ-------->")
    print("1.Kategori Ekle\n2.Kategori Düzenle\n3.Kategori Sil\n4.Kategori Listele\n5.Geri")
    userChoice = input("Yapmak istediğiniz işlemi seçiniz  --->   ").lower()
    if userChoice == "1":
        return ctg.addCategory()
    elif userChoice == "2":
        return ctg.updateCategory()
    elif userChoice == "3":
        return ctg.removeCategory()
    elif userChoice == "4":
        ctg.listCategory()
    elif userChoice == "5":
        backToMenu()


def report():
    print("\n<--------RAPOR İŞLEMLERİ-------->")
    print("1.Haftalık Rapor Oluştur\n2.Aylık Rapor Oluştur\n3.Yıllık Rapor Oluştur\n4.Özel Rapor Oluştur\n5.Geri")
    userChoice = input("Yapmak istediğiniz işlemi seçiniz  --->   ").lower()
    if userChoice == "1":
        print("\n<--------HAFTALIK RAPOR İŞLEMLERİ-------->")
        return rp.reportData(7)
    elif userChoice == "2":
        return rp.reportData(30)
    elif userChoice == "3":
        return rp.reportData(365)
    elif userChoice == "4":
        rp.special()
    elif userChoice == "5":
        backToMenu()


def backToMenu():
    main_page()



