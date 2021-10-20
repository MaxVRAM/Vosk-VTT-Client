# Vosk Voice To Text (VTT) client

[Vosk Server](https://alphacephei.com/vosk/server) is an open source Voice-To-Text server based on Vosk-API, and provides real-time voice transcription over WebSocket (and other protocols).

This Python script is based off their [`test_microphone.py`](https://github.com/alphacep/vosk-server/blob/master/websocket/test_microphone.py) example, acting as a client interface with a Vosk server. Currently, this version only adds OSC output of the transcription, but the plan is to expand this much further.

Please see the Vosk GitHub repo for details on the server and instructions on how to host your own:

[https://github.com/alphacep/vosk-server](https://github.com/alphacep/vosk-server)

---

## Future Plans
- Javascript/HTML5 interface.
- Allowing transcriptions to be sent via RESTful API.
- Implementing transcription retention in a database.
- Transcription of imported audio files.
- Visualisations and analysis (word-clouds, tables, etc).

## Dependencies

### Vosk Server

If you're using Docker, it's as easy as:
```
docker run -d -p 2700:2700 alphacep/kaldi-en:latest
```

See the Vosk Server [GitHub](https://alphacephei.com/vosk/server) page for more info.

### Client

- Python3
- pyaudio
- websockets
- python-osc

## Usage

If your Vosk Server is running locally listening on the default port `2700`, you can simply run the script:
```
python3 vtt_client.py
```

### Arguments

#### Vosk Server connection

- `-server <server_url>:<port>`
- Defaults to `localhost:2700`

A remote Vosk Server connection might look like this:
```
python3 vtt_client.py -server example.com:8089
```

#### OSC destination

- `-ip <osc_ip> -port <osc_port>`
- Defaults to `localhost` and `9600`

Sending the OSC elsewhere might look like this:
```
python3 vtt_client.py -ip 192.168.40.22 -port 5110
```

#### Putting it together

A full example might look like this:
```
python3 vtt_client.py -server example:8098 -ip 192.168.40.22 -port 5110
```
