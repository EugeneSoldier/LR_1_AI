class Line():
    
    def __init__(self, first = 0, second = 0):
        self.__first = int(first)
        self.__second = int(second)

    def get_first(self):
        return self.__first
    
    def set_first(self, A):
        self.__first = A

    def get_second(self):
        return self.__second

    def set_second(self, B):
        self.__second = B

    def root(self):
        return -(self.__second) / self.__first 
    
    #ввод с клавиатуры
    def read(self):
        self.set_first(int(input("Введите A: ")))
        self.set_second(int(input("Введите B: ")))

    #вывод на экран
    def display(self):
        print(f'Результат: {self.root()}')

if __name__ == '__main__':
    time = Line()
    time.read()
    time.display()
