import grpc
import example_pb2
import example_pb2_grpc


def run(value1, value2):
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = example_pb2_grpc.MyMegaServiceStub(channel)
		request = example_pb2.Request(value1=value1, value2=value2)
		response = stub.CalculateValue(request)
		print(f'Greeter client received: {response.value}')


if __name__ == '__main__':
	for i in range(1, 100):
		run(i, i + 1)
