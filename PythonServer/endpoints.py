from models import Move, Board
from nextMove import get_next_move
class EndpointHandler:
    def __init__(self):
        self.endpointDict = {}
    

    def addEndpoint(self, path, endpointObj):
        self.endpointDict[path] = endpointObj
    

    def handle(self, path, requestHeader, requestBody, onError):
        if path in self.endpointDict:
            return self.endpointDict[path].OnRequest(requestHeader, requestBody, onError)

        errorMsg = "{pathname} is invalid.".format(pathname=path)
        onError(404, "Path does not exists", errorMsg)
        return None
        

class PlayNextMoveEndpoint:
    def __init__(self):
        pass

    def OnRequest(self, header, body, onError):
        # try:
        # Example: Move(currPlayer, X-coordinate, Y-corrdinate, Z-coordinate)
        board = Board(body)
        return get_next_move(board, body["heuristic"], body["thinkTime"], chr(body["currPlayer"]), chr(body["opponent"]), body["inARow"], onError).BuildResponse()
        # except Exception as e:
        #     errorMsg = type(e).__name__ + ": " + str(e.args) 
        #     print(errorMsg)
        #     onError(400, "Invalid request", errorMsg)
        

class PlayAIMatchEndpoint:
    def __init__(self):
        pass

    def OnRequest(self, header, body, onError):
        try:
            pass
        except :
            onError(400, "Invalid request", "Request does not contain required fields in body")
        return None

class PlayAITournamentEndpoint:
    def __init__(self):
        pass

    def OnRequest(self, header, body, onError):
        try:
            pass
        except:
            onError(400, "Invalid request", "Request does not contain required fields in body")
        return None