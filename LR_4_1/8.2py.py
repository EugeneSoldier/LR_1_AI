#Реализовать класс Bankomat, моделирующий работу банкомата. В классе должны содержаться поля для хранения идентификационного номера банкомата, 
#информации о текущей сумме денег, оставшейся в банкомате, минимальной и максимальной суммах, которые позволяется снять клиенту в один день. 
#Сумма денег представляется полями- номиналами 10-1000 (см. задание 13). Реализовать метод инициализации банкомата, 
#метод загрузки купюр в банкомат и метод снятия определенной суммы денег. Метод снятия денег должен выполнять проверку на корректность 
#снимаемой суммы: она не должна быть меньше минимального значения и не должна превышать максимальное значение. 
# Метод toString()должен преобразовать в строку сумму денег, оставшуюся в банкомате.


import os
import Num2Text

class Bankomat():

    max = 10000
    min = 10

    def __init__(self, Idx = 1, Ostatok = 4578, Min_sum = 10, Max_sum = 10000):
        self.__Idx = Idx         # Id
        self.__Ostatok = Ostatok    #текущая сумма остатка в банкомате
        self.__Min_sum = Min_sum           # минимальная сумма которую можно снять в 1 день
        self.__Max_sum = Max_sum   # максимальная сумма которую можно снять в 1 день

    def get_name(self):
        return self.__Idx

    def set_name(self, n):
        self.__Idx = n

    def get_sumostat(self):
        return self.__Ostatok
    
    def set_sumostat(self, ostat):
        self.__Ostatok = ostat

    def get_minisum(self):
        return self.__Min_sum

    def set_minisum(self, mini):
        self.__Min_sum = mini

    def get_maxisum(self):
        return self.__Max_sum

    def set_maxisum(self, maxi):
        self.__Max_sum = maxi

 #   # Смена владельца счета
 #   def change_name(self):
 #       self.set_name(input("Введите номер банкомата: "))

    # Снятие денег со счета
    def take_money(self):
        print("Сумма на счету:", self.get_sumostat())
        amount_entered = int(input("Введите сумму денег, которые хотите снять:"))
        if amount_entered >= self.get_minisum() and amount_entered <= self.get_maxisum():
            if amount_entered > self.get_sumostat():
                print(f"Вы не можете вывести сумму больше вашего счета: {self.get_sumostat()}")
                self.take_money()
            else:
                self.set_sumostat(self.get_sumostat() - amount_entered)
                print("Отстаток счета:", self.get_sumostat())
        else:
            print(f"Вы не можете вывести сумму больше 10000 и меньше 10")

    # Зачисление денег на счет
    def give_money(self):
        print("Сумма на счету:", self.get_sumostat())
        amount_entered = int(input("Введите сумму денег, которые хотите зачислить:"))
        self.set_sumostat(self.get_sumostat() + amount_entered)
        print("Сумма на счету:", self.get_sumostat())

    # Получение суммы прописью
    def sum_to_text(self):
        
        # 1 - 99
        if 0 < self.get_sumostat() < 100:
            print(Num2Text.do_sta(self.get_sumostat()), "рублей")
        # 100 - 999
        elif 99 < self.get_sumostat() < 1000:
            print(Num2Text.do_tisyachi(self.get_sumostat()), "рублей")
        # 1000 - 9999
        elif 999 < self.get_sumostat() < 10000:
            print(Num2Text.do_ten_tisyachi(self.get_sumostat()), "рублей")
        # 10000 - 99999
        #elif self.get_maxisum() < 100000:
            

    # Вывод на экран
    def display(self):
        print(f"Номер счета: {self.get_name()}")
        print(f"Остаток в банкомате: {self.get_sumostat()}")
        print(f"Максимальная сумма выдачи: {self.get_maxisum()} руб.")
        print(f"Минимальная сумма выдачи: {self.get_minisum()} руб.")

    # Ввод данных
    
if __name__ == '__main__':
    acc = Bankomat()
    while True:
        os.system('cls')
        acc.display()
    
        print("Снять сумму денег со счета >> [1]")
        print("Пополнить счет>> [2]")
        print("Получить сумму прописью (до 9999) >> [3]")
        print("Выход >> [4]")
        
        command = int(input(">>"))
        

        if command == 1:
            acc.take_money() 
            input() 
        elif command == 2:
            acc.give_money()
            input() 
        elif command == 3:
            acc.sum_to_text() 
            input() 
        elif command == 4:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")    
    
    