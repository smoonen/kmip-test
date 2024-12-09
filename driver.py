# This test script randomly accesses 500 keys from a key server, using a new connection for each access.
# It is intended to function as a lightweight performance test.
# It is dependent on the 'pykmip' package.

import kmip.pie.client
import random
import patch

KMS_HOSTNAME = ''
KMS_PORT     = 5696
KMS_CERT     = 'cert.pem'
KMS_KEY      = 'key.pem'
KMS_USERNAME = None
KMS_PASSWORD = None
KMS_CONFIG   = 'pykmip.conf'

client = kmip.pie.client.ProxyKmipClient(
           hostname=KMS_HOSTNAME,
           port=KMS_PORT,
           cert=KMS_CERT,
           key=KMS_KEY,
           username=KMS_USERNAME,
           password=KMS_PASSWORD,
           config_file=KMS_CONFIG)

# Retrieve list of keys
client.open()
KEYIDS = client.locate()
client.close()

# Retrieve random keys sequentially
for x in range(500) :
  client.open()
  mo = client.get(random.choice(KEYIDS))
  client.close()

