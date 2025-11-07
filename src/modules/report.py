import datetime
import src.ui_uix.main_page as main
import src.core.utilts as utilts
from src.ui_uix.user import users
from prettytable import PrettyTable

from datetime import datetime ,timedelta ,date



def reportData(interval :int):
     end_date = date.today()
     start_date = (end_date - timedelta(days=interval))
     
     incomes = utilts.jsonRead("incomes.json")
     expenses = utilts.jsonRead("expenses.json")
     # categories = utilts.jsonRead("categories.json")
     actvUser = users.active_user
     
     user_incomes = [inc for inc in incomes if inc["userId"] == actvUser["userId"]]
     user_expenses = [exp for exp in expenses if exp["userId"] == actvUser["userId"]]
      
     income_table =PrettyTable()
     expense_table = PrettyTable()
     print("\n<--------GELİRLER-------->")

     income_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     amountCounterIc = 0
     expense_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     
     for ic in incomes:
          incomeDate = datetime.strptime(ic["incomeDate"], '%Y/%m/%d').date()
          if start_date <= incomeDate <= end_date:
               if ic["incomeCat"]:
                    income_table.add_row([ic["incomeName"] ,ic["incomeAmount"] ,ic["incomeDesc"] , ic["incomeCat"] ,ic["incomeDate"]])
                    amountCounterIc = amountCounterIc + ic["incomeAmount"]
               elif ic["incomeCat"] == None:
                    income_table.add_row([ic["incomeName"] ,ic["incomeAmount"] ,ic["incomeDesc"] , "" ,ic["incomeDate"]])
                    amountCounterIc = amountCounterIc + ic["incomeAmount"]
         
     print("\n<--------GELİRLER-------->")
     income_table.add_autoindex("")
     print(income_table)
     
     expense_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     amountCounterXp = 0
     for xp in expenses:
          expenseDate = datetime.strptime(xp["expenseDate"], '%Y/%m/%d').date()
          if start_date <= expenseDate <= end_date:
               if xp["expenseCat"]:
                    expense_table.add_row([xp["expenseName"] ,xp["expenseAmount"] ,xp["expenseDesc"] , xp["expenseCat"] ,xp["expenseDate"]])
                    amountCounterXp = amountCounterXp + xp["expenseAmount"]
               elif xp["expenseCat"] == None:
                    expense_table.add_row([xp["expenseName"] ,xp["expenseAmount"] ,xp["expenseDesc"] , "" ,xp["expenseDate"]])
                    amountCounterXp = amountCounterXp + xp["expenseAmount"]
         
     print("\n<--------GİDERLER-------->")
     expense_table.add_autoindex("")
     print(expense_table)
                    
     amount = amountCounterIc - amountCounterXp
     print(f"Toplam Geliriniz: {amountCounterIc}")
     print(f"Toplam Gideriniz: {amountCounterXp}")
     print(f"Bakiye: {amount}")
     main.report()
               
     


def special():
     print("\n<--------ÖZEL ARALIKTA RAPOR İŞLEMLERİ-------->")
     while True:
        userDate = input(
            "Başlangıç Tarihi (YYYY/MM/DD): ").strip()
        try:
            start_date = datetime.strptime(userDate, '%Y/%m/%d').date()
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY/MM/DD formatını kullanın.")
            return special()
     while True:
        userDate = input(
            "Bitiş Tarihi (YYYY/MM/DD): ").strip()
        try:
            end_date = datetime.strptime(userDate, '%Y/%m/%d').date()
            break
        except ValueError:
            print(" Geçersiz tarih formatı. Lütfen YYYY/MM/DD formatını kullanın.")
            return False
     
     
     
     incomes = utilts.jsonRead("incomes.json")
     expenses = utilts.jsonRead("expenses.json")
     # categories = utilts.jsonRead("categories.json")
     actvUser = users.active_user
     
     user_incomes = [inc for inc in incomes if inc["userId"] == actvUser["userId"]]
     user_expenses = [exp for exp in expenses if exp["userId"] == actvUser["userId"]]
      
     income_table =PrettyTable()
     expense_table = PrettyTable()
     print("\n<--------GELİRLER-------->")

     income_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     amountCounterIc = 0
     expense_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     
     for ic in incomes:
          incomeDate = datetime.strptime(ic["incomeDate"], '%Y/%m/%d').date()
          if start_date <= incomeDate <= end_date:
               if ic["incomeCat"]:
                    income_table.add_row([ic["incomeName"] ,ic["incomeAmount"] ,ic["incomeDesc"] , ic["incomeCat"] ,ic["incomeDate"]])
                    amountCounterIc = amountCounterIc + ic["incomeAmount"]
               elif ic["incomeCat"] == None:
                    income_table.add_row([ic["incomeName"] ,ic["incomeAmount"] ,ic["incomeDesc"] , "" ,ic["incomeDate"]])
                    amountCounterIc = amountCounterIc + ic["incomeAmount"]
         
     print("\n<--------GELİRLER-------->")
     income_table.add_autoindex("")
     print(income_table)
     
     expense_table.field_names =[" Adı" , "Miktarı" , "Açıklaması" ,"Kategori " ,"Tarih"]
     amountCounterXp = 0
     for xp in expenses:
          expenseDate = datetime.strptime(xp["expenseDate"], '%Y/%m/%d').date()
          if start_date <= expenseDate <= end_date:
               if xp["expenseCat"]:
                    expense_table.add_row([xp["expenseName"] ,xp["expenseAmount"] ,xp["expenseDesc"] , xp["expenseCat"] ,xp["expenseDate"]])
                    amountCounterXp = amountCounterXp + xp["expenseAmount"]
               elif xp["expenseCat"] == None:
                    expense_table.add_row([xp["expenseName"] ,xp["expenseAmount"] ,xp["expenseDesc"] , "" ,xp["expenseDate"]])
                    amountCounterXp = amountCounterXp + xp["expenseAmount"]
         
     print("\n<--------GİDERLER-------->")
     expense_table.add_autoindex("")
     print(expense_table)
                    
     amount = amountCounterIc - amountCounterXp
     print(f"Toplam Geliriniz: {amountCounterIc}")
     print(f"Toplam Gideriniz: {amountCounterXp}")
     print(f"Bakiye: {amount}")
     main.report()

