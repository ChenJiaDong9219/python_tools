import sys
import random

def generate_random_n(start, end, n):
    num_list = list(range(start, end+1))
    random.shuffle(num_list)
    return num_list[:n]

if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    n = int(sys.argv[3])
    print(generate_random_n(start, end, n))