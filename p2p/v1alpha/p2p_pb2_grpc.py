# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from p2p.v1alpha import p2p_pb2 as p2p_dot_v1alpha_dot_p2p__pb2


class P2PStub(object):
    """Mintter P2P API.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/com.mintter.p2p.v1alpha.P2P/Handshake',
                request_serializer=p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.SerializeToString,
                response_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.FromString,
                )
        self.ListObjects = channel.unary_unary(
                '/com.mintter.p2p.v1alpha.P2P/ListObjects',
                request_serializer=p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsRequest.SerializeToString,
                response_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsResponse.FromString,
                )
        self.RequestInvoice = channel.unary_unary(
                '/com.mintter.p2p.v1alpha.P2P/RequestInvoice',
                request_serializer=p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceRequest.SerializeToString,
                response_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceResponse.FromString,
                )


class P2PServicer(object):
    """Mintter P2P API.
    """

    def Handshake(self, request, context):
        """Handshake gets called whenever two Mintter peers connect to each other.
        No matter who initiates the connect, this will make sure both peers exchange their information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListObjects(self, request, context):
        """Returns list of all the objects authored by the account this peer belongs to.
        Used for syncing objects between peers. Clients are expected to periodically
        use this call to pull the latest objects from the remote peer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestInvoice(self, request, context):
        """Request a peer to issue a lightning BOLT-11 invoice
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_P2PServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.FromString,
                    response_serializer=p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.SerializeToString,
            ),
            'ListObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListObjects,
                    request_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsRequest.FromString,
                    response_serializer=p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsResponse.SerializeToString,
            ),
            'RequestInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestInvoice,
                    request_deserializer=p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceRequest.FromString,
                    response_serializer=p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mintter.p2p.v1alpha.P2P', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class P2P(object):
    """Mintter P2P API.
    """

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.p2p.v1alpha.P2P/Handshake',
            p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.SerializeToString,
            p2p_dot_v1alpha_dot_p2p__pb2.HandshakeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.p2p.v1alpha.P2P/ListObjects',
            p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsRequest.SerializeToString,
            p2p_dot_v1alpha_dot_p2p__pb2.ListObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.p2p.v1alpha.P2P/RequestInvoice',
            p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceRequest.SerializeToString,
            p2p_dot_v1alpha_dot_p2p__pb2.RequestInvoiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)