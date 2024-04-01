# A01705887_EV1_TC2037

## Description
I choose to use the set of words for the Chalkobsa language, the words I had to work with were:
- abra pl. ibar
- adab
- akrab
- alam
- alazor
  
In this case I decided to work with a Deterministic Finite Automata (DFA) to represent the solution to the group of words. I chooose this, after an investigation where I found out, in the JavatPoint website, that DFA can contain multiple final states and it follows one different character path at a time.

## Model of Solution 
I designed my automata in my iPad, and then I checked that it worked fine in a website called “Automaton simulator”. Here is an image showing the model:

![Automata](https://github.com/alexysreyna/A01705887_EV1_TC2037/assets/111073706/59f7733b-b7e4-4a7a-9c9f-aa81bdd8105f)


Additionally, I created a regular expression for the collection of words, which is shown here: ```^a((bra pl.\ ibar)|((d|kr)ab)|(la(m|zor)))$```.

It is also worth mentioning that I checked my RE only accepted the words I had to work with, I did this in a website called “Regex101”, as I did upwards, here is an image showing the process:

<img width="1426" alt="REGEX101" src="https://github.com/alexysreyna/A01705887_EV1_TC2037/assets/111073706/354923d9-0ecd-40fe-b830-9d33ac0a299f">

## Implementation and Test
Within the regexA01705887.py file you can find the code I created based on the RE, I decided to work with this instead of the Automata, for some reasons, being the most important: the fact that I prefer using Python and not Swipl and that according to the website “Medium” a RE describes patterns in strings which was my case, furthermore, they say it is an efficient way to deal with the volume of code and complexity at validation time.

Furthermore, testing is done in the same file by having a set of test_strings that are tested by using the function of match_regex, then the result is shown, which strings were accepted and which were not.

## Analysis
The complexity of my regex code is O(n), because it uses a for in order to check each string and compare it with the ones that are expected based on the RE, and in the code this is the part where we can observe this: 

```
for string in test_strings:
    if match_regex(string):
        print(f"'{string}' matches the RE.")
    else:
        print(f"'{string}' does not match the RE.")
```

Also, as I mentioned in the implementation section, working with a REGEX instead of an Automata has advantages such as the amount of code and the variety of programming languages you can work with. Finally, it is crucial to mention that I used the “Re” library, because after doing some research on Python’s official website and in the Programiz webpage I found it eases a lot the process.

## References
- Javatpoint. (2021). Non-Deterministic Finite Automata. Javatpoint. https://www.javatpoint.com/deterministic-finite-automata
- W3Schools. (n.d.). Python RegEx. W3Schools. https://www.w3schools.com/python/python_regex.asp
- Python Software Foundation. (2024). re — Regular expression operations. Python Documentation. https://docs.python.org/3/library/re.html
- Nagarjoon, B. (2022). What Are Regular Expressions and Why Should You Use Them? Medium. https://medium.com/@nagarjoon.b/what-are-regular-expressions-and-why-should-you-use-them-26140fe52bbe
- Programiz. (n.d.). Python RegEx: Regular Expressions with Python. Programiz. https://www.programiz.com/python-programming/regex
