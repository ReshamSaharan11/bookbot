

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq

def sort_dictionaries(freq):
    my_list = []
    for key, value in freq.items():
        ndict = {"name": key, "num": value}
        my_list.append(ndict)
    my_list.sort(reverse=True,key=sort_on)
    return my_list

def sort_on(items):
    return items["num"];    
         
                       
      
        