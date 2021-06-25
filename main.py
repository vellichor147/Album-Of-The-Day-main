from authorization import *
from getMethods import *
from artistsData import *
from opCV2 import *
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import random
import urllib.request
import pprint
import os
import pandas as pd
import webbrowser

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

# def newInput(artist_ID, artist_name, artist_popularity):
#     # Create input DataFrame
#     df_input = pd.DataFrame({'artist_id':[],'name':[],'popularity':[],'album_ids':[]})
#     # Change columns type
#     df_input['artist_id'] = df_input.artist_id.astype(str)
#     df_input['name'] = df_input.artist_id.astype(str)
#     df_input['popularity'] = df_input.artist_id.astype(int)
#     df_input['album_ids'] = df_input.artist_id.astype(str)
#     # Input new artist data
#     df_input.at[0, 'artist_id'] = artist_ID
#     df_input.at[0, 'name'] = artist_name
#     df_input.at[0, 'popularity'] = artist_popularity
#     # Print new input
#     # print('input:')
#     # print(df_input.head(5))
#     return df_input
#
# def getArtistHighPop():
#     # Create subset DataFrame of artists with popularity from 80 to 100
#     df_artists_hP = df_artists.loc[(df_artists['popularity'] > 80) & (df_artists['popularity'] <= 100)]
#     rows = len(df_artists_hP.index)                                   # Get number of rows (artists) - 341
#     rn = random.randint(0,rows)                                       # Generate random row number
#     artist_ID = df_artists_hP.iloc[rn,0]                              # Get artist ID form chosen random row
#     artist_name = df_artists_hP.iloc[rn,1]                            # Get artist name form chosen random row
#     artist_popularity = df_artists_hP.iloc[rn,2]                      # Get artist popularity form chosen random row
#     nInput = newInput(artist_ID,artist_name,artist_popularity)        # Create new input - new DataFrame used to pass information to history csv
#     return nInput


def createHistoryLogCSV():
    # Create album history csv file
    df_album_history = pd.DataFrame({'artist_id': [], 'artist': [], 'popularity': [],'album_name': [], 'album_id': []})
    df_album_history.to_csv('albums_history.csv', index=False)
    df_album_history['artist_id'] = df_album_history.artist_id.astype(str)
    df_album_history['artist'] = df_album_history.artist_id.astype(str)
    df_album_history['popularity'] = df_album_history.artist_id.astype(int)
    df_album_history['album_name'] = df_album_history.artist_id.astype(str)
    df_album_history['album_id'] = df_album_history.artist_id.astype(str)

    # print(df_album_history)


def HighPopularity():   # 40%
    # Create subset DataFrame of artists with popularity from 80 to 100
    df_artists_hP = df_artists.loc[(df_artists['popularity'] > 80) & (df_artists['popularity'] <= 100)]
    rows = len(df_artists_hP.index)                                   # Get number of rows (artists) - 341
    rn = random.randint(0, rows)                                       # Generate random row number
    artist_id = df_artists_hP.iloc[rn, 0]                              # Get artist ID form chosen random row
    return artist_id


def MediumPopularity():  # 30%
    df_artists_mP = df_artists.loc[(df_artists['popularity'] > 60) & (df_artists['popularity'] <= 80)]
    rows = len(df_artists_mP.index)                                   # Get number of rows (artists) - 341
    rn = random.randint(0, rows)                                       # Generate random row number
    artist_id = df_artists_mP.iloc[rn, 0]                              # Get artist ID form chosen random row
    return artist_id


def LowPopularity():   # 20%
    df_artists_lP = df_artists.loc[(df_artists['popularity'] > 40) & (df_artists['popularity'] <= 60)]
    rows = len(df_artists_lP.index)                                   # Get number of rows (artists) - 341
    rn = random.randint(0, rows)                                       # Generate random row number
    artist_id = df_artists_lP.iloc[rn, 0]                              # Get artist ID form chosen random row
    return artist_id


