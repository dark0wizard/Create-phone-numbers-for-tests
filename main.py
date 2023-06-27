import re

string = str(input('Enter the phone number in the format +309834784XXX or +Xx74389993x: '))
string = string.upper()


pattern = r"X"  # Pattern to search for characters "X" in a string
matches = re.findall(pattern, string)

numbers = []  # List for storing received numbers


def generate_number(n: int, m: int, prefix=None, result=""):
    '''
    This function outputs combinations of digits and a string with "X"s replaced

    :param n: int - number of available digits (0-9 by default)
    :param m: int - number of "X" characters in the string
    :param prefix: list - the current digit combination
    :param result: str - current string with "X" characters replaced
    '''
    prefix = prefix or []
    if m == 0:  # If all "X" characters are replaced, the base recursion case is reached
        if "X" not in result:  # Check if the result still contains any "X" characters
            write_number(result)
            numbers.append(result)
        return

    for digit in range(n):
        prefix.append(digit)
        if len(prefix) <= len(matches):  # If the length of the digit combination matches the number of characters "X"
            new_result = result.replace("X", str(prefix[-1]), 1)  # Replace the first occurrence of "X" with the current digit
        else:
            new_result = result  # Else, the newline with the "X" characters replaced is left unchanged
        generate_number(n, m - 1, prefix, new_result)  # Recursively call the function for the remaining characters "X"
        prefix.pop()


def write_number(number):
    '''The function opens or creates a file and writes the results'''
    with open("output.txt", "a") as output:
        output.write(str(number) + "\n")


with open("output.txt", "w") as file:  # Deleting old results
    file.write("")

generate_number(10, len(matches), result=string)

question = input('Do you want to have a list of numbers [y/n]: ')
if question.lower() == 'y' or question.lower() == 'yes':
    write_number(f"\nList of your numbers:\n{numbers}")

print('All ready!!!!!!!\nAll numbers are saved in output.txt')
