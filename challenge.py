import random as rand
DIM = 4
EXIT_SUCCESS = True

def array_print(test) :
    for line in test :
        print(line)

def array_create() :
    num_set = [num + 1 for num in range(DIM)]
    num_set_array = [[list(num_set) for _ in range(DIM)] for _ in range(DIM)]
    chal = [[0 for _ in range(DIM)] for _ in range(DIM)]

    for row in range(DIM) :
        for col in range(DIM) :
            index = rand.randint(0, len(num_set_array[row][col]) - 1)
            chal[row][col] = num_set_array[row][col][index]

            for across in range(col + 1, DIM) :
                try :
                    num_set_array[row][across].remove(chal[row][col])
                except ValueError :
                    pass

            for down in range(row + 1, DIM) :
                try :
                    num_set_array[down][col].remove(chal[row][col])
                except ValueError :
                    pass

    return chal, EXIT_SUCCESS

def main () :
    rand.seed()

    result = False
    while not result :
        try :
            chal, result = array_create()
        except :
            pass
    
    array_print(chal)

if __name__ == "__main__" :
    main()