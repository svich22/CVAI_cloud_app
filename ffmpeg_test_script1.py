import ffmpeg
import datetime
import shlex
import subprocess
import keyboard

print("Press 'a' when you want to cut last 30 second of video")

while True:
##Command to start mp4 conversion of live stream
    cmd = shlex.split('ffmpeg -i https://70adfb9ce288.us-east-1.playback.live-video.net/api/video/v1/us-east-1.064873805648.channel.kD3p7vqX9vpz.m3u8 -c copy -bsf:a aac_adtstoasc output_feb5.mp4') 
    subprocess.call(cmd)

    vid_duration = shlex.split('ffprobe -i output.mp4 -show_entries format=duration -v quiet -of csv="p=0"')
    subprocess.call(vid_duration)
    ## Get video duration
    # vid_duration_int = shlex.split('printf %.0f $vid_duration')
    # subprocess.call(vid_duration_int)


    ## Command to cut last 30 seconds of Video
    cmd_cut = shlex.split('ffmpeg -sseof -30 -i output_feb5.mp4 -c copy output.mp4')

        ## if you press a key on keyboard this will initiate cmd_cut command which will trim last 30 seconds of video
    if keyboard.read_key() == "a":
        print("Cut video processed is output_cut_vid.mp4")
        subprocess.call(cmd_cut)
        break
        

