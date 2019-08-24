import grpc

# import the generated classes
# TODO figure out the VS Code setting to remove the peek alert thing
import hogwords_pb2 as pb2
import hogwords_pb2_grpc as pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
choices_stub = pb2_grpc.SelectFromChoiceStub(channel)

# create a valid request message
selectfromthese = pb2.Query(rid="nirant", clientId="nykaa", msgId="alphabetagamma")

# get a valid response
selected_response = choices_stub.GetChoicesMatch(selectfromthese)

# et voilà
print(selected_response.rid)
print(selected_response.clientId)
print(selected_response.msgId)