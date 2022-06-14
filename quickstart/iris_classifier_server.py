from concurrent import futures
import bentoml
import grpc
import iris_classifier_pb2_grpc
import iris_classifier_pb2
import json

# Implement service class
class ClassifyIrisServicer(iris_classifier_pb2_grpc.ClassifyIrisServicer):
    def classify(self, request, context):
        iris_clf = bentoml.sklearn.load_model("iris_clf:latest")
        iris_classifier_input = json.loads(request.arr)
        output_list = iris_clf.predict(iris_classifier_input)
        iris_classifier_result = ','.join(str(v) for v in output_list)
        response = iris_classifier_pb2.outputArray(arr=iris_classifier_result)
        return response
# Create server
server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
iris_classifier_pb2_grpc.add_ClassifyIrisServicer_to_server(ClassifyIrisServicer(),server)
server.add_insecure_port('[::]:8000')

# Start server
server.start()
print("Starting server...")
print("Listening on port 8000...")
server.wait_for_termination()