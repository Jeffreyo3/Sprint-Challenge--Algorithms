#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) runtime: O(n) - Linear</br>
The `while` loop will run more times as the value of `n` increases.
The number of times the loop will execute will be the same as input size.

b) runtime: O(n^c) - Polynomial</br>
In the best-case scenario, the first `for` loop will run equal to the input of `n`. The number of times the nested the nested `while` loop
needs to run will increase at a greater rate than the increased input
value.

c) runtime: O(n) - Linear </br>
the number of times `bunnyEars(bunnies)` is called with recursion is equal to the input value of `bunnies`.

## Exercise II
I would start by implementing a binary search.

Divide the total floors in half (n/2) and see if the egg breaks.

If the egg doesn't break, we can set a low & high value. Low being (n/2 + 1) and high being n. Then try again at the half way point between low & high floors.

If the egg does break, we can set a low and high value. Low being 1 and high being (n/2 -1). Try again at the half way point between the set low & high floors