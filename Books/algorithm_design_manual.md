# Algorithm Design Manual Notes

Algorithm Design Manual by Steven Skiena
Second set of notes. First 

<h2>Chapter 1: Introduction to Algorithm Design</h2>

algorithm: procedure that always produces a correct result

heuristic: procedure that usually does a good job but not guaranteed to be correct

- best way to prove an algorithm is incorrect is to provide a counterexample
- a good counterexample has two important properties
    - verifiability
    - simplicity

<h2>Chapter 2: Algorithm Analysis</h2>

we can compare efficiency of algorithms in a machine-independent way using the RAM model of computation

- each operation is one time step
- count run time by number of steps an algorithm takes

<b>Big Oh Notation</b>

- Big Oh simplifies analysis by allowing us to ignore levels of detail unneeded for analysis
    - can ignore constants and lower level terms
- O(n) represents upper bound of algorithm

<b>Growth Rates and Dominance Relations</b>

- we can make such coarse analysis with Big Oh precisely because of growth rates of common functions
- the common functions are:
    - lg(n)
    - n
    - nlgn
    - n^2
    - 2^n
    - n!
- n! and 2^n become useless very quickly (10 and 30)
- quadratic is usable up until 10000, but then quickly becomes useless
- linear and nlgn useful on one billion items
- lg n works for any imaginable

<h2>Chapter 3: Data Structures</h2>

<b>Contiguous vs Linked Data Structures</b>

- data structures are classified as either contiguous or linked depending on whether they are based on arrays or pointers
    - contiguously allocated structures are single slabs of memory
        - arrays, heaps, hash tables
    - linked data structures are distinct chunks of memory bound together by pointers
        - lists, trees, graphs

arrays:
- each index maps directly to a particular memory address, arbitrary access is constant time
- can have dynamic arrays
    - grow array by 2n when run out of space
    - only loss is insertion is no longer constant time in the worst case

<b>Containers: Stacks and Queues</b>

- stack: LIFO, easily implemented with array
- queue: FIFO, implement with linked list

<b>Dictionary</b>

- access to data item by key
- good implementations with binary trees and hash tables

<b>Priority Queue</b>

- ADT that supports retrieve min/max, delete min/max, insert
- good implementation is with heap

<b>Hashing</b>

- use a hashing function to turn a key into an array index
- collision resolution
    - open addressing
    - chaining
    - both methods use O(n) to initialize an n element hash table
- search, insert and delete can be an expected constant time operation, making it very good for using it to implement a dictionary
- can use hasing to detect duplicates
    - is given document unique within a large database
    - is part of a document plagiarized

<b>Specialized data structures</b>

- String data structures: suffix trees/arrays
- Geometric data structures: kd-trees
- Graphs: adjacency matrixes/adjacency lists

<h2>Chapter 4: Sorting</h2>

- good sorting algorithms run in O(nlogn) time.
- many important problems can use sorting as a first step (note some of these could be faster using hashing)
    - searching
    - closest pair
    - element uniqueness
    - finding the mode, finding how often an element occurs
    - kth largest item

Good sorting algorithms
- heap sort
- merge sort
- quicksort
- distribution sort

<h2>Chapter 5: Divide and Conquer</h2>

- binary search: quintessential divide-and-conquer algorithm

<b>recurrence relations</b>

- equation in which a function is defined in terms of itself
- use the master theorem to solve recurrence relations

<h2>Chapter 11: NP-Completeness</h2>

- Theory of NP Completeness allows us to determine whether or not an efficient algorithm exists for a given problem.
- use reductions between pairs of problems to show that they are equivalent
    - a fast algorithm for one of the problems implies a fast algorithm for the other (and vice versa)

<b>P vs NP</b>

- P: algorithmic problems with a polynomial time algorithm to solve it. i.e P for polynomial time
- NP: problems that can be verified in polynomial time. i.e. NP for not necessarily polynomial time

primary issue in P v NP is whether verification is really easier than initial discovery of a solution
    - answer may seem obvious that verification is easier. e.g. verifying TSP tour has at most weight of k. just add up the weights, which is done in linear time, but to find the tour it takes exponential time
