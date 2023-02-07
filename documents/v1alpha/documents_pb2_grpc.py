# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from documents.v1alpha import documents_pb2 as documents_dot_v1alpha_dot_documents__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DraftsStub(object):
    """=== Draft Service ===

    Drafts service exposes the functionality
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDraft = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/CreateDraft',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.CreateDraftRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.Document.FromString,
                )
        self.DeleteDraft = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/DeleteDraft',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.DeleteDraftRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetDraft = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/GetDraft',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.GetDraftRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.Document.FromString,
                )
        self.UpdateDraftV2 = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/UpdateDraftV2',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.UpdateDraftRequestV2.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListDrafts = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/ListDrafts',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.ListDraftsRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.ListDraftsResponse.FromString,
                )
        self.PublishDraft = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Drafts/PublishDraft',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.PublishDraftRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.Publication.FromString,
                )


class DraftsServicer(object):
    """=== Draft Service ===

    Drafts service exposes the functionality
    """

    def CreateDraft(self, request, context):
        """Creates a new draft with a new permanent document ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDraft(self, request, context):
        """Deletes a draft by its document ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDraft(self, request, context):
        """Gets a single draft if exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDraftV2(self, request, context):
        """Updates a draft using granular update operations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDrafts(self, request, context):
        """List currently stored drafts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishDraft(self, request, context):
        """Publishes a draft. I.e. draft will become a publication, and will no longer appear in drafts section.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DraftsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDraft,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.CreateDraftRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.Document.SerializeToString,
            ),
            'DeleteDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDraft,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.DeleteDraftRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDraft,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.GetDraftRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.Document.SerializeToString,
            ),
            'UpdateDraftV2': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDraftV2,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.UpdateDraftRequestV2.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListDrafts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDrafts,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.ListDraftsRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.ListDraftsResponse.SerializeToString,
            ),
            'PublishDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishDraft,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.PublishDraftRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.Publication.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mintter.documents.v1alpha.Drafts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Drafts(object):
    """=== Draft Service ===

    Drafts service exposes the functionality
    """

    @staticmethod
    def CreateDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/CreateDraft',
            documents_dot_v1alpha_dot_documents__pb2.CreateDraftRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.Document.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/DeleteDraft',
            documents_dot_v1alpha_dot_documents__pb2.DeleteDraftRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/GetDraft',
            documents_dot_v1alpha_dot_documents__pb2.GetDraftRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.Document.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDraftV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/UpdateDraftV2',
            documents_dot_v1alpha_dot_documents__pb2.UpdateDraftRequestV2.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDrafts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/ListDrafts',
            documents_dot_v1alpha_dot_documents__pb2.ListDraftsRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.ListDraftsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Drafts/PublishDraft',
            documents_dot_v1alpha_dot_documents__pb2.PublishDraftRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.Publication.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PublicationsStub(object):
    """=== Publication Service ===

    Publications service provides access to published documents.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPublication = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Publications/GetPublication',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.GetPublicationRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.Publication.FromString,
                )
        self.DeletePublication = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Publications/DeletePublication',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.DeletePublicationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListPublications = channel.unary_unary(
                '/com.mintter.documents.v1alpha.Publications/ListPublications',
                request_serializer=documents_dot_v1alpha_dot_documents__pb2.ListPublicationsRequest.SerializeToString,
                response_deserializer=documents_dot_v1alpha_dot_documents__pb2.ListPublicationsResponse.FromString,
                )


class PublicationsServicer(object):
    """=== Publication Service ===

    Publications service provides access to published documents.
    """

    def GetPublication(self, request, context):
        """Gets a single publication.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePublication(self, request, context):
        """Deletes a publication from the local node. It removes all the patches corresponding to a document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPublications(self, request, context):
        """Lists stored publications. Only the most recent versions show up.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublicationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPublication': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPublication,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.GetPublicationRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.Publication.SerializeToString,
            ),
            'DeletePublication': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePublication,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.DeletePublicationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListPublications': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPublications,
                    request_deserializer=documents_dot_v1alpha_dot_documents__pb2.ListPublicationsRequest.FromString,
                    response_serializer=documents_dot_v1alpha_dot_documents__pb2.ListPublicationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mintter.documents.v1alpha.Publications', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Publications(object):
    """=== Publication Service ===

    Publications service provides access to published documents.
    """

    @staticmethod
    def GetPublication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Publications/GetPublication',
            documents_dot_v1alpha_dot_documents__pb2.GetPublicationRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.Publication.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePublication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Publications/DeletePublication',
            documents_dot_v1alpha_dot_documents__pb2.DeletePublicationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPublications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mintter.documents.v1alpha.Publications/ListPublications',
            documents_dot_v1alpha_dot_documents__pb2.ListPublicationsRequest.SerializeToString,
            documents_dot_v1alpha_dot_documents__pb2.ListPublicationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)