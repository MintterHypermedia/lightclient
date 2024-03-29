# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from groups.v1alpha import website_pb2 as groups_dot_v1alpha_dot_website__pb2


class WebsiteStub(object):
    """API service exposed by the website server.
    It's exposed as gRPC over Libp2p.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSiteInfo = channel.unary_unary(
                '/com.mintter.groups.v1alpha.Website/GetSiteInfo',
                request_serializer=groups_dot_v1alpha_dot_website__pb2.GetSiteInfoRequest.SerializeToString,
                response_deserializer=groups_dot_v1alpha_dot_website__pb2.PublicSiteInfo.FromString,
                )
        self.InitializeServer = channel.unary_unary(
                '/com.mintter.groups.v1alpha.Website/InitializeServer',
                request_serializer=groups_dot_v1alpha_dot_website__pb2.InitializeServerRequest.SerializeToString,
                response_deserializer=groups_dot_v1alpha_dot_website__pb2.InitializeServerResponse.FromString,
                )
        self.PublishBlobs = channel.unary_unary(
                '/com.mintter.groups.v1alpha.Website/PublishBlobs',
                request_serializer=groups_dot_v1alpha_dot_website__pb2.PublishBlobsRequest.SerializeToString,
                response_deserializer=groups_dot_v1alpha_dot_website__pb2.PublishBlobsResponse.FromString,
                )


class WebsiteServicer(object):
    """API service exposed by the website server.
    It's exposed as gRPC over Libp2p.
    """

    def GetSiteInfo(self, request, context):
        """Gets the public information about the website.
        This information is also available as JSON over HTTP on `/.well-known/hypermedia-site`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeServer(self, request, context):
        """Initializes the server to become a website for a specific group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishBlobs(self, request, context):
        """Publishes blobs to the website.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WebsiteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSiteInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSiteInfo,
                    request_deserializer=groups_dot_v1alpha_dot_website__pb2.GetSiteInfoRequest.FromString,
                    response_serializer=groups_dot_v1alpha_dot_website__pb2.PublicSiteInfo.SerializeToString,
            ),
            'InitializeServer': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeServer,
                    request_deserializer=groups_dot_v1alpha_dot_website__pb2.InitializeServerRequest.FromString,
                    response_serializer=groups_dot_v1alpha_dot_website__pb2.InitializeServerResponse.SerializeToString,
            ),
            'PublishBlobs': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishBlobs,
                    request_deserializer=groups_dot_v1alpha_dot_website__pb2.PublishBlobsRequest.FromString,
                    response_serializer=groups_dot_v1alpha_dot_website__pb2.PublishBlobsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mintter.groups.v1alpha.Website', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Website(object):
    """API service exposed by the website server.
    It's exposed as gRPC over Libp2p.
    """

    @staticmethod
    def GetSiteInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.groups.v1alpha.Website/GetSiteInfo',
            groups_dot_v1alpha_dot_website__pb2.GetSiteInfoRequest.SerializeToString,
            groups_dot_v1alpha_dot_website__pb2.PublicSiteInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitializeServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.groups.v1alpha.Website/InitializeServer',
            groups_dot_v1alpha_dot_website__pb2.InitializeServerRequest.SerializeToString,
            groups_dot_v1alpha_dot_website__pb2.InitializeServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishBlobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.groups.v1alpha.Website/PublishBlobs',
            groups_dot_v1alpha_dot_website__pb2.PublishBlobsRequest.SerializeToString,
            groups_dot_v1alpha_dot_website__pb2.PublishBlobsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
