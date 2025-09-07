## Problem Description
From a list of words, we want to find the words with a specific letter at a specific location. 
## Different Solutions
Below, we have three different solutions. One using a list one using a dictionary and one using a generator. When comparing the runtimes we can see that the list and dictionary are the fastest and the generator is the slowest. But what is interesting is what parts of the code are slow. 
- For the list solution, all the runtime happens in the `words_letter_position` function. If we were to call that function again, it would take the same amount of time.
- For the dict solution, most of the runtime is in the `build_dict` function. This means that if we need to call the `words_letter_position` function again, it would be very fast. 
- For the generator solution, exactly the opposite happens. The instantiation of the generator is very fast, but if we want to actually see the value (in this case print them) the runtime is very slow.

``` Python
from timeit import default_timer as timer
import timeit

# source data 
f = open("words.txt", "r")
fileContent = f.read().split()

# 1.1 simple solution with a list
def words_letter_position(data_structure, letter, position):
    result = []
    for word in data_structure:
        current_letter = word[position : position +1]
        if current_letter == letter: 
            result.append(word)

    return result

w = words_letter_position(fileContent, 'a', 5) 
print("results = ", w) 

# test solution 1.1
SETUP_CODE = '''
from __main__ import words_letter_position
f = open("words.txt", "r")
fileContent = f.read().split()
'''
TEST_CODE = '''
w = words_letter_position(fileContent, 'a', 5) 
'''
print("list result:")
print(timeit.timeit(setup=SETUP_CODE,stmt=TEST_CODE,number=100)/100)

# 1.2 dictionary solution
def build_dict(data_structure):
    result = dict()
    for word in data_structure:
        split_word = [x for x in word]
        counter = 0
        for letter in split_word:
            key = (letter, counter)
            if key in result:
                result[key].append(word)
            else:
                result[key] = []
                result[key].append(word)
            counter = counter+1
    return result

def words_letter_position_dict(d, letter, position):
    key = (letter, position)
    result = d[key]
    return result

d = build_dict(fileContent)
w = words_letter_position_dict(d, "a", 5) 
print("results = ", w) 

# test solution 1.2
SETUP_CODE = '''
from __main__ import words_letter_position_dict
from __main__ import build_dict
f = open("words.txt", "r")
fileContent = f.read().split()
d = build_dict(fileContent)
'''
TEST_CODE = '''
w = words_letter_position_dict(d, "a", 5) 
'''
print(timeit.timeit(setup=SETUP_CODE,stmt=TEST_CODE,number=100)/100)

# 1.3 generator solution
def loopGenerator(data_structure, letter, position):
    for word in data_structure:
        current_letter = word[position : position +1]
        if current_letter == letter: 
            yield word
  
gen = loopGenerator(fileContent, 'a', 1)  
for val in gen: 
     print(val, end="\n")

# test solution 1.3
SETUP_CODE = '''
from __main__ import loopGenerator
f = open("words.txt", "r")
fileContent = f.read().split()
'''
TEST_CODE = '''
gen = loopGenerator(fileContent, 'a', 1)
'''
print(timeit.timeit(setup=SETUP_CODE,stmt=TEST_CODE,number=100)/100)

```
