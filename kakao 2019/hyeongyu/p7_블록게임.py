# 가능한 블록들의 집합. 블록의 가장 상단을 (0,0)이라 할 때 나머지 블록의 상대 좌표 (y축, x축)으로 기술
# 이 블록이 감싸는 넓이 6의 직사각형에서 블록으로 채워진 부분을 0번 인덱스, 빈 부분을 1번 인덱스에 둔다.
possible_blocks = [[[[0, 0], [0, 1], [0, 2], [1, 2]], [[1, 0], [1, 1]]],
                   [[[0, 0], [0, 1], [1, 0], [2, 0]], [[1, 1], [2, 1]]],
                   [[[0, 0], [1, 0], [1, 1], [1, 2]], [[0, 1], [0, 2]]],
                   [[[0, 0], [1, 0], [2, -1], [2, 0]], [[1, -1], [0, -1]]],
                   [[[0, 0], [0, 1], [0, 2], [1, 0]], [[1, 1], [1, 2]]],
                   [[[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 1], [1, 1]]],
                   [[[0, 0], [1, -2], [1, -1], [1, 0]], [[0, -2], [0, -1]]],
                   [[[0, 0], [0, 1], [1, 1], [2, 1]], [[1, 0], [2, 0]]],
                   [[[0, 0], [1, -1], [1, 0], [1, 1]], [[0, -1], [0, 1]]],
                   [[[0, 0], [1, 0], [1, 1], [2, 0]], [[0, 1], [2, 1]]],
                   [[[0, 0], [0, 1], [0, 2], [1, 1]], [[1, 0], [1, 2]]],
                   [[[0, 0], [1, -1], [1, 0], [2, 0]], [[0, -1], [2, -1]]]]

# board[x][y]를 지나는 블록이 위의 배열에서 몇 번째 인덱스에 해당하는 블록인지 찾아낸다.
def get_block(x, y, board):
    global possible_blocks

    pivot = board[x][y]
    block = []
    for i in range(max(0, x - 2), min(len(board), x + 3)):
        for j in range(max(0, y - 2), min(len(board[0]), y + 3)):
            if board[i][j] == pivot:
                block.append([i - x, j - y])
    block.sort()

    for i in range(len(possible_blocks)):
        candidate = possible_blocks[i]
        is_equal = True
        for j in range(4):
            if candidate[0][j][0] != block[j][0] or candidate[0][j][1] != block[j][1]:
                is_equal = False
                break

        if is_equal:
            return i
    return -1

# 현재 블록의 빈 공간들에 대해 보드의 맨 위까지 어떤 다른 블록도 만나지 않고
# 이동할 수 있다면 검은 블록을 떨어뜨려서 채울 수 있다.
def can_fill(block, board):
    for empty_space in block[2]:
        i = block[0] + empty_space[0]
        j = block[1] + empty_space[1]
        while i >= 0 and board[i][j] == 0:
            i -= 1
        if i >= 0:
            return False
    return True

# 직사각형이 되어 채워진 블록을 보드에서 제거한다
def remove_block_id(removed_block_id, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == removed_block_id:
                board[i][j] = 0
    return


def solution(board):
    global possible_blocks
    blocks = {}
    # 보드에 존재하는 블록을 찾아 시작 좌표와 그 타입을 기록한다
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and board[i][j] not in blocks:
                blocks[board[i][j]] = [i, j, get_block(i, j, board)]

    cnt = 0
    while True:
        # 매 시행마다 최소 하나의 블록을 제거해야한다.
        removed_block_id = -1
        # 모든 블록에 대해
        for block_id in blocks:
            block = blocks[block_id]
            # 이 블록을 채울 수 있으면
            if can_fill([block[0], block[1], possible_blocks[block[2]][1]], board):
                # 카운트 하고 제거할 블록의 id를 기록한다.
                cnt += 1
                removed_block_id = block_id
                break

        if removed_block_id == -1:
            return cnt

        # 블록을 제거한다.
        blocks.pop(removed_block_id)
        remove_block_id(removed_block_id, board)