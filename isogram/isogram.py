def is_isogram(string):
    string = string.upper().replace("-","").replace(" ","")
    return all(string.count(char) == 1 for char in string)
