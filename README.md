# Matching strings: a biological perspective
### Problem 1. ### 
Write two functions, called `countSubStringMatch`
and `countSubStringMatchRecursive` that take two arguments, a `key` string and a `target` string. These functions 
iteratively and recursively count the number of instances of the key in the target string.

You should complete definitions for 
```Python
def countSubStringMatch(target,key): 
```
and
```Python
def countSubStringMatchRecursive (target, key): 
```
### Problem 2. ###
Write the function `subStringMatchExact`. This 
function takes two arguments: a `target` string, 
and a `key` string. It should return a tuple of the 
starting points of matches of the `key` string in 
the `target` string, when indexing starts at 0.  

Complete the definition for 
```Python
def subStringMatchExact(target,key):
```
For example, `subStringMatchExact("atgacatgcacaagtatgcat","atgc")` 

### Problem 3. ### 
Write a function, called which takes three arguments: 
* a tuple representing starting points for the first substring, 
* a tuple representing starting points for the second substring, 
* and the length of the first substring. 

The function should return a tuple of all members (call it n)
of the first tuple for which there is an element in the second 
tuple (call it k) such that *n+m+1 = k*, where *m* is the length 
of the first substring.

Complete the definition 
```Python
def constrainedMatchPair(firstMatch,secondMatch,length):
```

### Problem 4. ### 
Write a function, called which takes two arguments: 
a `target` string and a `key` string. 

This function should return a tuple of all starting 
points of matches of the `key` to the `target`, 
such that at exactly one element of the `key` is 
incorrectly matched to the `target`. 

Complete the definition 
```Python
def subStringMatchExactlyOneSub(target,key): 
```
