
def string_parser():
    aString = input("Give me a string")
    string_length = len(aString)
    return aString[0] + aString[1] + aString[string_length-2] + aString[string_length-1]




print(string_parser())
