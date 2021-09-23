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


def solve(input_str):
    # implement logic here
    pass


def test(inp, sol):
    result = solve(inp)
    print(f'result: {result}\nanswer: {sol}\npass: {result == sol}\n')


test('abcd', ['a', 'b', 'c', 'd'])
test('foobar', ['f', 'oo', 'b', 'a', 'r'])
test('foobarbaz', ['f', 'oo', 'barba', 'z'])
test('abcdefa', ['abcdefa'])