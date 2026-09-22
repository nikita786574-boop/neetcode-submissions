class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        for i in range(9):
            dictionary = dict()
            m = 0
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                dictionary[board[i][j]] = dictionary.get(board[i][j], 0) + 1
                m = max(m, dictionary[board[i][j]])
                if m > 1:
                    flag=False
        for j in range(9):
            dictionary = dict()
            m = 0
            for i in range(9):
                if not board[i][j].isdigit():
                    continue
                dictionary[board[i][j]] = dictionary.get(board[i][j], 0) + 1
                m = max(m, dictionary[board[i][j]])
                if m > 1:
                    flag=False
        for margin_i in range(3):
            for margin_j in range(3):
                dictionary = dict()
                m = 0
                for i in range(3):
                    for j in range(3):
                        
                        index_i = i + margin_i * 3
                        index_j = j + margin_j * 3
                        if not board[index_i][index_j].isdigit():
                            continue
                        dictionary[board[index_i][index_j]] = dictionary.get(board[index_i][index_j], 0) + 1
                        m = max(m, dictionary[board[index_i][index_j]])
                        if m > 1:
                            flag=False
        return flag