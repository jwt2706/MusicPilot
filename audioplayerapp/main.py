
# from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty, StringProperty
# from kivymd.uix.button import MDIconButton,MDTextButton
# from kivy.lang import Builder

# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.image import Image,AsyncImage
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import random
import os
#import time

Window.size = (450, 600)


class MusicPlayer():
    def __init__(self):
        self.music_list = []
        self.saved_music = []
        self.music_titles = dict()
        # self.thumbnail_list = []
        self.number_of_tracks = 0
        self.track_counter = 0
        self.thumbnail_url = ""
        self.song_title = ""
        self.music_length = 0.0
        self.current_music_path = ""
        self.shuffle_play = 1 #on
        self.sound = None
        self.play_started = False
        self.play_ended = False
        self.playing_pos = 0.0
        self.player_paused = False
        self.end_of_list = False
        self.manual_next = False
        ######
        self.load_playlist()
        #self.load_music_titles()
        # self.music_ethnic = False
        if self.number_of_tracks>0:
            self.play()

    def play(self):
        if self.player_paused:
            self.sound.play()
            self.sound.seek(self.playing_pos)
            self.player_paused = False
        else:
            self.play_music()

    def pause(self):
        self.playing_pos = self.sound.get_pos()
        self.player_paused = True
        self.sound.stop()

    def next(self):
        if self.sound:            
            if self.track_counter<len(self.music_list)-1:
                self.track_counter += 1                
            else:
                self.end_of_list = True
                print("End of list.")
                # self.track_counter = 0
            self.sound.stop()
        else:
            self.play_music()

    def previous(self):
        if self.sound:
            if self.track_counter>0:
                self.track_counter -= 1
            else:
                self.track_counter = len(self.music_list)-1
            
            self.sound.stop()
        else:
            self.play_music()

    def play_next(self):
        if self.track_counter<len(self.music_list)-1:
            self.track_counter += 1
            self.play_music()
    
    def shuffle(self):
        if len(self.music_list)>0:
            if self.shuffle_play:
                random.shuffle(self.music_list)

    def restart(self):
        if self.sound:
            self.track_counter = 0
            self.end_of_list = False
            self.sound.stop()
        else:
            self.play_music()

    def play_music(self):
        if self.load_audio():
            self.sound = SoundLoader.load(self.current_music_path)
            #self.sound.bind(on_play=self.player_playing,on_stop=self.player_stopped)
            if self.sound:
                self.music_length = self.sound.length
                self.sound.play()
        else:
            print("attempting next...")
            # time.sleep(5)
            if self.track_counter==0:
                self.track_counter += 1
            self.next()
    #########################    
    def player_playing(self, obj):
        self.play_started = True
        self.play_ended = False
        self.manual_next = False

    def player_stopped(self, obj):
        self.play_ended = True
        self.play_started = False

    def load_audio(self):
        print(" Track: {}".format(self.track_counter))
        video_id = self.music_list[self.track_counter]
        
        path = "./music"
        f_name = os.path.join(path,video_id+".mp3")
        img_name = os.path.join(path,video_id+".jpg")

        skip_list = ['oromo','ii','uu','aa','ee','oromiyaa','oroomiyaa','jj']

        if video_id in self.music_list:
            self.current_music_path = f_name
            print("F_NAME: "+f_name)
            if os.path.exists(img_name):
                self.thumbnail_url = img_name
            else:
                self.thumbnail_url = "default_1.png"
            s_title = ''
            self.song_title = self.music_titles.get(video_id,s_title)
            ### I'm just skipping some of the music tracks ...
            for term in skip_list:
                if term in self.song_title.lower():
                    print(self.song_title)
                    return False
            return True
        return False

    def load_playlist(self):
        #### Downloaded music files are in local disk
        path = "./music"
        files = os.listdir(path)
        lists = set()
        for f in files:
            # v_id = f.split('.')[0]
            lists.add(f.split('.')[0])
        self.saved_music = list(lists)
        self.music_list = list(self.saved_music)
        self.number_of_tracks = len(self.music_list)        
        # print("#saved music:",len(self.saved_music))

    #def load_music_titles(self):
    #    file = open('music_titles.json','r')
    #    jfile = json.load(file) 
    #    for id in jfile:
    #    self.music_titles[id] = jfile[id]
        # print("#titles:",len(self.music_titles))
    #    file.close()


