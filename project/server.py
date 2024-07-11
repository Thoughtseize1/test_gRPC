from concurrent import futures
import grpc

import example_pb2, example_pb2_grpc


class MyMegaServiceServicer(example_pb2_grpc.MyMegaServiceServicer):
	def CalculateValue(self, request, context):
		response = example_pb2.Response()
		print(f"Calculating value for: {request.value1} and {request.value2}")
		response.value = request.value1 + request.value2
		return response


def serve():
	print("Server started!")
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	example_pb2_grpc.add_MyMegaServiceServicer_to_server(MyMegaServiceServicer(), server)
	server.add_insecure_port('localhost:50051')
	server.start()
	server.wait_for_termination()


if __name__ == '__main__':
	serve()
