from flask import Flask
import redis, datetime

r = redis.Redis(host='redis')

k = "a-" + str(datetime.datetime.now())
r.set(k, 123 )

app = Flask(__name__)

from os import listdir
from os.path import isfile, join
mypath = "."
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print("Blah")



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True,host="0.0.0.0")
