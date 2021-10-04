def convert(number):
    result = ""
    sounds = {"Pling": 3, "Plang": 5, "Plong": 7}
        
    for index, factor in sounds.items():
        if number % factor == 0:
            result += index
    return result or str(number)
