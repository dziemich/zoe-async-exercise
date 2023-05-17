import logging
import time
from typing import Iterator

import grpc
import logging

from src.consts import server_addr
from src.proto.inference_pb2 import InferenceResponse, InferenceRequest
from src.proto.inference_pb2_grpc import InferenceServiceStub

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("client")

channel = grpc.insecure_channel(server_addr)
stub = InferenceServiceStub(channel)
image_bytes = b'aaaaaaaaaa'


def run_client_version0():
    logger.info("Requesting inference")
    response: InferenceResponse = stub.infer(
        InferenceRequest(image=image_bytes)
    )
    logger.info(
        f"Inference successful! Prediction is: {response.prediction}"
    )


def run_client_version1():
    def iterator():
        for i in range(6):
            logger.info("Requesting streamed inference")
            yield InferenceRequest(image=image_bytes)
            time.sleep(1)

    logger.info("Requesting inference")
    response_iterator: Iterator[InferenceResponse] = stub.infer_stream(
        iterator()
    )
    for response in response_iterator:
        logger.info(
            f"Inference successful! Prediction is: {response.prediction}"
        )


if __name__ == "__main__":
    run_client_version1()
