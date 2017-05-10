# -*- coding: utf-8 -*-
__auther__ = 'Tillfore'

from moviepy.editor import *
# region 初次使用可能要安装
import imageio
imageio.plugins.ffmpeg.download()
# endregion

int_ClipsNumber = 0
video = VideoFileClip("宣传视频1610.mp4").subclip(50,60)

# Make the text. Many more options are available.
# txt_clip = ( TextClip("测试视频",fontsize=70,color='white')
             #.set_position('center')
             #.set_duration(10) )

result = CompositeVideoClip([video, ]) # Overlay text on video
result.write_videofile("测试导出.mp4",fps=29) # Many options...