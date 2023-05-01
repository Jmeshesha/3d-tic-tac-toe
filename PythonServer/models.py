class Board:
    def __init__(self):
        pass
    def BuildObjectFromRequest(self):
        pass
    def BuildResponse(self):
        pass

class Move:
    def __init__(self, request):
        if not self.BuildObjectFromRequest(request):
            raise Exception("Request does not contain required fields!")    

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
