board = []


def build_board(dimension):
    position = 1
    for x in range(dimension):
        line = []
        for y in range(dimension):
            line.append(position)
            position += 1
        board.append(line)
    return board


def draw_board():
    for line in board:
        for piece in line:
            print('{:>5}'.format(piece), end="")
        print(' ')


def move(board_size, player):
    while True:
        try:
            player_input = int(input("{} position: ".format(player)))
            for x in range(len(board_size)):
                for y in range(len(board_size)):
                    if board_size[x][y] == player_input:
                        board_size[x][y] = player
                        return board_size
            print("Illegal move!")
        except ValueError:
            print("Illegal move!")
            continue


def all_same(line):
    first = line[0]
    for item in line:
        if item != first:
            return False
    return True


def victory():
    players = []
    # diagonal left->right
    for x in range(len(board)):
        players.append(board[x][x])
    if all_same(players):
        return True

    # diagonal right->left
    players = []
    for x in range(len(board)):
        players.append(board[x][len(board) - 1 - x])
    if all_same(players):
        return True

    # line (e. 1-3)
    for x in range(len(board)):
        line = board[x]
        vic = all_same(line)
        if vic:
            return True

    # column victory
    for column_ix in range(len(board)):
        players = []
        for line_ix in range(len(board)):
            players.append(board[line_ix][column_ix])
        if all_same(players):
            return True

    # no victory
    return False


def no_moves(count, size):
    if count == size:
        return True
    return False


def is_valid_size():
    while True:
        try:
            size = int(input("Input dimension of the board: "))
            if size > 2:
                return size
            else:
                continue
        except ValueError:
            continue


def play():
    size = is_valid_size()
    build_board(size)
    moves = 1
    while True:
        for current_player in ['X', 'O']:
            draw_board()
            move(board, current_player)
            if victory():
                draw_board()
                print("Winner is: {}".format(current_player))
                quit()

            if no_moves(moves, size**2):
                draw_board()
                print("Draw!")
                quit()
            moves += 1


play()