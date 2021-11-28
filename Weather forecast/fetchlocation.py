from ipregistry import IpregistryClient
client = IpregistryClient('fz7oviptwwe7moqa')  
ipInfo = client.lookup() 
city= ipInfo.location['city']
print(city)
