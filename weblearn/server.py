import grpc
from concurrent import futures
import time

# import the generated classes
import p_calc_pb2
import p_calc_pb2_grpc

# import the original calculator.py
import calc

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(p_calc_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # p_calc_pb2.Number
    def SquareRoot(self, request, context):
        response = p_calc_pb2.Number()
        response.value = calc.square_root(request.value)
        return response

class ConvoServicer(p_calc_pb2_grpc.SuggestReponseServicer):
    
    # calc.get_response is exposed here
    # the request is of the datatype Query
    # teh response is of the datatype Response
    def GetSmartReply(self, request, context):
        response = p_calc_pb2.Response()
        response.replytext = calc.get_response(request.querytext, request.tenant)
        return response

class TrainServicer(p_calc_pb2_grpc.SmartReplyTrainingServicer):
    def BeginTraining(self, request, context):
        response = p_calc_pb2.TrainSmartReply()
        response.status = calc.train_(request.tenant)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
p_calc_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

p_calc_pb2_grpc.add_SuggestReponseServicer_to_server(
    ConvoServicer(), server)

p_calc_pb2_grpc.add_SmartReplyTrainingServicer_to_server(
        TrainServicer(), server)
    
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