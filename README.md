# 🔔 Bell System – Okul Zil ve Ses Yayın Sistemi

Bu sistem, okul anfisine bağlı bir bilgisayarda çalışan bir otomasyon yazılımıdır.  
Mobil cihaz üzerinden kontrol edilen bu sistem ile:

- 📅 Ders/teneffüs saatlerine göre **otomatik zil çalma**
- 🇹🇷 **İstiklal Marşı** oynatma (zamanlı veya manuel)
- 📲 Mobil tarayıcıdan **manuel kontrol paneli**
- 🎙️ Telefon mikrofonundan **canlı ses yayını**

## 🚀 Kurulum

```bash
pip install -r requirements.txt
python run.py          # Web arayüz + zamanlayıcı
python server/voice_server.py   # WebSocket canlı yayın sunucusu
