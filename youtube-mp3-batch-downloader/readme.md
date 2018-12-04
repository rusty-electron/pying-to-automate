## Youtube mp3 Batch Downloader

I have been thinking about writing scripts to automate my regular tasks and I realized that I often find myself using third-party sites and sometimes manually converting videos to mp3 so I took up the task of writing a script of downloading batches of mp3 audio of youtube videos using their links. I use the functions of python module `youtube_dl` in this script. As of now, this script can do the following:

* download batches/single mp3 audio of youtube videos
    * links are to be provided in the `links.txt` file (can be easily altered to your choice)
    * it actually downloads the `.webm` file and then converts the file into `.mp3`.
    * bitrate of audio file can be specified
* download batches/single video file of youtube videos
    * video quality can be specified

## Getting Started

These instructions will get you a started for being able to use the scripts for downloading youtube video/audio at your own machine.

## Prerequisite

As the script is written in python, you are to download Python on your system, specifically Python 3.5 or latest. The installer can be downloaded [here](https://www.python.org/downloads/).

The other task that you need to do is to install the python module `youtube_dl`. You can download it using `pip`, which is a Python package manager and is included with Python. If you have never heard of it, you can learn about it [here](https://pypi.org/project/pip/).

`youtube_dl` can be installed using `pip` via the command:

```bash
pip install youtube-dl
```
The `youtube-dl` [git repo](https://github.com/rg3/youtube-dl/) contains detailed information for the its usage and the source code.

### Audio/Video Codec

`youtube-dl` utilizes ffmpeg/ffprobe for conversion tasks and therefore you are required to have it in your system `PATH`.

**For Windows**:

Download the codec from [here](https://ffmpeg.zeranoe.com/builds/) and extract and place the files in your system `PATH`.

**For Linux**:

Download it using terminal:

```bash
sudo apt get install ffmpeg
```

## Usage

After the preprequisites have been fulfilled, we can begin downloading by specifying the link(s) in the `links.txt` one line each.

```
https://www.youtube.com/watch?v=blahblahblah
https://www.youtube.com/watch?v=blahblahblah
```

Now, simply run the script in *command prompt* or *shell*.

```
python youtube-dlr.py
```

The default location for downloading files is in the `download/` folder in the current directory (can be altered in the code).

## Acknowledgments
* [Ricardo Garcia](https://github.com/rg3) for creating `youtube-dl`
* Zeranoe FFMPEG

## Update #1

* added instructions for installing `ffmpeg` on windows and linux
* added linux supported python script `youtube-dlr-linux.py`
    * *nothing special, simply changed path names. most of the code in supported in linux*




