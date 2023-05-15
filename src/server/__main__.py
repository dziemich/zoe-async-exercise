import logging
from concurrent import futures

import grpc

from src.consts import server_addr
from src.inference import run_inference
from src.proto.inference_pb2 import InferenceRequest, InferenceResponse
from src.proto.inference_pb2_grpc import add_InferenceServiceServicer_to_server, \
    InferenceServiceServicer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("server")


class InferenceServer(InferenceServiceServicer):
    def infer(self, request: InferenceRequest, _target) -> InferenceResponse:
        logger.info("Received inference request")
        prediction = run_inference(request.image)
        logger.info(f"Responding with prediction: {prediction}")
        return InferenceResponse(prediction=prediction)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_InferenceServiceServicer_to_server(InferenceServer(), server)
    server.add_insecure_port(server_addr)
    server.start()
    logger.info(f"Started gRPC server: {server_addr}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
