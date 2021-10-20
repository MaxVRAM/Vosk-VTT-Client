# Kaldi Vosk Voice To Text (VTT) client

Vosk is an open source Voice To Text server that provides real-time voice transcription over WebSocket (and other protocols).

This Python script acts as a client interface with a Vosk Voice To Text server for real-time voice transcription. It currently outputs transcription results as OSC over UDP, but the plan is to expand this much further.

Please see the Vosk GitHub repo for details on the server and instructions on how to host your own:

[https://github.com/alphacep/vosk-api](https://github.com/alphacep/vosk-api)

---

Future plans include:
- Javascript/HTML5 interface.
- Allowing transcriptions to be sent via RESTful API.
- Implementing transcription retention in a database.
- Transcription of imported audio files.
- Visualisations and analysis (word-clouds, tables, etc).

---

### Dependencies

**Note:** You'll need access to a Vosk VTT server. See the link at the top for details on running your own.

- Python
- pyaudio
- websockets
- python-osc

---

### Usage

To simple view the streaming transcription in the console log, run `python3 vtt.py <server_url>:<port>`, replacing <server_url> and <port> with your Vosk server details, for example:
```
python3 vtt.py vtt.example.com:7800
```
  
If you'd like to send the transcription via OSC, add these arguments to the run command: `-ip <osc_ip> -port <osc_port>`. These default to `localhost` and `9600`. For example:
```
python3 vtt.py vtt.example.com:7800 -ip localhost -port 5110
```
