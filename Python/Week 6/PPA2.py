"""
Accept a positive integer as input and print the digits present in it from left to right. 
Each digit should be printed as a lower case word on a separate line. How would you use dictionaries to solve this problem?
"""

numbers = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}

number = [*input()]
for i in number:
    print(numbers[i])


