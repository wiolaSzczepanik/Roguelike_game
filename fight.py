import os
from random import randint
import time

#live = 100
#skills = {"atak" : 15, "obrona" : 5, "ww" : 85}

#enemy_live = 100
#enemy_skills = {"atak" : 5, "obrona" : 5, "ww" : 35}

def throw_dice(od, do):
    random = randint(od, do)
    return random

def fight(live, skills, enemy_live, enemy_skills):
    akcja = "a - atak\nb - czekaj(ww + 5)"
    ww = skills["ww"]
    os.system('clear')
    print("Zostales zaatakowany! Przeciwnik rzuca sie na ciebie ale w ostatniej chwili")
    print("zdolales uniknac ciosu!")
    time.sleep(3)
    while live > 0 and enemy_live > 0:
        os.system('clear')
        print("Twoj ruch. Wybierz co robisz:")
        s = ""
        while s != "a" and s != "b":
            s = input(akcja)
        if s == "a":
            print("Atakujesz")
            rzut = throw_dice(1, 100)
            print(ww, rzut)
            if rzut <= ww:
                enemy_live = enemy_live - (skills["atak"] + throw_dice(1, 6) - enemy_skills["obrona"])
                print("Trafiles. Zostalo {0:d} zycia.".format(enemy_live))
                ww = skills["ww"]
            else:
                print("Nie trafiles")
                ww = skills["ww"]
        if s == "b":
            print("Zbierasz sily")
            ww += 5
            print("Twoja umiejetnosc walki wzrasta do {0:d}".format(ww))
        time.sleep(2)
        os.system('clear')
        if enemy_live > 0:
            print("Przeciwnik atakuje")
            rzut = throw_dice(1, 100)
            if rzut <= enemy_skills["ww"]:
                live = live - (enemy_skills["atak"] + throw_dice(1, 6) - skills["obrona"])
                print("Trafil. Zostalo {0:d} zycia.".format(live))
            else:
                print("Nie trafil")
            time.sleep(2)
        else:
            print("Przeciwnik pada na ziemie!")

    if live <= 0:
        print("Zmarles w okropnych meczarniach!")
        # game over
    if enemy_live <= 0:
        print("Jestes dobry w zabijaniu!")
        time.sleep(3)
    return live


#fight(live, skills, 20, enemy_skills)
