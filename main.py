import time
import random


def input_check():
    while True:
        user_play = input("Введите Камень, Ножницы, Бумага: ")
        if user_play.lower() in ["камень", "ножницы", "бумага"]:
            return user_play


def main():
    v = ["Камень", "Ножницы", "Бумага"]
    while True:
        print("Камень...Ножницы...Бумага")
        time.sleep(1)
        print("Раз...")
        time.sleep(0.5)
        print("Два...")
        time.sleep(0.5)
        print("Три...")
        system_play = random.choice(v)
        user_play = input_check()
        if system_play.lower() == user_play.lower():
            print(f"Ничья! {user_play.lower()}={system_play.lower()}")
        elif system_play.lower() == "камень" and user_play.lower() == "бумага":
            print(f"Вы победили! {user_play.lower()}>{system_play.lower()}")
            break
        elif system_play.lower() == "ножницы" and user_play.lower() == "камень":
            print(f"Вы победили! {user_play.lower()}>{system_play.lower()}")
            break
        elif system_play.lower() == "бумага" and user_play.lower() == "ножницы":
            print(f"Вы победили! {user_play.lower()}>{system_play.lower()}")
            break
        else:
            print(f"Вы проиграли! {user_play.lower()}<{system_play.lower()}")
            break
    input("Нажмите ENTER чтобы выйти")



main()
