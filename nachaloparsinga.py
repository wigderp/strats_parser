from urllib import response
import requests
from bs4 import BeautifulSoup as bs

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

my_url = "https://stratz.com/players/176775861?excludeTurbo=true" #эта моё да

print("Какой профиль будем чекать?\nВарианты ответа: autor (профиль создателя), 1 (ваша ссылка)\n ")
userSolution = input()

def autor():
    print("Вот мой профиль, люблю! <3")    
    req = requests.get(my_url, headers=headers)      # ПОХУЙ+ПОХУЙ
    src = req.text
    return src


if userSolution == "1": 
    outer_url = input(print("Введите вашу ссылку на stratz: "))
    req = requests.get(outer_url, headers=headers)           # подключаемся к чужой ссылке
    src = req.text

    if req.status_code == 200:
        print("К сайту подключился, парсю дальше")  

        soup = bs(src, "html.parser")
        globalWinrate = soup.find("span", class_="hitagi__sc-6oal1n-0 fJUbOw").text
        
        print(f"Ваш винрейт: {globalWinrate}")
        
    else:
        print("чет не получилось")
        
    
