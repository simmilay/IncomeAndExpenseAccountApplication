import src.core.utilts as utils


class User:
    def __init__(self):
        self.active_user = None
        self.userState = None

    def userRegistration(self, name, password):
        try: 
            data = utils.jsonRead("users.json")
            
        except :
            print("Dosya Bulunamadı")
            data = []
        
        while True:
            control = utils.uniqeCheck(data, "userName", name)
            if control == True:
                print("Girdiğiniz Kullanıcı adı Kullanılmaktadır.")
                return self.singIn()
            else:
                break

        userId = utils.uniqeId()
        while True:
            controlId = utils.uniqeCheck(data, "userId", f"{userId}")
            if controlId == True:
                userId = utils.uniqeId()
            else:
                break

        newData = {
            "userId": userId,
            "userName": name,
            "password": password
        }
        data.append(newData)
        utils.jsonWrite(data, "users.json")
        self.userState = "registered"
        print(f"Aramıza Hoşgeldin {name}\nKullanıcı Kaydınız oluşturuldu.")
    
    def singIn(self):
            print("\n\n<--------Kayıt Ol-------->")

            userName = input("Bir Kullanıcı Adı Giriniz: ").lower()
            while True:
                password = input("Şifre: ")
                password_confirm = input("Şifre Doğrulama: ")
                if password != password_confirm:
                    print("Şifreleriniz Eşleşmiyor Tekrar Deneyin")
                else:
                    self.userRegistration(userName, password)
                    return True
        
    def logProcces(self, name, password):
        users = utils.jsonRead("users.json")

        if not users:
            print("Kullanıcı verisi yüklenemedi.")
            users = []
            
        
        if self.active_user is None:
            for user in users:
                if user["userName"] == name and user["password"] == password:
                    self.active_user = user
                    print("Giriş başarılı!")
                    self.userState = "logged"
                    return True 

            print("\n\nKullanıcı Adı veya Şife Yanlış")
            self.userState = "wrong name or password"
            return False
        else:
            print("Sistemde şuan aktif bir kullanıcı bulunmaktadır. Önce çıkış yap")  

    def logout(self):
        if self.active_user is not None:
            print(f"Kullanıcı {self.active_user["userName"]} çıkış yapıyor.")
            self.active_user = None
        else:
            print("Lütfen önce giriş yapın")
            
    def login(self):
        print("\n\n<--------Girşi Yap-------->")

        userName = input(" Kullanıcı Adınızı Giriniz: ")
        password = input("Şifre: ")
        
        self.logProcces(userName , password)
        return True
        
        
    
    def userProcces(self):
        print("\n<--------Girşi/Çıkış işlemleri-------->")
        print("1.Giriş Yap\n2.Kayıt Ol\n3.Çıkış")
        userProcces = input(
            "Yapmak istediğiniz işlemi seçiniz (G/K/Ç) --->   ").lower()
        if userProcces == "g" or userProcces == "1":
            return "login"
        elif userProcces == "k" or userProcces == "2":
            return "self.singIn()"
        elif userProcces == "ç" or userProcces == "3":
            exit()
        else:
            print("Lütfen Geçerli bir Değer Giriniz.")
            return userProcces()

        return self.logProcces(userName, password)

   
users = User()

        



