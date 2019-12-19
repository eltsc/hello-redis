import redis

client = redis.Redis(host = '127.0.0.1' , port = 6379)

client.set('name', 'elad')
client.set('name1', 'shay')
client.set('name2', 'yoni')
for key in client.keys('*'):
    print(client.get(key))
