import requests
from bs4 import BeautifulSoup

FILENAME = 'lab1/employees.txt'
URL = 'https://omgtu.ru/sveden/employees/'

def decorator(input):
    def output(first_letter):
        print('Парсим...')
        input(first_letter[0].upper())
        print('Спарсили!')
    return output

@decorator
def parse(first_letter):    
    page = requests.get(URL)    
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('span', itemprop='fio')
    
    with open(FILENAME, 'w', encoding='utf-8') as file:
        for data in block:   
            surname = data.find('a')     
            if surname:
                surname = surname.text.lstrip()                        
                if surname.startswith(first_letter):
                    file.write(f'{surname}\n')    

if __name__ == '__main__':
    first_letter = input('Введите первую букву вашей фамилии: ')
    parse(first_letter)