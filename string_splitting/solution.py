import copy

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

def get_domain(nums):
    '''given list of nums return the low to high,  range
    ex: given [1, 4, 7, 2] 
        return [1, 7]
    ex: given [3] 
        return [3, 3]'''
    snums = sorted(nums)
    return (snums[0], snums[-1])

def ranges_intersect(a, b):
    '''given two ranges, return if they intersect
    ex: given [1, 6] and [4, 4]
        returns true
    ex: given [1, 6] and [8, 10]
        returns false'''
    if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
        return True
    else:
        return False

def simplify_ranges(ranges):
    '''given a list of ranges, combine any that intersect
    ex: given [[1, 6], [4, 4], [7, 7], [3, 5]]
        returns [[1, 7]]'''
    sranges = sorted(ranges, key=lambda r: r[0])
    simplified_ranges = []
    a = sranges[0] #   start with first range
    for i, b in enumerate(sranges[1:]):
        is_last_iter = i == (len(sranges) - 2)
        if ranges_intersect(a, b):
            a = (a[0], max(a[1], b[1])) #   combine a and b
        else:
            simplified_ranges.append(a)
            a = b
        if is_last_iter:
            simplified_ranges.append(a)
    return tuple(simplified_ranges)

def find_all(target, l):
    ''' gets all indices where target occurs in list'''
    return [i for i, el in enumerate(l) if el == target]

def solve(input_str):
    letters = list(set(input_str))
    st = list(input_str)
    ranges = []
    for l in letters:
        hits = find_all(l, st)
        hit_range = get_domain(hits)
        ranges.append(hit_range)
    combine_zones = simplify_ranges(ranges)
    base_zones = [(i, i) for i in range(len(st))]
    zones = (*combine_zones, *base_zones)
    simplified_zones = simplify_ranges(zones)
    slices = [input_str[start:end+1] for start, end in simplified_zones]
    return slices

def test(inp, sol):
    result = solve(inp)
    print(f'result: {result}\nanswer: {sol}\npass: {result == sol}\n')

test('abcd', ['a', 'b', 'c', 'd'])
test('foobar', ['f', 'oo', 'b', 'a', 'r'])
test('foobarbaz', ['f', 'oo', 'barba', 'z'])
test('abcdefa', ['abcdefa'])