def get_num_words(text):
    words = text.split()
    return len(words)

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

def sort_on(dict):
    return dict["num"]

def srtd_char_dict(dict):
    sorted_dict_list = []
    for chr in dict:
        sorted_dict_list.append({"char":chr,"num":dict[chr]})
    sorted_dict_list.sort(reverse=True,key = sort_on)
    return sorted_dict_list