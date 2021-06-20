from flask import Flask
from threading import Thread

app = Flask("")

@app.route('/')
def home():
  link = "https://discord.com/api/oauth2/authorize?client_id=841145872314400778&permissions=2148001856&scope=bot"
  web_message = "Hello. I am alive!\n" + "To add bot to server, visit link: " + link
  return web_message

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()