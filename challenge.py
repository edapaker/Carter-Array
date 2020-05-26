import random as rand
DIM = 4

def array_print(test) :
    for line in test :
        print(line)

def array_create() :
    num_set = [num + 1 for num in range(DIM)]
    num_set_array = [[list(num_set) for _ in range(DIM)] for _ in range(DIM)]
    chal = [[0 for _ in range(DIM)] for _ in range(DIM)]

    for row in range(DIM) :
        for col in range(DIM) :
            chal[row][col] = num_set_array[row][col][rand.randint(0, DIM - 1)]

    return chal

def main () :
    rand.seed()
    chal = array_create()
    array_print(chal)

if __name__ == "__main__" :
    main()