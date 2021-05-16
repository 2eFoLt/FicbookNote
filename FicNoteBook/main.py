#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import dirm
import os

while True:
    print("1. Добавить новый рассказ")
    print("2. Выбрать существующий рассказ")
    print("3. Удалить существующий рассказ")
    print("4. Показать все существующие рассказы")
    print("5. Выйти из программы")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        os.system('cls')
        dirm.add_new()
    elif cmd == "2":
        os.system('cls')
        dirm.select_ex()
    elif cmd == "3":
        os.system('cls')
        dirm.delete()
    elif cmd == "4":
        os.system('cls')
        dirm.show()
    elif cmd == "5":
        break
    else:
        os.system('cls')
        print("Вы ввели не правильное значение")
