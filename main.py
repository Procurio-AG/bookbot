def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    n = num_words(text)
    print_car_rep(srtd_char_dict(char_count(text)),n)

def sort_on(dict):
    return dict["num"]

def srtd_char_dict(dict):
    sorted_dict_list = []
    for chr in dict:
        sorted_dict_list.append({"char":chr,"num":dict[chr]})
    sorted_dict_list.sort(reverse=True,key = sort_on)
    return sorted_dict_list


def print_car_rep(car_d,num):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num} words found in the document\n\n")
    ccd = car_d
    for i in ccd:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
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

def num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()