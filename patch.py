# This module patches pykmip to support the latest SSL implementation

import kmip.services.kmip_client
import ssl

def _patched_create_socket(self, sock):
   ssl_context = ssl.SSLContext(self.ssl_version)
   ssl_context.verify_mode = self.cert_reqs
   ssl_context.load_verify_locations(self.ca_certs)
   ssl_context.load_cert_chain(self.certfile, self.keyfile)
   self.socket = ssl_context.wrap_socket(
                   sock,
                   server_side=False,
                   do_handshake_on_connect=self.do_handshake_on_connect,
                   suppress_ragged_eofs=self.suppress_ragged_eofs,
                   server_hostname=self.host)
   self.socket.settimeout(self.timeout)

kmip.services.kmip_client.KMIPProxy._create_socket = _patched_create_socket

