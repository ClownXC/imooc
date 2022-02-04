import argparse
import os
import signal
import sys
from concurrent import futures

import grpc
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2_grpc
from user_srv.handler.user import UserServicer
from common.grpc_health.v1 import health_pb2_grpc, health_pb2
from common.grpc_health.v1 import health


def on_exit():
    logger.info("进程中断")
    sys.exit(0)


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        nargs="?",
                        type=str,
                        default="127.0.0.1",
                        help="binding ip"
                        )

    parser.add_argument("--port",
                        nargs="?",
                        type=int,
                        default=50051,
                        help="the listening port"
                        )

    args = parser.parse_args()
    logger.add("logs/user_srv_{time}.log")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    # 注册健康检查
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    server.add_insecure_port(f"{args.ip}:{args.port}")

    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGINT, on_exit)

    logger.info(f"启动服务: {args.ip}:{args.port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

    # logger.debug("test_log")
    # logger.info("test_log")
    # logger.warning("test_log")
    # logger.error("test_log")
    # logger.critical("test_log")
