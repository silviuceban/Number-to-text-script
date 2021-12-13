# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string

ones = ('Zero', 'una', 'două', 'trei', 'patru', 'cinci', 'șase', 'șapte', 'opt', 'nouă')

twos = ('zece', 'unsprezece', 'doisprezece', 'treisprezece', 'paisprezece', 'cincisprezece', 'șaisprezece', 'șaptesprezece', 'optsprezece', 'nouăsprezece')

tens = ('douăzeci', 'treizeci', 'patruzeci', 'cincizeci', 'șaizeci', 'șaptezeci', 'optzeci', 'nouăzeci', 'o sută')

suffixes = ('', 'mie', 'milion', 'miliard')

symbols = " !@#$%^&*()-_+={}[]|\:;'<>?,/\""

def process(number, index):
    
    if number=='0':
        return 'Zero'
    
    length = len(number)
    
    if(length > 3):
        return False
    
    number = number.zfill(3)
    words = ''
    
    if (index == -1):
        index = 0
        number = "0" + number[1:]
        words += "întreg și "
    
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    
    
        
    
    
    # words += '' if number[0] == '0' else ones[hdigit]
    if(index==0 or index==1):
        words += '' if number[0] == '0' else ones[hdigit]
    elif (index>=2 and odigit==1 and tdigit==0 and hdigit==0):
        words += "un"
    else:
         words += '' if number[0] == '0' else ones[hdigit]
        
        
    
    if (hdigit == 1):
        words += ' sută '
    elif(hdigit>1):
        words += ' sute '
    else:
        words += ""
    
    if(tdigit > 1 and odigit != 0):
        words += tens[tdigit - 2]
        words += ' și '
        if(index==0 and odigit==1):
            words += "unu"
        elif(index==0 and odigit==2):
            words += "doi"
        elif(index>=2 and odigit ==1):
            words += "unu"
        else:
            words += ones[odigit]

    
    elif (tdigit > 1 and odigit == 0):
        words += tens[tdigit - 2]
       
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
   
    elif(tdigit == 0 and odigit == 1 and index==1):
        words += ones[odigit]
        
    elif(tdigit == 0 and odigit == 1 and hdigit !=0):
        words += "unu"
    elif(tdigit == 0 and odigit == 1 and hdigit ==0 and index==0):
        words += "unu"
    elif(tdigit == 0 and odigit == 2 and hdigit ==0 and index==0):
        words += "doi"
        
    elif(tdigit == 0 and odigit != 1):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    # elif(words =="întreg și "):
    #     words += ''
    elif (index==0):
        words += ""
    else:
        words += ' '
     
    if(not len(words) == 0):
        #words += suffixes[index]
        if(index==0):
            words += suffixes[index]
            
        elif(index==1 and hdigit==0 and tdigit==0 and odigit==1):
            words += suffixes[index]
        elif(index==1 and odigit>1):
            words += "mii"
        elif(index==1 and tdigit>=1):
            words += "mii"
        elif(index==1 and hdigit>=1):
            words += "mii"
            
        elif(index==2 and hdigit==0 and tdigit==0 and odigit==1):
            words += suffixes[index]
        elif(index==2 and odigit>1):
            words += "milioane"
        elif(index==2 and tdigit>=1):
            words += "milioane"
        elif(index==2 and hdigit>=1):
            words += "milioane"
            
        elif(index==3 and hdigit==0 and tdigit==0 and odigit==1):
            words += suffixes[index]
        elif(index==3 and odigit>1):
            words += "miliarde"
        elif(index==3 and tdigit>=1):
            words += "miliarde"
        elif(index==3 and hdigit>=1):
            words += "miliarde"
            
         
        
    return words;
    
def getWords(number):
    
    #number = str(number)
    
    for symbol in symbols:
        if(number.find(symbol) != -1):
            return("Symbols other than \".\" (dot) are not allowed!")
    for digit in number:
        if(string.ascii_letters.find(digit) != -1):
            return("Letters are not allowed. Introduce a number with or without decimals")
    
    
    
    decimal = number.find(".")
    
    length = len(number) #length defined for cheking the compliance with algorithm requirements
    
    if (length>12 and decimal == -1) :
        return 'This program supports up to 12 integer digit numbers, a point and 2 decimal digits.'
    
    if (length>15 and decimal != -1) :
        return 'This program supports up to 12 integer digit numbers, a point and 2 decimal digits.'
    if(len(number[:decimal]) < 1 and decimal != -1):
        return("At least one integer digit is required!")
    
    if(decimal != -1):
        if (len(number[decimal:]) > 3):
            return("Only 2 degimal digits are allowed!")
        elif(len(number[decimal:])==2 and number[decimal+1] == '0'):
            return("Inappropriate format of the number! Null decimals should not be included")
        elif(len(number[decimal:])==2):
            number = number + "0"
    
    
    
    length = len(number) #redefined length for processing the decimal numbers
    
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    if(decimal != -1):
        copy = count
        count += 1
    else:
        copy = count
    words = []
 
    for i in range(length - 1, -1, -3):
        words.append(process(number[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    
    return final_words
# End Main Logic

# Reading number from user
number = str(1.01) # inputul trebuie convertit in STRING aici
print(str(number)+' in words is: ' + getWords(number))