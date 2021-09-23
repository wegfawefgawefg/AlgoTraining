'''
Write a function which partitions a string into groups
where any single, unique character cannot exist in more than one partition
but may exist any number of times in a single partition.

The input string should be validated to not be empty or null.
The input string should be validated to only contain alphanumeric characters,
The input string characters should maintain their initial order.
The output of the function should return an array of partitioned character strings.

Example input => output

'abcd'      => ['a', 'b', 'c', 'd']
'foobar'    => ['f', 'oo', 'b', 'a', 'r']
'foobarbaz' => ['f', 'oo', 'barba', 'z']
'abcdefa'   => ['abcdefa']
'''

'''
generate list of division indices
#   check each one
#   for speedup find relationship between division placements
#   #   presumably this converges to divide and conquer

#   go straight for divide and conquer
"a" - > ["a"]        "a" -> ["a"]
              ["a"] ["a"]
                ["aa"]
"a" - > ["a"]        "b" -> ["b"]
'''


def solve(input_str):
    slices = list(input_str)
    iteration = 0
    shrinks = 1
    while shrinks > 0:
        #print(f"iter: {iteration}")
        shrinks = 0
        #print(slices)

        new_slices = []
        a_v_b_iter = zip(slices, slices[1:])
        for i, (a, b) in enumerate(a_v_b_iter):
            #print(f"{i}: {a} : {b}")
            if set(list(a)).intersection(set(list(b))):
                new_slices.append(a+b)
                next(a_v_b_iter)
                shrinks += 1
            else:
                new_slices.append(a)
                is_last_letter = (len(slices) - shrinks  - 2)
                #print(f"{i} - {is_last_letter}")
                if i == is_last_letter:
                    new_slices.append(b)
        slices = new_slices
        iteration += 1

        #if iteration >= 5:
        #    quit()
    return slices
        



def test(inp, sol):
    result = solve(inp)
    print(f'result: {result}\nanswer: {sol}\npass: {result == sol}\n')


test('abcd', ['a', 'b', 'c', 'd'])
test('foobar', ['f', 'oo', 'b', 'a', 'r'])
test('foobarbaz', ['f', 'oo', 'barba', 'z'])
test('abcdefa', ['abcdefa'])