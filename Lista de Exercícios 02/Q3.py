def alphaNumStrings(list):
    #We'll consider the strings it must have both alphabetic and numeric values to be accepted
    newList = []
    for element in list:
        if (element.isalnum() and not element.isalpha() and not element.isnumeric()):
            newList.append(element)

    return newList

lista = ["Nao pode essa", "8461278", "&*&jdjda423", "3ss44qu1p0d3"]
print(alphaNumStrings(lista))