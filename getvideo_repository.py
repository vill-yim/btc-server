from yt_dlp import YoutubeDL

class GetVideo():
    def __init__(self, ytb_channel):
        self.ytb_channel = ytb_channel

    def get_latest_video(self):
        ydl_opts={
            "quiet":True,
            'dump_single_json':True,
            'extract_flat': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.ytb_channel,download=False)
            video = info['entries'][0]
            return video
