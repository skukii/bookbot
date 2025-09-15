def get_num_words(s):
    return len(s.split())
    
def mapping_chars(s):
    helper = s.lower()
    d = {}

    for k in s:
        if k.isalpha():
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
    return d