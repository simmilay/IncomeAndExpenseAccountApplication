import src.ui_uix.main_page as mp
from src.ui_uix.user import users
import src.core.utilts as utl


def active_user_query():
    actvUser = users.active_user

    if actvUser is None:
        userProcces()

    else:
        return mp.main_page()


def userProcces():
    print("\n<--------Girşi/Çıkış işlemleri-------->")
    print("1.Giriş Yap\n2.Kayıt Ol\n3.Çıkış")
    userProccess = input(
        "Yapmak istediğiniz işlemi seçiniz (G/K/Ç) --->   ").lower()
    if userProccess == "g" or userProccess == "1":
        users.login()
        if users.userState == "logged":
            return mp.main_page()
        elif users.userState == "wrong name or password":
            return userProcces()
    elif userProccess == "k" or userProccess == "2":
        users.singIn()
        userProcces()
    elif userProccess == "ç" or userProccess == "3":
        exit()
    else:
        print("Lütfen Geçerli bir Değer Giriniz.")
        return userProcces()


active_user_query()
