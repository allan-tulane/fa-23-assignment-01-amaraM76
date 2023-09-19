

# CMPS 2200 Assignment 1

**Name:**____Amara Midouhas_____________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? Yes $2^{n+1}$ will not grow faster than $O(2^n)$. Big O describes the upper bound of the complexity this means f(n) grows at least as fast then g(n) so f(n) needs to be smaller. Also , $2^{n+1}$ belongs to $O(2^n) because the constant attached to $2^{n+1}$ is $2^n$ * $2^1$. Therefore $2^n$ is part of $O(2^n)$ and so $2^{n+1} \in O(2^n)$ is true
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not? No because $2^{2^n}$ grows much faster then  $2^n$ because of the exponent 2. Also, $2^{2^n}$ is not bounded by any fixed constant of $2^n$ since $2^{2^n}$ grows much faster.    
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$? No because the n in $n^{1.01}$ grows much faster than the n in $O(\mathrm{log}^2 n)$ . For example, using the limit equation, if n =100, $100^{1.01}$ / ${log}^2 100$ = 15.76. If n increases, the number will too so it will never reach a finite positive number and keep going towards infinity.
.  
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  Yes it is because $n^{1.01}$ grows much faster then $\Omega(\mathrm{log}^2 n)$ and therefore will be bigger then $\Omega(\mathrm{log}^2 n)$. Omega describes the lower bound of the complexity this means f(n) grows at most as fast then g(n) so f(n) needs to be bigger. So f(n), $n^{1.01}$,  needs to be greater than $\Omega(\mathrm{log}^2 n)$. Therefore n to the power 0f 1.01 will always be larger then any $log^2 n$ and so $n^{1.01}$ belongs to $\Omega(\mathrm{log}^2 n)$
.  
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$? Yes because the $\sqrt{n}$ will always be less then $O((\mathrm{log} n)^3)$ because after you take the log you square it. So doing the $\sqrt{n}$ will make the n grow more slow and be less than taking the ${log} n^3$. So the $\sqrt{n}$ is part of $O((\mathrm{log} n)^3)$.
.  
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  No because the  $\sqrt{n}$ of n will be less then $\Omega((\mathrm{log} n)^3)$. So no matter the n value, the square root of n will grow much slower and be less then the ${log}n^3$ causing it to not belong to  $\Omega((\mathrm{log} n)^3)$
.  


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words? What does this function do, in your own words? This function will take the input value and go to the position before the x input value position of the sequence and will take that number at the position and the previous number at that position and add that together to return the Fibonacci number associated with that particular position of x. For example, if x = 5, it will go up to the position before 5, which is at 4, and the number at position 4 is 3, and then the position twice before 5, which is 3, and the number at position 3 is 2. Therefore, you add 3+2 to give you five, so the Fibonacci number at 5 is 5. Also, if x is 0 or 1, it will return 0 and 1 because the sequence begins with positions 0 and 1 with the numbers 0 and 1.

.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  The work would be O(n) because the total amount of iterations done in the loop of myList is dependent on how long myList is. Since n represents the length of list, it would be O(n). The span would be 0(n) because there is not parallelized computations because each iteration of the loop depends on the iteration prior so the span is linked to the length of the list and the length of the list is n.

.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  The work is O(n) because it depends on the list's length, and the number of calls made depends on the array's length. The span is O(n) because to find the longest run of a key, you have to recursively look at each key before the list, which is why it can't be running parrel. This means runtime depends on the list's length, so it is O(n). 



.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm? The work would be O(n) because the amount of operations to look for a key in a list is the same as the number of elements in the list. Also, since you are comparing each key once and the same operations are being done, when the size of n increases, so does the number of operations done on that list. The span is O(n) because each recursive call depends on the result of the previous call, so it does not execute parrel. The n represents the number of calls, and since it depends on the n of the previous calls, it will be O(n)
.  

.  
.  
.  
.  
.  
.  
.  
.  

