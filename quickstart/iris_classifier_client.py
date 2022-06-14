import grpc
import iris_classifier_pb2
import iris_classifier_pb2_grpc
# Define a channel that connects to the server
channel=grpc.insecure_channel('localhost:8000')
# Define a client using the generated stub function
stub=iris_classifier_pb2_grpc.ClassifyIrisStub(channel)

data = "[[2.1, 22.1, 9.8, 0.2]]"
#Send request and print response
query_string=iris_classifier_pb2.inputArray(arr=data)
response=stub.classify(query_string)

print(response)

