import grpc
from concurrent import futures
import time

# import the generated classes
import hogwords_pb2 as pb2 ##nocheck
import hogwords_pb2_grpc as pb2_grpc

# import the core logic for generic string matching
import generic as generic

# create a class to define the server functions
class WebServicer(pb2_grpc.SelectFromChoiceServicer):

    def GetChoicesMatch(self, request, context):
        response = pb2.Response()
        response.rid = request.rid
        response.msgId = request.msgId
        response.clientId = request.clientId
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
pb2_grpc.add_SelectFromChoiceServicer_to_server(
        WebServicer(), server)
    
# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)