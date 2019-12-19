import redis
from flask import Flask, request
import random
import string

app = Flask(__name__)
client = redis.Redis(host = 'localhost' , port = 6379)

client.set('name', 'elad')
client.set('name1', 'shay')
client.set('name2', 'yoni')

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/')
def hello():
    hello = ''
    for key in client.keys('*'):
        hello += client.get(key).decode("utf-8") 
    return hello

@app.route('/add')
def add():
    new = request.args['new']
    name = randomString()
    client.set(name, new)
    return new + " added"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = '8080')