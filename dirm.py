#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import os


def add_new():
    name = 'lib/' + input("Введите название рассказа: ") + '.data'
    out = open(name, 'w')
    out.write('')
    print("Успешно добавлено!")
    os.system('pause')
    os.system('cls')


#


def select_ex():
    while True:
        title = input("Введите название рассказа: ") + '.data'
        if title in os.listdir(path="lib"):
            name = 'lib/' + title
            while True:
                print(name)
                print("1. Записать информацию")
                print("2. Вывести информацию на экран")
                print("3. Вернуться в главное меню")
                cmd = input("Выберите пункт: ")

                if cmd == "1":
                    os.system('cls')
                    writeInfo(name)
                elif cmd == "2":
                    os.system('cls')
                    showInfo(name)
                elif cmd == "3":
                    os.system('cls')
                    break
            break
        else:
            print("Такого рассказа ещё нет в базе!")
            os.system('pause')
            os.system('cls')
            break


#


def delete():
    name = 'lib/' + input("Введите название рассказа: ") + '.data'
    os.remove(name)
    print("Успешно удалено!")
    os.system('pause')
    os.system('cls')


#


def show():
    print(os.listdir(path="lib"))


#

def writeInfo(name):
    writing = open(name, 'a')
    print(name)
    print("Чтобы выйти из режима записи, введите 'quit'.")
    print('\n')
    while True:
        inp = input()
        if inp == "quit":
            os.system('cls')
            break
        else:
            inp += '\n'
            writing.write(inp)


def showInfo(name):
    while True:
        print(name)
        print("1. Вывести всю информацию")
        print("2. Вывести информацию по конкретному персонажу")
        print("3. Выйти из режима чтения")
        cmd = input("Выберите пункт: ")
        if cmd == "1":
            os.system('cls')
            reading = open(name, 'r')
            lines = reading.readlines()
            for line in lines:
                print(line)
            os.system('pause')
            os.system('cls')
            break
        elif cmd == "2":
            os.system('cls')
            search(name)
        elif cmd == "3":
            os.system('cls')
            break


def search(name):
    character = input("Введите имя персонажа: ")
    os.system('cls')
    reading = open(name, 'r')
    lines = reading.readlines()
    count = 0
    for line in lines:
        if line.find(character) != -1 or line.find(character.capitalize()) != -1:
            count += 1
            print(line)
    if count == 0:
        os.system('cls')
        print("Персонаж не найден. Проверьте имя или его наличие в рассказе")
    os.system('pause')
    os.system('cls')
