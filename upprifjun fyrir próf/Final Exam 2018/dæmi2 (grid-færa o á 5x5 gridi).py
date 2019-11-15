# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'


def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')

    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move


def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid


def organize(grid):
    for line in (grid):                 ##hérna er ég að taka inn initialize_grid functionið og gerir forloopu sem breytir þessu í string
        print(" ".join(line))             ##hérna er ég að nota .join sem tekur lista og skrifa út sem string

def mover(move, x, y):


    if move == RIGHT:    ## ef inputtið var r þá fer hann hér inn

        x += 1            ## hækka x hnitið um 1
        if x == DIM:      ## og ef x er jafnt og Dimensionið þá núllstillist það aftur
            x = 0
    elif move == DOWN:
        y += 1
        if y == DIM:
            y = 0
    elif move == LEFT:
        x -= 1
        if x < 0:
            x = DIM-1
    elif move == UP:
        y -= 1
        if y < 0:
            y = DIM-1

    return x, y

def new_grid(x, y):
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[y][x] = POSITION  # Current position    ## hérna kemur inn x hnitið sem núna 1 og þá er y = o og x = 1 og skila þessu nýja gridi tilbaka
    return grid


# Main program starts here

def main():
    x = 0
    y = 0


    grid = initialize_grid()
    organize(grid)                  ## hérna er ég búinn að búa til function sem heitir organize function sem tekur in initialize_grid functionið og skrifa út leikinn rétt
    move = get_move()               ## þegar ég er búinn að prenta út leikinn þá skýri ég get_moce functionið sem move


    while move == RIGHT or move == LEFT or move == DOWN or move == UP:   ## hérna skoða ég hvort ég stafurinn sem ég gef move sé r,l,d eða u og ef svo þá heldur hann afram

        x, y = mover(move, x, y)   ##hérna skýri ég mover(move, x,y) sem x, y. semsagt set x sem 0 og y sem 0 og læt það inn í mover functionið
        grid = new_grid(x, y)      ## hendi x hnitinu sem er núna orðið 1 inn í new_grind functionið
        organize(grid)             ## núna hendi ég þessu nýja gridi inn í organize aftur og læt það prenta út nýja gridið þar sem ég er búinn að færa x um 1
        move = get_move()          ## svo spyr ég aftur um move ef það er r, l, d eða u þá keyrir þessi while lykkja aftur






main()
# In your implementation, you have to use the functions and the constants given above