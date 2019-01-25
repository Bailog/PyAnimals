
def ImportFile():
    dictionary = {}
    with open('darwin.txt', 'r') as f:
        text = f.read()
    # print(text)
    rules = text.split(')\n(')
    # print(rules)
    for rule in rules:
        rule = rule.translate(str.maketrans('', '', '()'))
        text = rule.split('\nТО ')
        # print(text)
        key = text[1].strip()
        ifs = text[0].split('\nИ ')
        ifs2 = []
        for i in ifs:
            ifs2.append(i.strip())
        # print(i)
        dictionary[key] = ifs2
    return dictionary


def ask_user(i, yes, no):
    print(i + '? (y/n)')
    answer = ''
    while answer != "y" and answer != 'n':
        answer = input(answer)
    if answer == 'y':
        print('yes')
        yes.append(i)
    else:
        print('no')
        no.append(i)


def add_animal(dic, name):
    dic[str(name)] = []
    name = 'ЖИВОТНОЕ ' + name.capitalize()
    print('Added', name, 'to diction', dic)


def add_rule(dic, animal, rule):
    try:
        rule = 'ЖИВОТНОЕ ' + rule.capitalize()
        dic[str(animal)].append(rule)
    except KeyError:
        print('Такого животного нет')
    print('Added animal', animal, 'rule', rule, 'to diction', dic)


def remove_animal(dic, animal):



if __name__ == '__main__':
    choice = ''
    diction = ImportFile()
    print('Diction:', diction)
    while choice != '3':
        print('Выбрать пункт:\n1)Добавить животное\n2)Добавить правило\n3)Выполнить программу')
        choice = input(choice)
        if choice == '1':
            animal_name = ''
            print('Назовите животное: ')
            animal_name = input(animal_name)
            add_animal(diction, animal_name)
        elif choice == '2':
            animal_name = ''
            rule_name = ''
            print('Введите животное: ')
            animal_name = input(animal_name)
            print('Введите правило: ')
            rule_name = input(rule_name)
            add_rule(diction, animal_name, rule_name)
        elif choice == '3':
            break
        elif choice != '1' or choice != '2' or choice != '3':
            print('Неверный ввод')

    # hypothesis = ['ЖИВОТНОЕ ПИНГВИН', 'ЖИВОТНОЕ СТРАУС', 'ЖИВОТНОЕ ТИГР', 'ЖИВОТНОЕ ГЕПАРД', 'ЖИВОТНОЕ ЗЕБРА', 'ЖИВОТНОЕ ЖИРАФ']
    hypothesis = []
    for key, value in diction.items():
        hypothesis.append(key)
    print(hypothesis)

    yes = []
    no = []

    for hyp in hypothesis:
        current_hyp = diction[hyp]
        print('current_hyp:', current_hyp)
        hyp_is_wrong = False
        for i in current_hyp:
            print('===================================')
            # i есть в списке yes
            print('i:', i)
            if i in yes:
                print('i есть в списке yes')
                current_hyp.remove(i)
            # i есть в списке no
            elif i in no:
                print('i есть в списке no')
                hyp_is_wrong = True
                break
            # i является ключем словаря
            elif i in diction.keys():
                print('i является ключем словаря')
                current_hyp.remove(i)
                current_hyp = current_hyp + diction[i]
            # Спросить i у пользователя
            else:
                ask_user(i, yes, no)
        if hyp_is_wrong:
            continue

    # Процедура Объясни
    # Процедура добавь Правило
    # Процедура добавь Животное
