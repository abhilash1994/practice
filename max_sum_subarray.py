def max_sum_subarray(array):
    print array
    max_ending_here = 0
    max_so_far = 0
    for i in array:
        max_ending_here = max_ending_here + i
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


if __name__ == '__main__':
    n = int(raw_input())
    while n:
        size_of_array = int(raw_input())
        a = []
        string = raw_input()
        string = string.split()
        for i in xrange(size_of_array):
            a.append(int(string[i]))
        print max_sum_subarray(a)
