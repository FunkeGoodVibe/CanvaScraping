###
from bs4 import BeautifulSoup
import requests
import re

url_base = "https://biblehub.com/niv/{0}/{1}.htm"


def get_input():

    get_book = input("Which book?: ")
    get_book = get_book.lower()
    get_book = get_book.strip()  # remove trailing spaces

    get_chapter = input("Which chapter?: ")
    get_chapter = int(get_chapter)

    return [get_book, get_chapter]


user_response = get_input()
book = user_response[0]
chapter = user_response[1]

intro = "\n{0} {1} bible study questions!:".format(book, chapter)
print(intro.upper(), "\n\n")
get_niv_chapter(book, chapter)

