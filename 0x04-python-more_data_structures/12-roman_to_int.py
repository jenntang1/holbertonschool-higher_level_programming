#!/usr/bin/python3
def roman_to_int(roman_string):
    converted = []
    compare = []
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str):
        for index1 in range(len(roman_string)):
            for key, value in dict.items():
                if roman_string[index1] in key:
                    converted.append(value)
        compare = converted[1:]
        for index2 in range(len(roman_string) - 1):
            if converted[index2] < compare[index2]:
                converted[index2] = converted[index2] * -1
        return sum(converted)
    return 0
