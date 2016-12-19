# -*- coding: utf-8 -*-
from colorama import Back, Style, Fore
from django.core.management import call_command


def info_green(text):
    print(Back.GREEN + text + Style.RESET_ALL)
    # print(Back.GREEN + Fore.BLACK + text + Style.RESET_ALL)


def info(text):
    print(Back.BLUE + text + Style.RESET_ALL)


def warning(text):
    print(Fore.YELLOW + Style.DIM + text + Style.RESET_ALL)


def generate_fixtures(filename, app):
    # Ustawienie nazwy pliku.
    info('Przygotowuję fixtures dla app: ' + app + ' w pliku: ' + filename)
    output = open(filename, 'w')
    # Zrzut testowej bazy danych do pliku w formacie json.
    call_command('dumpdata', app, format='json', indent=3, stdout=output)
    output.close()
