import os
from random import randint
import time


def throw_dice(od, do):
    random = randint(od, do)
    return random

def fight(skills, enemy_skills):
    action = "a - atakujesz\nb - czekasz(ws + 5)"
    ws = skills['ws']
    live = skills['live']
    enemy_live = enemy_skills['live']
    os.system('clear')
    print("Zostales zaatakowany! Przeciwnik rzuca sie na ciebie ale w ostatniej chwili")
    print("zdolales uniknac ciosu!")
    time.sleep(3)
    while live > 0 and enemy_live > 0:
        os.system('clear')
        print("Twoj ruch. Wybierz co robisz:")
        s = ""
        while s != "a" and s != "b":
            s = input(action)
        if s == "a":
            print("Atakujesz")
            throw = throw_dice(1, 100)
            print(ws, throw)
            if throw <= ws:
                enemy_live = enemy_live - (skills["attack"] + throw_dice(1, 6) - enemy_skills["defence"])
                print("Trafiles. Zostalo {0:d} zycia.".format(enemy_live))
                ww = skills["ws"]
            else:
                print("Nie trafiles")
                ws = skills["ws"]
        if s == "b":
            print("Zbierasz sily")
            ws += 5
            print("Twoja umiejetnosc walki wzrasta do {0:d}".format(ws))
        time.sleep(2)
        os.system('clear')
        if enemy_live > 0:
            print("Przeciwnik atakuje")
            throw = throw_dice(1, 100)
            if throw <= enemy_skills["ws"]:
                live = live - (enemy_skills["attack"] + throw_dice(1, 6) - skills["defence"])
                print("Trafil. Zostalo {0:d} zycia.".format(live))
            else:
                print("Nie trafil")
            time.sleep(2)
        else:
            print("Przeciwnik pada na ziemie!")

    export_stats(skills, "hero_stats.csv")

    if live <= 0:
        print("Zmarles w okropnych meczarniach!")
        exit()
        # game over
    if enemy_live <= 0:
        print("Jestes dobry w zabijaniu!")
        time.sleep(3)


def export_stats(statistics, filename=None):
    if filename:
        with open(filename, "w") as save:
            stat_to_save = [(element[0]+",")*element[1] for element in statistics.items()]
            stat_to_save[-1] = stat_to_save[-1][:-1]

            for stat in stat_to_save:
                save.write(stat)
