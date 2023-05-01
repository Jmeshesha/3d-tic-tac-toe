from models import Move
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
        print(body)
        return Move(chr(body["currPlayer"]), 1, 0, 0).BuildResponse()
        

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