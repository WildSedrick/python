import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

data = list(capitals_dict.items())
ran_data = data[random.randint(0, len(data) - 1)]
x = ran_data[0]
y = ran_data[1]
e = 0
while True:
    user_in = input(f'Угадайте столицу штата {x} или введите "Exit" для выхода из программы: ')
    
    if user_in.capitalize() == y:
        print('Согласен')
        break
    
    if e >= 1 and user_in.upper() == 'EXIT':
        print(f'Правильный ответ: {y}')
        print('До свидания')
        break
    
    if user_in.upper() == 'EXIT':
        print('До свидания')
        break
    
    print('Попробуйте еще раз')
    e = e + 1
        
    

