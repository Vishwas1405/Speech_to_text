#import the library
from msilib.schema import File
from pytube import YouTube  
import moviepy.editor                                          #importing editor module form Moviepy library 
import speech_recognition as Sr                                #importing speech recognistion library 


#here we paste youutube video link to downalaod it 

link = input("Paste the youtube link here:")
youtube_1= YouTube(link)                                        #'youtube' function is reffering to the video link(link)

#title of youtube video
print("Title:" ,youtube_1.title)
tit = youtube_1.title



#download process of youtube video
YT_video = youtube_1.streams.get_highest_resolution()           #Downloading the video in highest Quality 
print("------Downloading----- ")                                           
Down_video = YT_video.download()                                #downloaded the Videos
print("-----Video downloaded Successfully-----") 


#Converting Video to Audio 
Vid_AUD = moviepy.editor.VideoFileClip(Down_video)
print("-----Now Converting Video File to Audio File-----")
Aud = Vid_AUD.audio
Aud_File = Aud.write_audiofile(youtube_1.title+".wav")
print("-----File Conversion to Audio is Completed Successfully-----")


#Converting Audio to Text
r = Sr.Recognizer()                                             #Initialize the Speech recognizer class
print("----Please Wait While Video is Converting from Audio to Text---- ")


with Sr.AudioFile(youtube_1.title+'.wav') as Source:
    audio_text = r.listen(Source)

    try:
        Aud_txt= r.recognize_google(audio_text)
        
    except:
        print("Error Found please Re-Run the program")

File=open(youtube_1.title+'.txt','w')
File.write(Aud_txt)
print("Video is Successfully Converted to Text")
print("-----Opening the TXT File----")





