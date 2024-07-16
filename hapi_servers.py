from hapiclient import hapi

servers = hapi() # servers is an array of URLs
print(servers)

server = 'https://cdaweb.gsfc.nasa.gov/hapi'
meta = hapi(server)
print(meta)