def VeryLowPopularity():    # 10%
    df_artists_vlP = df_artists.loc[(df_artists['popularity'] > 0) & (df_artists['popularity'] <= 40)]
    rows = len(df_artists_vlP.index)                                    # Get number of rows (artists) - 341
    rn = random.randint(0, rows)                                        # Generate random row number
    artist_id = df_artists_vlP.iloc[rn, 0]                              # Get artist ID form chosen random row
    return artist_id

# root window
root = Tk()
root.title("Album of the day")
root.iconbitmap('vinyl.ico')
root.resizable(0, 0)                # fixed window size
root.geometry("1000x620")           # window size
root.configure(background="#191414")

token = getAccessToken(client_ID, client_Secret)            # Get user token
df_artists = pd.read_csv('artists.csv')                     # Load artists.csv
#createHistoryLogCSV()                                       # Create albums_history.csv
df_log = pd.read_csv('albums_history.csv')                  # Load albums_history.csv as DataFrame object 'df_log'
                                                            # ({'artist_id':[],'name':[],'popularity':[],'album_ids':[]})


class GUI:
    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.pack()

        # region Class members
        self.artist_id = None
        self.artist_info = None
        self.artist_genre = None
        self.album_info = None
        self.artist_name = None
        self.artist_url = None
        self.artist_followers = None
        self.artist_popularity = None
        self.album_id = None
        self.album_cover = None
        self.album_name = None
        self.album_name_extended = None
        self.album_date = None
        self.album_link = None
        self.artist_genre_list = None
        self.cover = None
        self.cover_label2 = None
        self.label_font = 'Calibri 22 italic bold'
        self.label_status_font = 'Calibri 10'
        # endregion

        #region Widgets position members
        # Main widgets
        self.album_name_x = 50
        self.album_name_y = 0
        self.album_year_x = 50
        self.album_year_y = 35
        self.artist_name_x = 50
        self.artist_name_y = 70
        self.genre_x = 50
        self.genre_y = 115
        self.genre_list_x = 120
        self.genre_list_y = 115
        self.cover_x = 50
        self.cover_y = 150
        self.button_x = 135
        self.button_y = 520
        #API data widgets
        self.API_data_widget_x = 425
        self.API_data_widget_y = 200
        self.artist_id_widget_x = 425
        self.artist_id_widget_y = 220
        self.artist_id_text_x = 485
        self.artist_id_text_y = 222
        self.artist_link_widget_x = 425
        self.artist_link_widget_y = 240
        self.artist_link_text_x = 498
        self.artist_link_text_y = 242
        self.artist_popularity_widget_x = 425
        self.artist_popularity_widget_y = 260
        self.artist_popularity_text_x = 540 
        self.artist_popularity_text_y = 263
        self.artist_followers_widget_x = 425
        self.artist_followers_widget_y = 280
        self.artist_followers_text_x = 500
        self.artist_followers_text_y = 282
        self.album_id_widget_x = 425    
        self.album_id_widget_y = 300
        self.album_id_text_x = 495
        self.album_id_text_y = 302
        self.album_link_widget_x = 425
        self.album_link_widget_y = 320
        self.album_link_text_y = 430
        self.album_link_text_x = 505
        self.album_link_text_y = 322

        #endregion
     
        #region Buttons
        self.myFont = font.Font(family='Calibri', size=20, weight='bold')
        self.new_album_button = Button(master, text="NEW ALBUM", padx=15, pady=15, bg="#1DB954", fg="white", command=self.click)
        self.new_album_button.place(x=self.button_x, y=self.button_y)
        self.new_album_button['font'] = self.myFont
        #endregion

        #region Main Labels
        # Album name widget
        self.album_name_widget = Label(root, text='', fg="white", bg='#191414', font=self.label_font)
        self.album_name_widget.place(x=self.album_name_x, y=self.album_name_y)

        # Album year widget
        self.album_year_widget = Label(root, text='', fg="white", bg='#191414', font=self.label_font)
        self.album_year_widget.place(x=self.album_year_x, y=self.album_year_y)

        # Artist name widget
        self.artist_name_widget = Label(root, text='', fg="white", bg='#191414', font=self.label_font)
        self.artist_name_widget.place(x=self.artist_name_x, y=self.artist_name_y)

        # Genre widget
        self.genre_widget = Label(root, text='Genre: ', fg="white", bg='#191414', font='Calibri 15')
        self.genre_widget.place(x=self.genre_x, y=self.genre_y)
        self.genre_list_widget = Label(root, text='', fg="white", bg='#191414', font='Calibri 15')
        self.genre_list_widget.place(x=self.genre_list_x, y=self.genre_list_y)

        self.hover_label = Label(root, text='', fg="white", bg='#191414', font=self.label_status_font)
        self.hover_label.place(x=900, y=600)
        #endregion

        #region API Labels and text
        self.API_data_widget = Label(root, text='Spotify API data:', fg="white", bg='#191414', font='Calibri 12 bold')
        self.API_data_widget.place(x=self.API_data_widget_x, y=self.API_data_widget_y)

        self.artist_id_widget = Label(root, text='Artist id:', fg="white", bg='#191414', font='Calibri 12 bold')
        self.artist_id_widget.place(x=self.artist_id_widget_x, y=self.artist_id_widget_y)

        self.artist_id_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_id_text.insert(1.0, 'artist_id-placeholder')
        self.artist_id_text.configure(state="disable",inactiveselectbackground=self.artist_id_text.cget("selectbackground"))
        self.artist_id_text.place(x=self.artist_id_text_x, y=self.artist_id_text_y)

        self.artist_link_widget = Label(root, text='Artist link: ', fg="white", bg='#191414', font='Calibri 12')
        self.artist_link_widget.place(x=self.artist_link_widget_x, y=self.artist_link_widget_y)

        self.artist_link_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_link_text.insert(1.0, 'artist_link-placeholder')
        self.artist_link_text.configure(state="disable",inactiveselectbackground=self.artist_link_text.cget("selectbackground"))
        self.artist_link_text.place(x=self.artist_link_text_x, y=self.artist_link_text_y)

        self.artist_popularity_widget = Label(root, text='Artist popularity: ', fg="white", bg='#191414', font='Calibri 12')
        self.artist_popularity_widget.place(x=self.artist_popularity_widget_x, y=self.artist_popularity_widget_y)

        self.artist_popularity_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_popularity_text.insert(1.0, 'artist_popularity-placeholder')
        self.artist_popularity_text.configure(state="disable",inactiveselectbackground=self.artist_popularity_text.cget("selectbackground"))
        self.artist_popularity_text.place(x=self.artist_popularity_text_x, y=self.artist_popularity_text_y)

        self.artist_followers_widget = Label(root, text='Followers: ', fg="white", bg='#191414', font='Calibri 12')
        self.artist_followers_widget.place(x=self.artist_followers_widget_x, y=self.artist_followers_widget_y)

        self.artist_followers_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_followers_text.insert(1.0, 'artist_followers-placeholder')
        self.artist_followers_text.configure(state="disable",inactiveselectbackground=self.artist_followers_text.cget("selectbackground"))
        self.artist_followers_text.place(x=self.artist_followers_text_x, y=self.artist_followers_text_y)

        self.album_id_widget = Label(root, text='Album id: ', fg="white", bg='#191414', font='Calibri 12')
        self.album_id_widget.place(x=self.album_id_widget_x, y=self.album_id_widget_y)

        self.album_id_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.album_id_text.insert(1.0, 'album_id-placeholder')
        self.album_id_text.configure(state="disable",inactiveselectbackground=self.album_id_text.cget("selectbackground"))
        self.album_id_text.place(x=self.album_id_text_x, y=self.album_id_text_y)

        self.album_link_widget = Label(root, text='Album link: ', fg="white", bg='#191414', font='Calibri 12')
        self.album_link_widget.place(x=self.album_link_widget_x, y=self.album_link_widget_y)

        self.album_link_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.album_link_text.insert(1.0, 'album_link-placeholder')
        self.album_link_text.configure(state="disable",inactiveselectbackground=self.album_link_text.cget("selectbackground"))
        self.album_link_text.place(x=self.album_link_text_x, y=self.album_link_text_y)

       
        #endregion 


    def hover(self,e):
        self.hover_label.config(text='Listen on Spotify')
        resizeFunction("cover.png", 360, 360, "resized_cover_enlarge.png")     
        self.cover_enlarge = ImageTk.PhotoImage(Image.open("resized_cover_enlarge.png"))
        self.ButtonImage.config(image=self.cover_enlarge)
        self.ButtonImage.place(x=self.cover_x-5, y=self.cover_y-5)
        #print('hovering')

    def hover_leave(self,e):
        self.hover_label.config(text='')
        self.ButtonImage.config(image=self.cover)
        self.ButtonImage.place(x=self.cover_x, y=self.cover_y)
        #print("not hovering")

    def update_widgets(self):

        # Album cover label
        urllib.request.urlretrieve(self.album_cover, "cover.png")            # Create album cover from album_cover link
        resizeFunction("cover.png", 350, 350, "resized_cover.png")        
        self.cover = ImageTk.PhotoImage(Image.open("resized_cover.png"))     # Store resized album cover to 'cover' variable
        #self.cover2 = cv2.imread("resized_cover")
        
        #self.cover_label2 = Label(image=self.cover).place(x=self.cover_x, y=self.cover_y)       # Create label for album cover and place is on 80,50
        self.ButtonImage = Button(root, image = self.cover, command=self.openAlbumLink)
        self.ButtonImage.place(x=self.cover_x, y=self.cover_y)
        self.ButtonImage.bind("<Enter>", self.hover) 
        self.ButtonImage.bind("<Leave>", self.hover_leave) 

        # Album name widget
        self.album_name_widget.destroy()
        self.album_name_widget = Label(root, text=self.album_name, fg="white", bg='#191414', font=self.label_font)
        self.album_name_widget.place(x=self.album_name_x, y=self.album_name_y)
    
        # Artist name widget
        self.artist_name_widget.destroy()
        self.artist_name_widget = Label(root, text='by ' + self.artist_name, fg="white", bg='#191414', font=self.label_font)
        self.artist_name_widget.place(x=self.artist_name_x, y=self.artist_name_y)

        # Album year widget
        self.album_year_widget.destroy()
        self.album_year_widget = Label(root, text=self.album_date, fg="white", bg='#191414', font=self.label_font)
        self.album_year_widget.place(x=self.album_year_x, y=self.album_year_y)

        # Genre widget
        self.genre_list_widget.destroy()
        self.genre_list_widget = Label(root, text=self.artist_genre_list, fg="white", bg='#191414', font='Calibri 15')
        self.genre_list_widget.place(x=self.genre_list_x, y=self.genre_list_y)

        self.artist_id_widget.destroy()
        self.artist_id_widget = Label(root, text='Artist id: ', fg="white", bg='#191414', font='Calibri 12')
        self.artist_id_widget.place(x=self.artist_id_widget_x, y=self.artist_id_widget_y)

        # Artist id Text
        self.artist_id_text.destroy()
        self.artist_id_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_id_text.insert(1.0, str(self.artist_id))
        self.artist_id_text.configure(state="disable",inactiveselectbackground=self.artist_id_text.cget("selectbackground"))
        self.artist_id_text.place(x=self.artist_id_text_x, y=self.artist_id_text_y)
        # Artist url Text
        self.artist_link_text.destroy()
        self.artist_link_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_link_text.insert(1.0, str(self.artist_url))
        self.artist_link_text.configure(state="disable",inactiveselectbackground=self.artist_link_text.cget("selectbackground"))
        self.artist_link_text.place(x=self.artist_link_text_x, y=self.artist_link_text_y)
        # Artist pupularity
        self.artist_popularity_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_popularity_text.insert(1.0, str(self.artist_popularity))
        self.artist_popularity_text.configure(state="disable",inactiveselectbackground=self.artist_popularity_text.cget("selectbackground"))
        self.artist_popularity_text.place(x=self.artist_popularity_text_x, y=self.artist_popularity_text_y)
        # Album link Text
        self.album_link_text.destroy()
        self.album_link_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.album_link_text.insert(1.0, self.album_link)
        self.album_link_text.configure(state="disable",inactiveselectbackground=self.album_link_text.cget("selectbackground"))
        self.album_link_text.place(x=self.album_link_text_x, y=self.album_link_text_y)

        # Artist followers
        self.artist_followers_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.artist_followers_text.insert(1.0, str(self.artist_followers))
        self.artist_followers_text.configure(state="disable",inactiveselectbackground=self.artist_followers_text.cget("selectbackground"))
        self.artist_followers_text.place(x=self.artist_followers_text_x, y=self.artist_followers_text_y) 

        self.album_id_text.destroy()
        self.album_id_text = Text(root, height=1, borderwidth=0, fg="white", bg='#191414', font='Calibri 12')
        self.album_id_text.insert(1.0, str(self.album_id))
        self.album_id_text.configure(state="disable",inactiveselectbackground=self.album_id_text.cget("selectbackground"))
        self.album_id_text.place(x=self.album_id_text_x, y=self.album_id_text_y)
    
    def update_artist_data(self):
        self.artist_info = getArtistInfo(token=token, artist_ID=self.artist_id)  # Returns artist info [name,link,followers,genres,popularity]
        self.album_info = getAlbumsInfo(token=token, artist_ID=self.artist_id)   # Returns albums info [album_id,album_cover,album_name,album_date,album_link]
        
        # Check if album appeard by searching albums_history.csv
        found = df_log[df_log['album_id'].str.contains(self.album_info[0])]
        a = found.count()
        if a['album_id'] >= 1:
            print('duplicate!')
            self.click()
        else:     
            self.artist_name = self.artist_info[0]
            self.artist_url = self.artist_info[1]
            self.artist_followers = self.artist_info[2]
            self.artist_genre_list = self.artist_info[3][0:3]
            self.artist_popularity = self.artist_info[4]

            self.album_id = self.album_info[0]
            self.album_cover = self.album_info[1]
            self.album_name = self.album_info[2]
            self.album_date = '(' + self.album_info[3][0:4] + ')'
            self.album_link = self.album_info[4]

            #region Enter log in albums_history.csv
            rows = len(df_log.index)
            if rows == 0:
                df_log.at[0, 'artist_id'] = self.artist_id
                df_log.at[0, 'artist'] = self.artist_name
                df_log.at[0, 'popularity'] = self.artist_popularity  
                df_log.at[0,'album_name'] = self.album_name
                df_log.at[0,'album_id'] = self.album_id
                df_log.to_csv('albums_history.csv')
                #print(df_log)
            else:
                df_log.at[rows, 'artist_id'] = self.artist_id
                df_log.at[rows, 'artist'] = self.artist_name
                df_log.at[rows, 'popularity'] = self.artist_popularity  
                df_log.at[rows,'album_name'] = self.album_name
                df_log.at[rows,'album_id'] = self.album_id
                df_log.to_csv('albums_history.csv')
                #print(df_log)
            #endregion


    def click(self):
        #rn = random.randint(1, 10)
        rn = 1
        if rn <= 4:
            self.artist_id = HighPopularity()
            self.update_artist_data()
            self.update_widgets()
            #print("High popularity!")
        elif (rn > 4) & (rn <= 7):
            self.artist_id = MediumPopularity()
            self.update_artist_data()
            self.update_widgets()
            #print("Medium popularity!")
        elif (rn > 7) & (rn <= 9):
            self.artist_id = LowPopularity()
            self.update_artist_data()
            self.update_widgets()
            #print("Low popularity!")
        else:
            self.artist_id = VeryLowPopularity()
            self.update_artist_data()
            self.update_widgets()
            #print("Very low popularity!")
    def openAlbumLink(self):
        webbrowser.open(self.album_link, new=0, autoraise=True)
    #endregion 

window = GUI(root)
window.click()

root.mainloop()
