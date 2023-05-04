class Board:
    def __init__(self, request):
        if not self.BuildObjectFromRequest(request):
             raise Exception("Request does not contain required fields for board!") 
    def BuildObjectFromRequest(self, request):
        required_fields = ["board", "planes", "rows", "cols", "InARow"]
        for field in required_fields:
            if field not in request:
                return False
        self.planes = request["planes"]
        self.rows = request["row"] 
        self.cols = request["cols"]
        self.emptyPiece = request["emptyPiece"]
        self.board = []
        self.moveStack = []
        self.inARow = request["inARow"]
        oldBoard = request["board"]
        counter = 0
        self.possibleMoves = set()
        for i in range(self.planes):
            self.board.append([])
            for j in range(self.rows):
                self.board[i].append([])
                for k in range(self.cols):
                    if(oldBoard[counter] == self.emptyPiece):
                        self.possibleMoves.add((i, j, k))
                    self.board[i][j][k] = chr(oldBoard[counter])
                    counter += 1
        return True
    
    def isEmptyMoveStack(self):
        return len(self.moveStack) == 0
    def isTie(self):
        return len(self.possibleMoves) == 0
    def isWin(self):
        pass
    def getMoveStack(self):
        return tuple(self.moveStack)
        

    def GetPossibleMoves(self):
        return self.possibleMoves
    
    def MakeMove(self, move, player):
        if move not in self.possibleMoves:
            return False
        (plane, row, col) = move
        self.moveStack.append(move)
        self.board[plane][row][col] = player
        self.possibleMoves.discard(move)
        return True
    def UndoMove(self):
        if len(self.moveStack) == 0:
            return None
        move = self.moveStack.pop()
        if move in self.possibleMoves:
            return None
        (plane, row, col) = move
        self.board[plane][row][col] = self.emptyPiece
        self.possibleMoves.add(move)

        
        
    def GetBoard(self):
        return self.board
    
    
    def BuildResponse(self):
        return None

class Move:
    def __init__(self, request):
        if not self.BuildObjectFromRequest(request):
            raise Exception("Request does not contain required fields for move!")    

    def __init__(self, player, plane, row, col):
        self.player = player
        self.plane = plane
        self.row = row
        self.col = col
    def BuildObjectFromRequest(self, request):
        required_fields = ["plane", "player", "row", "col"]
        for field in required_fields:
            if field not in request:
                return False
        self.player = request["player"]
        self.plane = int(request["plane"])
        self.row = int(request["row"])
        self.col = int(request["col"])
        return True
    def BuildResponse(self):
        return {
            "player": str(self.player),
            "plane": str(self.plane),
            "row": str(self.row),
            "col": str(self.col)
        }

class Game:
    def __init__(self):
        pass
    def BuildObjectFromRequest(self):
        pass
    def BuildResponse(self):
        pass

class Tournament:
    def __init__(self):
        pass
    def BuildObjectFromRequest(self):
        pass
    def BuildResponse(self):
        pass
