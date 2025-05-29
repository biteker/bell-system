import asyncio
import websockets
import pyaudio
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

async def audio_handler(websocket):
    print("📲 Canlı yayın bağlantısı kuruldu!")
    try:
        async for message in websocket:
            print(f"📦 Veri geldi: {len(message)} byte")  # <--- BU SATIRI EKLE
            audio_data = np.frombuffer(message, dtype=np.int16)
            stream.write(audio_data.tobytes())
    except websockets.exceptions.ConnectionClosed:
        print("🔌 Yayın kesildi")

async def main():
    async with websockets.serve(audio_handler, "0.0.0.0", 8765):
        print("📡 WebSocket ses sunucusu hazır: ws://0.0.0.0:8765")
        await asyncio.Future()  # sonsuz döngü

if __name__ == "__main__":
    asyncio.run(main())
