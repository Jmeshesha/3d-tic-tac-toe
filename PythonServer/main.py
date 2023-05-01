from http.server import BaseHTTPRequestHandler, HTTPServer
from endpoints import EndpointHandler, PlayNextMoveEndpoint, PlayAIMatchEndpoint, PlayAITournamentEndpoint
import json

def loadEndpoints():
    handler = EndpointHandler()
    handler.addEndpoint('/PlayNextMove', PlayNextMoveEndpoint())
    handler.addEndpoint('/PlayAIMatch', PlayAIMatchEndpoint())
    handler.addEndpoint('/PlayAITournament', PlayAITournamentEndpoint())
    return handler

hostName = "localhost"
serverPort = 8080
endpoints = loadEndpoints()

class MyServer(BaseHTTPRequestHandler):

    def send_success_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        #length = int(self.headers.get('content-length'))
        #requestBody = json.loads(self.rfile.read(length))
        responseBody = endpoints.handle(self.path, self.headers, None, self.send_error)
        
        if responseBody is None:
            self.send_success_header()
            self.wfile.write(json.dumps(responseBody).encode(encoding='utf_8'))

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        requestBody = json.loads(self.rfile.read(length))
        responseBody = endpoints.handle(self.path, self.headers, requestBody, self.send_error)
        
        if responseBody is not None:
            self.send_success_header()
            self.wfile.write(json.dumps(responseBody).encode(encoding='utf_8'))

    

if __name__ == "__main__":   
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")