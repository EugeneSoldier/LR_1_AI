def add_person():
    Cout = int(input("Введите количество людей: "))
    i =0 
    while i < Cout:
        name = input("Фамилия и инициалы? ")
        phone = int(input("Номер телефона? "))
        data_birth = input("Дата рождения (day)? ")
        Person = {
        'name': name, 
        'phone': phone, 
        'data_birth': data_birth
        }
        People.append(Person)
        global sorted_people
        if len(People) > 0:       
           sorted_people = sorted(People, key=lambda row: row['data_birth'])
        i+=1

def get_person():
    for idx, Person in enumerate(sorted_people, 1):
        print(
        idx,
        Person.get('name', ''),
        Person.get('phone', ''),
        Person.get('data_birth', 0)
        )
        print("\n----------------------")

def output_person():
    N = int(input("Введите номер телефона: "))
    Index = 0
    i = 0
    while i < len(sorted_people):
        a = sorted_people[i].get('phone')
        if a == N:
            Index = i
            print(sorted_people[Index])
            break
        i+=1
People = []