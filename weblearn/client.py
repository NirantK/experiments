import grpc

# import the generated classes
import p_calc_pb2
import p_calc_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
calc_stub = p_calc_pb2_grpc.CalculatorStub(channel)
train_stub = p_calc_pb2_grpc.SmartReplyTrainingStub(channel)
convo_stub = p_calc_pb2_grpc.SuggestReponseStub(channel)

# create a valid request message
number = p_calc_pb2.Number(value=24.99)
convo_query = p_calc_pb2.Query(querytext="Hello", tenant="nykaa")
convo_train = p_calc_pb2.TrainSmartReply(tenant="nykaa")

# get a valid response
number_response = calc_stub.SquareRoot(number)
ts_response = train_stub.BeginTraining(convo_train)
convo_response = convo_stub.GetSmartReply(convo_query)

# et voilà
print(number_response.value)
print(ts_response.status)
print(convo_response.replytext)