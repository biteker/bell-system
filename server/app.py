from flask import Flask, send_from_directory
from server.audio_player import play_bell, play_anthem
from server.scheduler import setup_schedule, run_schedule
import threading
import os

app = Flask(__name__, static_folder='../static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/play/bell')
def bell():
    play_bell()
    return 'Zil çalındı 🔔'

@app.route('/play/anthem')
def anthem():
    play_anthem()
    return 'İstiklal Marşı çalındı 🇹🇷'

def start_scheduler():
    setup_schedule()
    run_schedule()

# Zamanlayıcıyı paralel thread'de çalıştır
threading.Thread(target=start_scheduler, daemon=True).start()
