HELP = """
help - Напечать справку по программе.
add - добавить задачу в список
show - напечать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []
run = True

while True:
    command = input('Введите команду\n')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date == 'Сегодня': 
          today.append(task)
        elif date == 'Завтра':
          tomorrow.append(task)
        else:
          other.append(task)
        print(f'Задача {task} добавлена')
    elif command == 'show':
        print('Сегодня')
        print(today)      
        print('Завтра')
        print(tomorrow)
        print('Другие')
        print(other)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда!')
        break