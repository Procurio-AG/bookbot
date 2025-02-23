import sys
from stats import *

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    n = get_num_words(text)
    print_car_rep(srtd_char_dict(char_count(text)),n,book_path)


def print_car_rep(car_d,num,book):
    print(f'''============ BOOKBOT ============
Analyzing book found at {book}...''')
    print(f'''----------- Word Count ----------
Found {num} total words''')
    print(f'''--------- Character Count -------''')
    ccd = car_d
    for i in ccd:
        print(f"{i["char"]}: {i["num"]}")
    print("--- End report ---")

def char_count(text):
    d={}
    text=text.lower()
    for j in text:
        if not(j.isalpha()):
            continue
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    return d

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()