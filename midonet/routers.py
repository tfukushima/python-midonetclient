# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Router(ResourceBase):

    def create(self, tenant_id, name):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        data = {"name": name}
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        return self.cl.get(uri)

    def update(self, router_uuid, name):

        data = {"name": name}
        uri = self.uri + '/' + router_uuid
        return self.cl.put(uri, data)

    # get() and delete() are implemented in the super class

    def link_create(self, router_uuid,
             network_address, network_length,
             port_address, peer_port_address,  peer_router_uuid):

        response, content = self.get(router_uuid)
        uri = content['peerRouters']
        data = {
            "networkAddress": network_address,
            "networkLength": network_length,
            "portAddress": port_address,
            "peerPortAddress": peer_port_address,
            "peerRouterId": peer_router_uuid
            }
        return self.cl.post(uri, data)


    def link_list(self, router_uuid):
        response, content = self.get(router_uuid)
        uri = content['peerRouters']
        return self.cl.get(uri)


    def link_get(self, router_uuid, peer_router_uuid):
        response, content = self.get(router_uuid)
        uri = content['peerRouters'] + '/' + peer_router_uuid
        return self.cl.get(uri)

    def link_delete(self, router_uuid, peer_router_uuid):
        response, content = self.get(router_uuid)
        uri = content['peerRouters'] + '/' + peer_router_uuid
        return self.cl.delete(uri)
