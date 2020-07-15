#!/usr/bin/env python
# coding: utf-8

# In[3]:


### This code trim the video file to multiple parts in length less than 60 seconds,
### with extension mp4 and wav using moviepy package.

from moviepy.editor import *

part1 = VideoFileClip("COPD, inhaler choice and PIF Short.mp4").subclip("00:00:00", "00:00:58")
part1.write_videofile("part1.mp4")
part1.audio.write_audiofile("part1_audio.wav")

part2 = VideoFileClip("COPD, inhaler choice and PIF Short.mp4").subclip("00:00:58", "00:01:43")
part2.write_videofile("part2.mp4")
part2.audio.write_audiofile("part2_audio.wav")

part3 = VideoFileClip("COPD, inhaler choice and PIF Short.mp4").subclip("00:01:43", "00:02:33")
part3.write_videofile("part3.mp4")
part3.audio.write_audiofile("part3_audio.wav")


# In[4]:


### This code convert the speech from each audio part to text using speech recognition package and google recognition API
### and create a text file in the local machine and print the speech in jupyter cell. 

import speech_recognition as sr

r = sr.Recognizer()

part1 = sr.AudioFile('part1_audio.wav')
with part1 as source1:
    audio1 = r.record(source1)
    
text1 = r.recognize_google(audio1)

part1_text = open(r'part1_text.txt','w')
part1_text.writelines(text1)
part1_text.close()

part2 = sr.AudioFile('part2_audio.wav')
with part2 as source2:
    audio2 = r.record(source2)
    
text2 = r.recognize_google(audio2)

part2_text = open(r'part2_text.txt','w')
part2_text.writelines(text2)
part2_text.close()

part3 = sr.AudioFile('part3_audio.wav')
with part3 as source3:
    audio3 = r.record(source3)
    
text3 = r.recognize_google(audio3)

part3_text = open(r'part3_text.txt','w')
part3_text.writelines(text3)
part3_text.close()

print('Video_Text_Part1:')
print((text1))
print('\nVideo_Text_Part2:')
print((text2))
print('\nVideo_Text_Part3:')
print((text3))

