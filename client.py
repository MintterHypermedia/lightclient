#!/usr/bin/env python3

import daemon_pb2
import daemon_pb2_grpc
import networking_pb2
import networking_pb2_grpc
import documents_pb2
import documents_pb2_grpc
import p2p_pb2
import p2p_pb2_grpc
import accounts_pb2
import accounts_pb2_grpc
import grpc
import argparse
import sys

class client():
    def __init__(self, server="localhost:55002"):
        self.__channel = grpc.insecure_channel(server)
        self._daemon = daemon_pb2_grpc.DaemonStub(self.__channel)
        self._p2p = p2p_pb2_grpc.P2PStub(self.__channel)
        self._networking = networking_pb2_grpc.NetworkingStub(self.__channel)
        self._accounts = accounts_pb2_grpc.AccountsStub(self.__channel)
        self._documents = documents_pb2_grpc.PublicationsStub(self.__channel)
    def __del__(self):
        self.__channel.close()

    def forceSync(self, quiet=False):
        try:
            res = self._daemon.ForceSync(daemon_pb2.ForceSyncRequest())
        except Exception as e:
            print("forceSync error: "+str(e))
            return
        if not quiet:
            print("forceSync OK:"+str(res))

    def peerInfo(self, cid, quiet=False):
        try:
            res = self._networking.GetPeerInfo(networking_pb2.GetPeerInfoRequest(peer_id=cid))
        except Exception as e:
            print("peerInfo error: "+str(e))
            return
        if not quiet:
            print("Addresses :"+str(res.addrs))
            print("Account id :"+str(res.account_id))
            print("Status :"+str(res.connection_status))

    def get_publication(self, cid, quiet=False):
        try:
            res = self._documents.GetPublication(documents_pb2.GetPublicationRequest(document_id=cid))
        except Exception as e:
            print("get_publication error: "+str(e))
            return
        if not quiet:
            print("Version :"+str(res.version))
            print("Document :"+str(res.document))
    def list_publications(self, quiet=False):
        try:
            res = self._documents.ListPublications(documents_pb2.ListPublicationsRequest())
        except Exception as e:
            print("list_publications error: "+str(e))
            return
        if not quiet:
            for p in res.publications:
                print("Version :"+str(p.version))
                print("Document :"+str(p.document))
    def register(self, mnemonics, passphrase = "", quiet=False):
        try:
            res = self._daemon.Register(daemon_pb2.RegisterRequest(mnemonic=mnemonics, passphrase=passphrase))
        except Exception as e:
            print("register error: "+str(e))
            return
        if not quiet:
            print("registered account_id :"+str(res.account_id))

    def connect(self, addrs, quiet=False):
        if type(addrs) != list:
            print("addrs must be a list")
            return
        try:
            res = self._networking.Connect(networking_pb2.ConnectRequest(addrs=addrs))
        except Exception as e:
            print("connect error: "+str(e))
            return
        if not quiet:
            print("connect response:"+str(res))

    def account_info(self, acc_id = "", quiet=False):
        try:
            res = self._accounts.GetAccount(accounts_pb2.GetAccountRequest(id=acc_id))
        except Exception as e:
            print("account info error: "+str(e))
            return
        if not quiet:
            if len(res.devices)>0:
                devices={}
                for d in res.devices:
                    address = self.peer_info(d, quiet=True)
                    devices[d]=address
            else:
                devices = "No devices under the account"
            
            print(devices)
    
    def set_alias(self, alias = "",  quiet=False):
        try:
            account = self._accounts.UpdateProfile(accounts_pb2.Profile(alias=alias))
        except Exception as e:
            print("update profile error: "+str(e))
            return
        if not quiet:
            print("new alias: "+str(account.profile.alias))

    def get_profile(self, quiet=False):
        try:
            account = self._accounts.GetAccount(accounts_pb2.GetAccountRequest())
        except Exception as e:
            print("Getting account error: "+str(e))
            return
        if not quiet:
            print("Alias: "+str(account.profile.alias))
            print("Bio: "+str(account.profile.bio))
            print("Email: "+str(account.profile.email))

    def peer_info(self, id, quiet=False):
        try:
            res = self._networking.GetPeerInfo(networking_pb2.GetPeerInfoRequest(peer_id=id))
        except Exception as e:
            print("peer_info error: "+str(e))
            return
        if not quiet:
            print("peer account_id :%s addrs: %s status: %s"%(str(res.account_id), str(res.addrs), str(res.connection_status)))
        else:
            return {"account id": str(res.account_id), "addresses":str(res.addrs), "connection status": str(res.connection_status)}

def main():
    """basic gRPC client that sends commands to a remote gRPC server

    Returns:
        int: return code 0 on success -1 on error
    """
    parser = argparse.ArgumentParser(description='Basic gRPC client that sends commands to a remote gRPC server',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--sync", action="store_true",  help="Forces a sync loop on the server")
    parser.add_argument("--quiet", action="store_true",  help="Suppress output")
    parser.add_argument('--connect', dest='peer_connect', type=str, default=[], metavar='ADDRS', nargs='+',
                        help='connects to the given multiaddresses')
    parser.add_argument('--register', dest='mnemonics', type=str, default=[], metavar='WORDS', nargs='+',
                        help='registers the device under the account taken from the provided mnemonics.')
    parser.add_argument('--account-info', dest = "get_account", action="store_true", 
                        help='gets information from own account.')
    parser.add_argument('--get-profile', dest = "get_profile", action="store_true", 
                        help='gets profile information.')
    parser.add_argument('--list-publications', dest = "list_publications", action="store_true", 
                        help='gets a list of own publications.')
    parser.add_argument('--set-alias', dest = "alias", type=str, metavar='ALIAS',
                        help='sets alias of the device running in SRV.')
    parser.add_argument('--peer-info', dest = "peer_info", type=str, metavar='CID',
                        help='gets information from given peer encoded CID.')
    parser.add_argument('--get-publication', dest = "publication_id", type=str, metavar='CID',
                        help='gets remote publication given its CID.')
    parser.add_argument('--server', dest='server', type=str, default="localhost:55002", metavar='SRV',
                        help='gRPC server addres in the format <IP>:<port>.')


    args = parser.parse_args()

    try:
        my_client = client(args.server)
    except Exception as e:
        print("Could not connect to provided server: "+str(e))
        sys.exit(1)
    if args.sync:
        my_client.forceSync(args.quiet)
    elif args.peer_connect != []:
        my_client.connect(args.peer_connect, args.quiet)
    elif args.peer_info:  
        my_client.peerInfo(args.peer_info, args.quiet)
    elif args.list_publications:  
        my_client.list_publications(args.quiet)
    elif args.publication_id:  
        my_client.get_publication(args.publication_id, args.quiet)
    elif args.mnemonics != []:
        my_client.register(args.mnemonics, quiet=args.quiet)
    elif args.alias:
        my_client.set_alias(alias=args.alias, quiet=args.quiet)
    elif args.get_profile:
        my_client.get_profile(quiet=args.quiet)
    elif args.get_account:
        my_client.account_info(quiet=args.quiet)
    del my_client
    
if __name__ == "__main__":
    main()
