import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(10)]
        self.player = 'X'
        self.computer = 'O'
    

    def isWinner(self, board, player):
        return ((board[1] == player and board[2] == player and board[3] == player) or
                (board[4] == player and board[5] == player and board[6] == player) or
                (board[7] == player and board[8] == player and board[9] == player) or
                (board[1] == player and board[4] == player and board[7] == player) or
                (board[2] == player and board[5] == player and board[8] == player) or
                (board[3] == player and board[6] == player and board[9] == player) or
                (board[1] == player and board[5] == player and board[9] == player) or
                (board[3] == player and board[5] == player and board[7] == player))
    
    def isBoardFull(self, board):
        if board.count(' ') > 1:
            return False
        else:
            return True
        
    def makeMove(self, board, player, move):
        board[move] = player

    def getBoardCopy(self, board):
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard
    
    def isSpaceFree(self, board, move):
        return board[move] == ' '
    
    def getComputerMove(self, board, computer, player):
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0
        for let in [computer, player]:
            for i in possibleMoves:
                boardCopy = self.getBoardCopy(board)
                self.makeMove(boardCopy, let, i)
                if self.isWinner(boardCopy, let):
                    move = i
                    return move
        cornersOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = self.selectRandom(cornersOpen)
            return move
        if 5 in possibleMoves:
            move = 5
            return move
        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = self.selectRandom(edgesOpen)
        return move
    
    def selectRandom(self, li):
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]
    
    def drawBoard(self, board):
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    def playGame(self):
        print('Welcome to Tic Tac Toe!')
        self.drawBoard(self.board)
        while not(self.isBoardFull(self.board)):
            if not(self.isWinner(self.board, self.computer)):
                self.playerMove()
                self.drawBoard(self.board)
            else:
                print('Sorry, you lose!')
                break
            if not(self.isWinner(self.board, self.player)):
                self.computerMove()
                self.drawBoard(self.board)
            else:
                print('You win!')
                break
        if self.isBoardFull(self.board):
            print('Tie Game!')

    def playerMove(self):
        run = True
        while run:
            move = input('Please select a position to place an \'X\' (1-9): ')
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if self.isSpaceFree(self.board, move):
                        run = False
                        self.makeMove(self.board, self.player, move)
                    else:
                        print('Sorry, this space is occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')

    def computerMove(self):
        possibleMoves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        move = 0
        for let in [self.computer, self.player]:
            for i in possibleMoves:
                boardCopy = self.getBoardCopy(self.board)
                self.makeMove(boardCopy, let, i)
                if self.isWinner(boardCopy, let):
                    move = i
                    return self.makeMove(self.board, self.computer, move)
        cornersOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = self.selectRandom(cornersOpen)
            return self.makeMove(self.board, self.computer, move)
        if 5 in possibleMoves:
            move = 5
            return self.makeMove(self.board, self.computer, move)
        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = self.selectRandom(edgesOpen)
        return self.makeMove(self.board, self.computer, move)
    
    def resetBoard(self):
        self.board = [' ' for x in range(10)]

    def get_current_game(self):
        return self.board
    
    def get_current_player(self):
        return self.player
    


if __name__ == "__main__":
    game = TicTacToe()
    game.playGame()