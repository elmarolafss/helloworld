import os
from bottla import *

@route("/")
def helloworld():
  return "Hello Heroku"

run(host="0.0.0.0", port="os.environ.get("PORT")")
