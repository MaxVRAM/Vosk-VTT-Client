# Vosk Voice To Text (VTT) client

[Vosk Server](https://alphacephei.com/vosk/server) is an open source Voice-To-Text server based on Vosk-API, and provides real-time voice transcription over WebSocket (and other protocols).

This Python script is based off their [`test_microphone.py`](https://github.com/alphacep/vosk-server/blob/master/websocket/test_microphone.py) example, acting as a client interface with a Vosk server. Currently, this version only adds OSC output of the transcription, but the plan is to expand this much further.

Please see the Vosk GitHub repo for details on the server and instructions on how to host your own: [https://github.com/alphacep/vosk-server](https://github.com/alphacep/vosk-server)



## Feature ideas
- [x] OSC transcription output.
- [x] Python argument parser.
- [ ] Local Vosk server integration.
- [ ] Transcription of imported audio files.
- [ ] Webapp front-end:
  - [ ] Flask / Bootstrap / SQLAlchemy stack.
  - [ ] User authentication.
  - [ ] Per-account transcription retention.
- [ ] Text analysis:
  - [ ] Feature and keyword extraction
- [ ] Visualisation:
  - [ ] Wordcloud, tables, charts
  - [ ] D3.js?

## Dependencies

### Vosk Server

If you're using Docker, it's as easy as:

```shell
docker run -d -p 2700:2700 alphacep/kaldi-en:latest
```

See the Vosk Server [GitHub](https://alphacephei.com/vosk/server) page for more info.

### Client modules

- Python3
- pyaudio
- websockets
- python-osc


## Client setup guide

### Linux 

<details>
  <summary>Click for Linux setup instructions... </summary>

**This assumes you have `Python3` and `pip` installed.**

#### 1. Install the Python modules

*I had a fatal install error using the official `pip install pyaudio` on Ubuntu 20.04. The following command worked perfectly instead:*

``` shell
sudo apt install portaudio19-dev python3-pyaudio
pip install websockets python-osc
```

#### 2. Clone the project

```shell
git clone https://github.com/MaxVRAM/vosk_vtt_client.git
```

</details>


### Windows

<details>
  <summary>(Windows) Click for setup instructions... </summary>

#### 1. Install `Python 3`

**This will work with other versions of Python, but I've only tested it with Python 3.10.0, so that's what I'll be using as an example.**

1. Head over to the [Python Releases for Windows](https://www.python.org/downloads/windows/) site and download Python 3.10.0 (64-bit) installer - or use this [direct download link](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
2. Open the downloaded install file, **make sure the `Add Python 3.10 to PATH` option** at the bottom of the window is **checked**, then hit Install Now and wait for it to finish.
3. Open Windows command prompt by pressing `[win] + r`, enter `cmd` in the box and hit enter.
4. Check that Python is installed by entering `python -V` (with a capital V). It should print out `Python 3.10.0`.

#### 2. Install the Python modules

**PyAudio is not a native package on Windows, so it needs to be manually downloaded and imported from a `whl` wheel file.**

1. Open up your browser, and download the matching PyAudio file for your Python version and OS - [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

- For example, Python 3.10.0 on Windows 10 (64-bit) would require:
  - `PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl`
  - Where `cp310` is Python 3.10.0, and `win_amd64` is Windows 64-bit).

2. Move the file to your user's `Documents` folder.
3. Back in Windows command prompt, navigate to the Documents folder, using `cd Documents` if you're already in your user folder, otherwise `cd C:\Users\<your_user_name>\Documents`.
4. Now install the module:

```shell
pip install PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl
```

5. And finally install `websockets` and `python-osc`:

```shell
pip install websockets python-osc
```

#### 3. Clone the project

```shell
git clone https://github.com/MaxVRAM/vosk_vtt_client.git
```

- Or download the script directly [`vtt_client.py`](https://github.com/MaxVRAM/vosk_vtt_client/blob/main/vtt_client.py).

</details>


## Usage

If your Vosk Server is running locally listening on the default port `2700`, you can simply run the script:

```shell
python3 vtt_client.py
```

### Arguments

#### Vosk Server connection

- `-server <server_url>:<port>`
- Defaults to `localhost:2700`

A remote Vosk Server connection might look like this:

```shell
python3 vtt_client.py -server example.com:8089
```

#### OSC destination

- `-ip <osc_ip> -port <osc_port>`
- Defaults to `localhost` and `9600`

Sending the OSC elsewhere might look like this:

```shell
python3 vtt_client.py -ip 192.168.40.22 -port 5110
```

#### Putting it together

A full example might look like this:

```shell
python3 vtt_client.py -server example:8098 -ip 192.168.40.22 -port 5110
```
