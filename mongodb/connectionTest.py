import pymongo


try:
    input = raw_input
except NameError:
    pass
host = input("Enter mongoDB host: ")
port = input("Enter mongoDB port: ")
try:
    client = pymongo.MongoClient(host, int(port))
except Exception as e:
    print("Failed to connect to host %s port %s" % (host, port))
    print(e)

# MongoClient does not block, we need to start using the client to get exceptions
print(client.admin.command("ismaster"))
