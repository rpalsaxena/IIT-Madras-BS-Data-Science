"""

Accept a sequence of words as input. Create a dictionary named freq whose keys are the distinct words in the sequence. 
The value corresponding to a key (word) should be the frequency of occurrence of the key (word) in the sequence.

(1) You can assume that all words will be in lower case.

(2) You do not have to print the output to the console. This will be the responsibility of the autograder.

"""

string = input().split(',')

freq ={}
for i in string:
    if i in freq.keys():
        freq[i] += 1
    else:
        freq[i] = 1
