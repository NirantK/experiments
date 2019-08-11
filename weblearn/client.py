import grpc

# import the generated classes
import p_calc_pb2
import p_calc_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = p_calc_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = p_calc_pb2.Number(value=24.99)

# get a valid response
response = stub.SquareRoot(number)

# et voilà
print(response.value)