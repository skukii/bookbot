def get_num_words(s):
    return len(s.split())
    
def mapping_chars(s):
    helper = s.lower()
    d = {}

    for k in s:
        if k not in d.values():
            d[k] = 1
        else:
            h = d.get(k)
            d.update({k: h+1})
    return d