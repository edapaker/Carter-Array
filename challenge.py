import random as rand
DIM = 4

def array_print(test) :
    for line in test :
        print(line)

def array_create() :
    num_set = [num + 1 for num in range(DIM)]
    temp_num_set = []
    chal = [[0 for _ in range(DIM)] for _ in range(DIM)]

    # Setting first row
    temp_num_set = list(num_set)
    rand.shuffle(temp_num_set)
    chal[0] = list(temp_num_set)

    # Rest of the rows
    

    return chal

def main () :
    rand.seed()
    chal = array_create()
    array_print(chal)

if __name__ == "__main__" :
    main()