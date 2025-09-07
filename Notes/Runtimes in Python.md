## Wall or Clock time vs. CPU time
Wall time (also known as clock time or wall-clock time) is simply the total time elapsed during the measurement. It’s the time you can measure with a stopwatch. It is the difference between the time at which a program finished its execution and the time at which the program started. **It also includes waiting time for resources**.

CPU Time, on the other hand, refers to the time the CPU was busy processing the program’s instructions. The time spent waiting for other tasks to complete (like I/O operations) is not included in the CPU time. **It does not include the waiting time for resources.**

## Measuring time
1. Measuring wall time with the `time` module:

``` Python
import time

# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
```

2. Measuring CPU time with the `time` module:

``` Python
import time

# get the start time
st = time.process_time()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# get the end time
et = time.process_time()

# get execution time
res = et - st
print('CPU Execution time:', res, 'seconds')
```

3. Using the `timeit` module:

``` Python
# timeit can be really useful if you want to measure the runtime of one function 
import timeit

def my_function():
    return sum(range(1000000))

# Time the function
execution_time = timeit.timeit(my_function, number=100)
print(f"Average Execution Time: {execution_time / 100} seconds")

# You can also use it to measure multiple lines of coding
# data structures
f = open("words.txt", "r")
fileContent = f.read().split()

# 1.1 simple solution
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

print(timeit.timeit(setup=SETUP_CODE,stmt=TEST_CODE,number=100)/100)
```

In this example, it is evident that there is a lot of work necessary to time multiple lines of code with the `timeit` module. It might be better to use a wrapper function or a [[Decorators in Python|decorator]].

4. Using the `timeit` module with a wrapper function:

``` Python
# data structures
f = open("words.txt", "r")
fileContent = f.read().split()

# 1.1 simple solution
def words_letter_position(data_structure, letter, position):
	result = []
	for word in data_structure:
		current_letter = word[position : position +1]
		if current_letter == letter:
			result.append(word)
			
	return result

def wrapper_function(fileContent, a, x)
	w = words_letter_position(fileContent, a, x)
	return w
	
print("results = ", wrapper_function(fileContent, 'a', 5))

execution_time = timeit.timeit(wrapper_function, number=100)
print(f"Average Execution Time: {execution_time / 100} seconds")
```