from alphabet import alpha, upper


def encrypt(message, shift):
    output = ""

    # checks each element in dictionary and adds the total sum to find the shift using indexing in "data"
    # the module alphabet contains a dictionary with each letter assigned to its number in the alphabet e.g: b = 2, y = 25
    # if the element is a symbol or number I'm just randomizing a letter for the output
    lower_case, upper_case = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = ".,!?-$%@;"
    numbers = "0123456789"

    for ind, element in enumerate(message):
        if element not in alpha and element not in symbols and element not in upper_case \
        and element not in numbers:
            output += " "
        
        # check if element is a number:
        if element in numbers or element in symbols:
            output += element
            
        # check if element is upper case:
        if element.isupper():
            target = upper[element] + shift
            if target > len(upper_case):
                target = target - 26

            output += upper_case[target - 1]

        if element in alpha:
            target = alpha[element] + shift
            if target > len(alpha):
                target = target - 26

            output += lower_case[target - 1]

    # return a list on encrypted code and original message
    return [output, message]


# checking if word is stored in encryption dictionary to decode:
def decrypt(encryption, word):
    if word in encryption:
        return encryption[word]

    return "Couldn't find word."

