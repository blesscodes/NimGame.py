
def create_token_counts(size, token_max):
    if size <= 0:
        return []
    tokenlis = []
    if size >=1:
        for i in range(size):
            tokenlis.append(token_max - i)
        for i in range(len(tokenlis)):
            if tokenlis[i]<= 0:
                tokenlis[i] = 1
        return tokenlis



def is_valid_move(token_counts, row, takes):

    row=str(row)
    takes= str(takes)
    token_counts[0] = token_counts[1]

    if  row.isdigit() or  takes.isdigit() == False:
        return False
    if row.isdigit() and takes.isdigit()== True:
        if int(row) > len(token_counts):
            if int(takes) > 3:
                if takes > token_counts[row]:
                    return False
    else: 
        return True
def update(token_counts, row,takes):
    for i in range(len(token_counts)):
        token_counts[row] = token_counts[row] - takes
        return token_counts



def draw_board(token_count):
    print(' Game Board.')
    print(' ')
    print(' ====================')
    for i, takes in enumerate(token_count, start=1):
        takes = '$'* takes
        print(i, takes)

    print(' ====================')


def is_over(token_counts):
    if sum(token_counts) == 0:
            return True
    else:
        return False