class MainUI(MDBoxLayout):

    manual_next = False
    play_state = 0

    icon_type = StringProperty("play-outline")
    shuffle_icon = StringProperty("shuffle")
    thumbnail_url = StringProperty("default_1.png")
    song_title = StringProperty("-- Music Title --")
    song_pos = StringProperty("\n 0.0")
    num_of_tracks = StringProperty("\n #Tracks: 0")
    slider_value = NumericProperty(0.0)
    volume_value = NumericProperty(50)
    volume_icon = StringProperty("volume-medium")
    mplayer = MusicPlayer()

    def __init__(self,**kwargs):
        super(MainUI,self).__init__(**kwargs)
        # self.mplayer = MusicPlayer()
        self.play_event = Clock.schedule_interval(self.player_state_callback, 1 / 2.)
        
    def play_click(self):
        # print("Play button clicked.")
        if self.play_state:
            self.icon_type = "play-outline"
            self.play_state = 0
            self.mplayer.pause()
        else:
            self.icon_type = "pause"
            self.play_state = 1
            self.song_title = " Loading music ...."
            self.mplayer.play()
        self.update_ui()

    def next_click(self):
        self.mplayer.manual_next = True
        self.mplayer.next()
        self.update_ui()  

    def previous_click(self):
        self.mplayer.manual_next = True
        self.mplayer.previous()
        self.update_ui()

    def restart_click(self):
        self.mplayer.restart()
        self.update_ui()

    def shuffle_click(self):
        if self.mplayer.shuffle_play:
            self.mplayer.shuffle_play = 0 #off
            self.shuffle_icon = "shuffle"
        else:
            self.mplayer.shuffle_play = 1 #on
            self.shuffle_icon = "shuffle-disabled"
        self.mplayer.shuffle()
        # print('shuffle clicked.')

    def update_ui(self):
        self.thumbnail_url = self.mplayer.thumbnail_url
        self.song_title = self.mplayer.song_title
        self.num_of_tracks = "\n #Tracks: "+str(self.mplayer.number_of_tracks)
        print("CHECK: "+str(self.mplayer.number_of_tracks))
        # self.song_pos = str(self.mplayer.music_length)
        
    def player_state_callback(self,obj):
        if self.mplayer.play_started:
            self.update_ui()
            pos = self.mplayer.sound.get_pos()
            self.slider_value = 100.0*pos/self.mplayer.music_length
            minute = int(pos/60)
            second = int(pos-minute*60)
            if second<10:
                second = '0'+str(second)
            
            t_min = int(self.mplayer.music_length/60)
            t_sec = int(self.mplayer.music_length-t_min*60)
            if t_sec<10:
                t_sec ='0'+str(t_sec)
            t_time = str(t_min)+':'+str(t_sec)
            self.song_pos = '\n'+str(minute)+':'+str(second)+"/"+t_time
            self.play_state = 1
            self.icon_type = "pause"

        elif self.mplayer.play_ended:
            if self.mplayer.player_paused:
                pass
            else:
                if not self.mplayer.end_of_list:
                    if self.mplayer.manual_next:
                        self.mplayer.play()
                        # self.manual_next = False
                    else:
                        self.mplayer.play_next()

                    self.update_ui()
                    # self.thumbnail_url = self.mplayer.thumbnail_url
                    # self.song_title = self.mplayer.song_title
                else:
                    self.play_state = 0
                    self.mplayer.track_counter = 0
                    self.icon_type = "play-outline" 
                
    def slider_value_change(self,widget):
        self.slider_value = widget.value


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MainUI()

    def on_pause(self):
        return True

if __name__ == "__main__":
    MainApp().run()
