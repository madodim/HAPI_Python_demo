from hapiclient import hapi
from hapiplot import hapiplot


server = 'https://cdaweb.gsfc.nasa.gov/hapi'
dataset = 'OMNI2_H0_MRG1HR'
start = '2020-01-01T00:00:00'
stop = '2023-01-01T00:00:00'
parameters = 'DST1800'
opts = {'logging': True}

# Get data
data, meta = hapi(server, dataset, parameters, start, stop, **opts)
print(meta)
print(data)

# Plot all parameters

hapiplot(data, meta)