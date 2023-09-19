"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        previous = foo(x - 2)
        next = foo(x-1)
        return previous + next

    ### TODO
    pass

def longest_run(mylist, key):
    max = 0  
    current = 0 

    for x in mylist:
        if x == key:
            current += 1
        else:
            current = 0  

        if current > max:
            max = current

    return max
    ### TODO
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def longest_run_recursive(mylist, key):

    if key not in mylist:
      return Result(0, 0, 0, False)
    else:
        if mylist[0] == key:
            current = 1
        
            while current < len(mylist) and \
                mylist[current] == key:
                current += 1

            run_result = longest_run_recursive(mylist[current:], key)

            left_size = run_result.left_size
            right_size = current
            longest_size = max(right_size, run_result.longest_size)

            if run_result.is_entire_range and left_size + right_size == len(mylist):
                is_entire_range = True
            else:
                is_entire_range = False

            return Result(left_size, right_size, longest_size, is_entire_range)
    
    result = longest_run_recursive(mylist[1:], key)

    left_size = 0
    right_size = result.left_size + 1
    longest_size = result.longest_size
    is_entire_range = False
    return Result(left_size, right_size, longest_size, is_entire_range)

   ### TODO
pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([12,12,12,8,12,12,0,12,1], 12) == 3
    assert longest_run([12,12,12,8,12,12,0,12,12,12,12], 12) == 4



