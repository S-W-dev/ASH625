q = input('0 = ENCRYPT, 1 = DECRYPT >> ')
if (q == '0'):
    text = input('Input >> ')
    textFinal = ''

    # makes text into string

    text = str(text)

    # seperates text by char into an array

    text = list(text)

    # changes to numbers
    for i in range (len(text)):
        text[i] = ord(text[i])
        print(text)

    # converts numbers

    for i in range (len(text)):
        text[i] = text[i] + 1;
        if (text[i] > 126):
            text[i] = text[i] - 126 + 31
        print(text)
        
    ## change back to string

    for i in range (len(text)):
        text[i] = chr(text[i])
         
    # prints text

    print(text)

    textFinal = ",".join(text)
    textFinal = textFinal.replace(",","")

    # prints text

    print (textFinal)
else:

            ##Decrytion##
##########################################
    
    text = input('Input >> ')
    textFinal = ''

    # makes text into string

    text = str(text)

    # seperates text by char into an array

    text = list(text)

    # changes to numbers
    for i in range (len(text)):
        text[i] = ord(text[i])
        print(text)

    # converts numbers

    for i in range (len(text)):
        text[i] = text[i] + 1;
        if (text[i] > 126):
            text[i] = text[i] - 126 + 31
        print(text)
        
    ## change back to string

    for i in range (len(text)):
        text[i] = chr(text[i])
         
    # prints text

    print(text)

    textFinal = ",".join(text)
    textFinal = textFinal.replace(",","")

    # prints text

    print (textFinal)
