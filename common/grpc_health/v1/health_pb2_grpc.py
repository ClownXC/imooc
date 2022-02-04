# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from common.grpc_health.v1 import health_pb2 as grpc__health_dot_v1_dot_health__pb2


class HealthStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary(
            '/grpc.health.v1.Health/Check',
            request_serializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.FromString,
        )
        self.Watch = channel.unary_stream(
            '/grpc.health.v1.Health/Watch',
            request_serializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.FromString,
        )


class HealthServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Check(self, request, context):
        """If the requested service is unknown, the call will fail with status
        NOT_FOUND.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Performs a watch for the serving status of the requested service.
        The server will immediately send back a message indicating the current
        serving status.  It will then subsequently send a new message whenever
        the service's serving status changes.

        If the requested service is unknown when the call is received, the
        server will send a message setting the serving status to
        SERVICE_UNKNOWN but will *not* terminate the call.  If at some
        future point, the serving status of the service becomes known, the
        server will send a new message with the service's serving status.

        If the call terminates with status UNIMPLEMENTED, then clients
        should assume this method is not supported and should not retry the
        call.  If the call terminates with any other status (including OK),
        clients should retry the call with appropriate exponential backoff.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Check': grpc.unary_unary_rpc_method_handler(
            servicer.Check,
            request_deserializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.FromString,
            response_serializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.SerializeToString,
        ),
        'Watch': grpc.unary_stream_rpc_method_handler(
            servicer.Watch,
            request_deserializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.FromString,
            response_serializer=grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc.health.v1.Health', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Health(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Check(request,
              target,
              options=(),
              channel_credentials=None,
              call_credentials=None,
              compression=None,
              wait_for_ready=None,
              timeout=None,
              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.health.v1.Health/Check',
                                             grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.SerializeToString,
                                             grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
              target,
              options=(),
              channel_credentials=None,
              call_credentials=None,
              compression=None,
              wait_for_ready=None,
              timeout=None,
              metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.health.v1.Health/Watch',
                                              grpc__health_dot_v1_dot_health__pb2.HealthCheckRequest.SerializeToString,
                                              grpc__health_dot_v1_dot_health__pb2.HealthCheckResponse.FromString,
                                              options, channel_credentials,
                                              call_credentials, compression, wait_for_ready, timeout, metadata)
