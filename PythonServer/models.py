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
        self.board = []
        self.inARow = request["inARow"]
        oldBoard = request["board"]
        counter = 0
        for i in range(self.planes):
            self.board.append([])
            for j in range(self.rows):
                self.board[i].append([])
                for k in range(self.cols):
                    self.board[i][j][k] = chr(oldBoard[counter])
                    counter += 1
        return True
    
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
