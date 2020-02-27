
# MongoDB Connection Test
This docker image is used to test customer's connection to MongoDB; using the specific version of pymongo the smart agent uses.

You can run the script directly, without docker, as long as you have the pymongo package installed (example: run it in the same place where the agent is running)

## Build
Run the below to build the image
```
docker build -t <repo/name:tag> .
```

## Run
`--net host` is only needed if mongodb is installed on the same docker host and you are trying to access it through localhost

```
docker run -it --net host <repo/name:tag>
```

## Examples

#### Successful Run:
```
prompt$ docker run -it --net host dlouca/mongotest:latest
Enter mongoDB host: localhost
Enter mongoDB port: 27017
{u'ismaster': True, u'maxWriteBatchSize': 100000, u'ok': 1.0, u'maxWireVersion': 8, u'connectionId': 8, u'readOnly': False, u'localTime': datetime.datetime(2020, 2, 25, 18, 31, 14, 76000), u'minWireVersion': 0, u'maxBsonObjectSize': 16777216, u'maxMessageSizeBytes': 48000000, u'logicalSessionTimeoutMinutes': 30}
```

#### Failed Run:
```
prompt$ docker run -it --net host dlouca/mongotest:latest
Enter mongoDB host: saassa
Enter mongoDB port: 12334
Traceback (most recent call last):
# MongoDB Connection Test
  File "./connectionTest.py", line 17, in <module>
# MongoDB Connection Test
    print(client.admin.command("ismaster"))
  File "/usr/local/lib/python2.7/site-packages/pymongo/database.py", line 478, in command
    with client._socket_for_reads(read_preference) as (sock_info, slave_ok):
  File "/usr/local/lib/python2.7/contextlib.py", line 17, in __enter__
    return self.gen.next()
  File "/usr/local/lib/python2.7/site-packages/pymongo/mongo_client.py", line 798, in _socket_for_reads
    with self._get_socket(read_preference) as sock_info:
  File "/usr/local/lib/python2.7/contextlib.py", line 17, in __enter__
    return self.gen.next()
  File "/usr/local/lib/python2.7/site-packages/pymongo/mongo_client.py", line 762, in _get_socket
    server = self._get_topology().select_server(selector)
  File "/usr/local/lib/python2.7/site-packages/pymongo/topology.py", line 210, in select_server
    address))
  File "/usr/local/lib/python2.7/site-packages/pymongo/topology.py", line 186, in select_servers
    self._error_message(selector))
pymongo.errors.ServerSelectionTimeoutError: saassa:12334: [Errno -2] Name or service not known
```

## Additional Options:

You can pass additional options as environmental variables.
The following options are supported: `ssl_ca_certs`, `ssl` and `tlsInsecure`

example using docker:
```
docker run -it --env ssl=True --env tlsInsecure=True --net host dlouca/mongotest:latest bash
```








