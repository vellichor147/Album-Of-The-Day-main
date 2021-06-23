# Album-Of-The-Day

Simple application for discovering new music by using Spotify API to retrive data and randomly generate new album/artist. Application generates new album by randomly picking one artist from artists.csv file where artists are divided in four groups: high popularity, medium popularity, low popularity and very low popularity. Artist's popularity varies in range from 0 to 100 where 100 is the highest popularity score. Artists.csv file was obtained from dataset by Yamac Eren Ay (https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks)  

Prerequisites:
- Spotify account (https://www.spotify.com/)
- Client ID and Client secret for authorization purposes (https://developer.spotify.com/)
- requests (https://pypi.org/project/requests/)
- opencv-python (https://pypi.org/project/opencv-python/)
- Pillow (https://pypi.org/project/Pillow/)
- pandas (https://pypi.org/project/pandas/)  

Install libraries: pip install requests opencv-python Pillow pandas

![image](https://user-images.githubusercontent.com/71836410/123064618-b8cceb00-d40e-11eb-8e3a-d94f58ff48a4.png)

NOTE: Don't forget to enter your client ID and client secret (provided by Spotify) in Authorization.py file, otherwise authorization will not be possible and application won't work!
