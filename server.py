from getvideo_repository import GetVideo
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_latest_video():
    channel_url = "https://www.youtube.com/@coinbeast_media/videos"
    getVideo = GetVideo(channel_url)
    video = getVideo.get_latest_video()
    return  video
        

if __name__ == "__main__":
    app.run(port=3000)