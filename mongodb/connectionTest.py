import os
import pymongo

try:
    input = raw_input
except NameError:
    pass
host = input("Enter mongoDB host: ")
port = input("Enter mongoDB port: ")
user = input("Enter mongoDB username: ")
pasw = input("Enter mongoDB password: ")

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError

def get_extra_options():
    d = {}
    if "ssl_ca_certs" in os.environ:
      d["ssl_ca_certs"]=os.environ["ssl_ca_certs"]
    if "ssl" in os.environ:
      d["ssl"]=str_to_bool(os.environ["ssl"])
    if "tlsInsecure" in os.environ:
      d["tlsInsecure"]=str_to_bool(os.environ["tlsInsecure"])
    #Add more when needed
    return d


options = get_extra_options()
if len(options) > 0:
  print("Additional Options %s" % options)

try:
    options = get_extra_options()
    client = pymongo.MongoClient(host, int(port), username = user , password = pasw, **options)
except Exception as e:
    print("Failed to connect to host %s port %s" % (host, port))
    print(e)

# MongoClient does not block, we need to start using the client to get exceptions
print(client.admin.command("ismaster"))
