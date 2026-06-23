# FCC Dynamic Programming

These are my python implementation of solutions to the problems in dynamic programming course by Alvin Zablan from [Coderbyte](https://www.youtube.com/channel/UCOJtQcnBnIy4LERo6vkrItg)

The course video can be accessed in [here](https://www.youtube.com/watch?v=oBt53YbR9Kk) 

Two techniques used in the course
- Memoization
- Tabulation

## List of the Problems

### 1. Fibonacci number

Given integer *n*, find fibonacci number *f(n)*

### 2. Grid traveler
Given 2D grid size *m* times *n*, how many ways of travel from top left corner to bottom right corner of the grid with left and down move.

### 3. Can sum

Write a function **canSum(target_number, numbers)** that takes in a **targetSum** and an array of **numbers** as arguments.

The function should return a boolean indicating whether or not it is possible to generate **targetSum** using **numbers** from the array.

### 4. How sum

Write a function **canSum(target_number, numbers)** that takes in a **targetSum** and an array of **numbers** as arguments.

The function should return an array containing any combination of elements that add up to the **targetSum**. If there is no combination that adds up to the **targetSum**, then return null

### 5. Best sum

Write a function **bestSum(target_number, numbers)** that takes in a **targetSum** and an array of **numbers** as arguments.

The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.

if there is a tie for the shortest combination, you may return any one of the shortest combination

### 6. Can construct

Write a function **canConstruct(target, wordBank)** that accept a target string and an array of strings.

The function should return a boolean indicating whether or not the **target** can be constructed by concatenating elements of **wordBank** array

You may reuse elements of **wordBank** as many times as needed

### 7. Count construct

Write a function **countConstruct(target, wordBank)** that accept a target string and an array of strings.

The function should return the number of ways that the **target** can be constructed by concatenating elements of **wordBank** array

You may reuse elements of **wordBank** as many times as needed

### 8. All construct

Write a function **allConstruct(target, wordBank)** that accept a target string and an array of strings.

The function should return a 2D array containing all of the ways that the **target word** can be constructed by concatenating elements of the **wordBank** array. Each element of the 2D array should represent one combination that constructs the **target**

You may reuse elements of **wordBank** as many times as needed