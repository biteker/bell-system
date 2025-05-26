import schedule
import time
from .audio_player import play_bell, play_anthem

def setup_schedule():
    # 🔔 Zil saatlerini buraya yaz (örnek saatler)
    schedule.every().day.at("09:00").do(play_bell)
    schedule.every().day.at("10:40").do(play_bell)
    schedule.every().monday.at("08:30").do(play_anthem)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
