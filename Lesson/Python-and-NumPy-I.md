# Introduction to Python and NumPy, part I

## Sources
This tutorial is based on a combination of [a MATLAB tutorial from Prof. Todd Ehlers (Uni Tübingen)](http://www.geo.uni-tuebingen.de/arbeitsgruppen/mineralogie-geodynamik/geologie-geodynamik/ibm-documentation/matlab-tutorial.html) and the [Software Carpentry group's](http://software-carpentry.org/) lessons on [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/).

## Getting started
1. Since [Anaconda is likely installing in the background[(Anaconda.md)], you should open a second Terminal window by clicking on the Dash Home icon at the top left corner of the screen, typing `terminal` into the search box, and clicking on the Terminal icon. Alternatively, you can right click on the existing Terminal icon and select **New Terminal**.
2. I assume you have also already [downloaded and extracted the lesson data](Data.md), so you can navigate to the `Data` directory to start this lesson.

    ```bash
    $ cd ~/Desktop/Lab-1/Data
    ```
Note the `$` symbol represents the command prompt in the Terminal window.
3. Open a new IPython window.

    ```bash
    ipython
    ```

Now we are ready to start.

## Variables, arithmetic and libraries
We will start our Python lesson by learning a bit of the basic operations you can perform using Python.

1. Python can be used as a simple calculator.

    ```python
    >>> 1 + 1
    2
    >>> 5 * 7
    35
    ```

2. You can use Python for more advanced math by using *functions*. Functions are pieces of code that perform a single action such as printing information to the screen (e.g., the `print()` function). Functions exist for a huge number of operations in Python.

    ```python
    >>> sin(3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'sin' is not defined
    >>> sqrt(4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'sqrt' is not defined
    ```

    Wait, what? Python can't calculate square roots or do basic trigonometry? Of course it can, but we need one more step.

3. The list of basic arithmetic operations that can be done by default in Python is in the table below.

    | Operation      | Symbol | Example syntax | Returned value |
    | -------------- | ------ | ---------------|----------------|
    | Addition       | `+`    | `2 + 2`        | `4`            |
    | Subtraction    | `-`    | `4 + 2`        | `2`            |
    | Multiplication | `*`    | `2 * 3`        | `6`            |
    | Division       | `/`    | `4 / 2`        | `2`            |
    | Exponentiation | `**`   | `2**3`         | `8`            |
For anything more advanced, we need to load a *library*.

    ```python
    >>> import math
    >>> math.sin(3)
    0.1411200080598672
    >>> math.sqrt(4)
    2.0
    ```

A *library* is a group of code items such as functions that are related to one another. Libraries are loaded using `import`. Functions that are part of the library `libraryname` could then be used by typing `libraryname.functionname()`. For example, `sin()` is a function that is part of the `math` library, and used by typing `math.sin()` with some number between the parentheses.
4. Functions can also be combined.

    ```python
    >>> print(math.sqrt(4))
    2.0
    >>> print('The square root of 4 is',math.sqrt(4))
    The square root of 4 is 2.0
    ```

5. *Variables* can be used to store values calculated in expressions.

    ```python
    >>> x = 2 + 2
    >>> print(x)
    4
    >>> y = math.sqrt(x)
    >>> print(y)
    2.0
    ```



## Introducing NumPy
NumPy is a library for Python designed for efficient scientific computing. Here, we'll get a sense of a few things NumPy can do.

1.

0. Why Python and the patient data

1. Analyzing patient data
	0. `cd` to the `python/data` directory and open Python. For Mac users, launch it by typing `pythonw`!
	1. Simple example of math in Python
		1. `1+1`, `5*7`
		2. function examples: `sin(3)`, `sqrt(4)` + why this doesn’t work
		3. `import math` `math.sin(3)` or `math.sqrt(4)` + dotted notation concept (`thing.component`) + functions in libraries
	2. `import numpy` `numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')` + the two parameters and why they are in quotes + a quick review of the screen output (`1.` versus `1.0`, `...`, etc.)
	3. Assignment of single values to variables + must start with a letter and case sensitive + assignment using `=` `weight_kg = 55` `print(weight_kg)` `print(‘weight in pounds:’, 2.2 * weight_kg)`
	4. Changing the assigned value: `weight_kg = 57.5` `print('weight in kilograms now:', weight_kg)` Can print multiple things at once by separating by commas
	5. Variable assignment as “sticky notes” `weight_lb = 2.2 * weight_kg` `print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)` We can now change `weight_kg` and it will not affect `weight_lb`: `weight_kg = 100.0` `print('weight in kilograms is now', weight_kg, 'and weight in pounds is still:', weight_lb` Note this is different from how a spreadsheet works.
	6. Challenge question 1.1
	7. Challenge question 1.2
	6. Can also assign arrays to variables, not just single values `data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')` Note: no screen output, must use `print()` to see the data `print(data)`
	7. Data types: `print(type(data))` *n*-dimensional array created using NumPy
	8. “members” or “attributes” of the data: `print(data.shape)` 60 rows, 40 cols + similarity of dotted notation in libraries, `shape` is a part of `data`
	9. Indexing: `print('first value in data:', data[0, 0])` Index starts at zero, use square brackets `print('middle value in data:', data[30, 20])` Note: `[0, 0]` is the UPPER LEFT, not lower left
	10. Ranges (slicing data): `print(data[0:4, 0:10])` Slice will start a index `0` and go up to, but not include index `4`. `print(data[5:10, 0:10])` No need to explicitly list bounds. Python will default to `0` if no lower bound is given, end of the range if no upper is given `small = data[:3, 36:]` `print('small is:')` `print(small)`
	11. Challenge question 1.3
	11. Arithmetic: Operations occur on all members in an array: `doubledata = data * 2.0` New array with values that are twice those in `data` `print('original:')` `print(data[:3, 36:])` `print('doubledata:')` `print(doubledata[:3, 36:])` Can also do arithmetic with arrays of the same size: `tripledata = doubledata + data` `print('tripledata:')` `print(tripledata[:3, 36:])`
	12. Other operations on arrays: `print(data.mean())` `mean` is a **method** of the array, a function that belongs to it just like the **member** `shape` If variables are nouns, methods are verbs. We need the empty parentheses even when not giving any parameters to make it clear to Python we are using a method (asking it to do something for us). Not needed for member `shape`.
	13. NumPy array methods: Lots of useful ones: `print('maximum inflammation:', data.max())` `print('minimum inflammation:', data.min())` `print('standard deviation:', data.std())`
	14. Partial datasets: Can create temporary arrays with part of a larger array: `patient_0 = data[0, :] # 0 on the first axis, everything on the second` `print('maximum inflammation for patient 0:', patient_0.max())` But we don’t even need to assign `patient_0` `print('maximum inflammation for patient 2:', data[2, :].max())`
	15. Operations across axes slide `print(data.mean(axis=0))` Can check the size of this output `print(data.mean(axis=0).shape)` Looks OK. We have an *N*x1 vector, so this is the average inflammation per day for all 40 patients. Average inflammation per patient across all days: `print(data.mean(axis=1))`
	16. Visualization using `matplotlib` `import matplotlib.pyplot` `image  = matplotlib.pyplot.imshow(data)` `matplotlib.pyplot.show(image)` We get a “heat map” with reds showing higher inflammation
	17. More visualization: Average inflammation over time: `ave_inflammation = data.mean(axis=0)` `ave_plot = matplotlib.pyplot.plot(ave_inflammation)` `matplotlib.pyplot.show(ave_plot)` Expected a sharper rise and shallower fall… Max: `max_plot = matplotlib.pyplot.plot(data.max(axis=0))` `matplotlib.pyplot.show(max_plot)` Min: `min_plot = matplotlib.pyplot.plot(data.min(axis=0))` `matplotlib.pyplot.show(min_plot)` Seems suspicious
	18. Subplots: Probably need to make a Python script file to use this example. Would mean opening a second terminal window, etc. `import numpy` `import matplotlib.pyplot`  `data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')`  `fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))`  `axes1 = fig.add_subplot(1, 3, 1)` `axes2 = fig.add_subplot(1, 3, 2)` `axes3 = fig.add_subplot(1, 3, 3)`  `axes1.set_ylabel('average')` `axes1.plot(data.mean(axis=0))`  `axes2.set_ylabel('max')` `axes2.plot(data.max(axis=0))`  `axes3.set_ylabel('min')` `axes3.plot(data.min(axis=0))`  `fig.tight_layout()`  `matplotlib.pyplot.show(fig)` Lots of new stuff here, probably will skip this…
	19. `import numpy as np`;`import matplotlib.pyplot as plt`

2. Repeating actions with loops
	1. Example about how our plots looked a bit strange and how we might want to make many plots for all of our data to check things out
	2. Example: Looking at each character of a word `word = 'lead'` `print(word[0])` `print(word[1])` `print(word[2])` `print(word[3])` Bad idea:
		1. Doesn’t scale - will take forever for us to print long strings
		2. Fragile - only prints part of longer words, gives errors for shorter `word = 'tin'` `print(word[0])` `print(word[1])` `print(word[2])` `print(word[3])`
	3. Better approach: `word = 'lead'` `for char in word:` `    print(char)` This is shorter and more flexible. Can change word to `oxygen` and it still works.
	4. `for` loops in general: `for variable in collection:` `    do things with variable` `variable` can be anything we like; statement must end with a `:`; stuff inside must be indented; nothing needed to end the loop
	5. Another example: `length = 0` `for vowel in 'aeiou':` `    length = length + 1` `print('There are', length, 'vowels')` Walk through what happens in this loop
	6. Note that like bash, the loop variable is just a variable and exists after the loop has run: `letter = 'z'` `for letter in 'abc':` `    print(letter)` `print('after the loop, letter is', letter)`
	7. Note that finding the length of a string is extremely common, so there is a built-in function for that in Python called `len`: `print(len('aeiou'))` Much faster than our loop above and easier to read
	8. Challenge question 2.1
	9. Challenge question 2.2

3. Storing multiple values in lists
	1. Lists can be used to store many values; built-in to Python (no need to load a library); use square brackets to make lists: `odds = [1, 3, 5, 7]` `print('odds are:', odds)`
	2. Indexing: Can get individual values using indexes: `print('first and last:', odds[0], odds[-1])`
	3. Looping over lists: `for number in odds:` `    print(number)` Can see we get values one at a time
	4. One important difference between lists and character strings: Can change values in lists, not individual characters in a string: `names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name` `print('names is originally:', names)` `names[1] = 'Darwin' # correct the name` `print('final value of names:', names)` versus `name = 'Bell'` `name[0] = 'b'` Mutable versus immutable data types: Immutable: Character strings, numbers Mutable: Lists and arrays
	5. Changing list contents: Appending: `odds.append(11)` `print('odds after adding a value:', odds)` Removing a value: `del odds[0]` `print('odds after removing the first element:', odds)` Reversing a list: `odds.reverse()` `print('odds after reversing:', odds)`
	6. Beware of the nature of lists - they are stored in memory and can have counterintuitive behaviour: `odds = [1, 3, 5, 7]` `primes = odds` `primes += [2]` `print('primes:', primes)` `print('odds:', odds)` Lists are stored in memory, so the variable names are just a reference to the list data. Copying lists: `odds = [1, 3, 5, 7]` `primes = list(odds)` `primes += [2]` `print('primes:', primes)` `print('odds:', odds)` A bit different from variables from lesson 1.
	7. Challenge question 3.1

4. SKIPPING - Analyzing data from multiple files

5. Making choices
	1. Conditional statements - can change behaviour based on certain conditions `num = 37` `if num > 100:` `    print('greater')` `else:` `    print('not greater')` `print('done')` Note again that code within the given condition is indented and the statement ends with a `:` On line 2 the code check the value of `num` and proceeds differently based on the comparison that is made; Figure of this statement
	2. `if`, `else` is common, but `else` is not required `num = 53` `print('before conditional...')` `if num > 100:` `    print('53 is greater than 100')` `print('...after conditional')`
	3. Can also have multiple conditions using `elif`, which is short for `else if`: `num = -3`  `if num > 0:` `    print(num, "is positive")` `elif num == 0:` `    print(num, "is zero")` `else:` `    print(num, "is negative")` Note the usage of the `==` to compare whether a value is equal to another, rather than assigning a value.
	4. Challenge question 5.1
	4. We can also use `and` or `or` to meet multiple conditions: `if (1 > 0) and (-1 > 0):` `    print('both parts are true')` `else:` `    print('one part is not true')` versus `if (1 < 0) or (-1 < 0):` `    print('at least one test is true')`
	5. Checking out the inflammation data
		1. Checking for suspicious maxima: `if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:` `    print('Suspicious looking maxima!')`
		2. Checking for healthy individuals: `elif data.min(axis=0).sum() == 0:` `    print('Minima add up to zero!')`
		3. Make note if the data look OK. `else:` `    print('Seems OK!')`
		4. Challenge question 5.2

6. Creating functions
	1. Often we will want to repeat certain parts of a code for many data files, or to process the many parts of a dataset using the same set of operations. **Functions** are an easy way to accomplish such a task without needing to copy and paste sections of code over and over.
	2. Example function: `def fahr_to_kelvin(temp):` `    return ((temp - 32) * (5/9)) + 273.15` General function setup:
		1. Starts with `def`
		2. Gives function name with any parameters used by the function
		3. First line ends with a `:`
		4. Indent stuff that is part of the function
		5. Ends with the value that should be returned from the function using a `return` statement
	3. How does it work? Same as any other function: `print('freezing point of water:', fahr_to_kelvin(32))` `print('boiling point of water:', fahr_to_kelvin(212))`
	4. The old integer division problem from Python 2 is fixed in Python 3. Division always returns floats! Can use the `//` for integer division, if desired.
	5. Challenge question 6.1
	6. Converting Fahrenheit to Celsius just combines our existing functions: `def fahr_to_celsius(temp):` `	temp_k = fahr_to_kelvin(temp)` `	result = kelvin_to_celsius(temp_k)` `	return result`  `print('freezing point of water in Celsius:', fahr_to_celsius(32.0))`
