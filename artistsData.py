import pandas as pd

# Function used for modifying original artists.csv file
def prepareArtistsData():
    df = pd.read_csv("data/artists.csv")
    df = df.drop(columns=["followers","genres"])
    df = df.sort_values("popularity", ascending=False)
    df.to_csv('artists.csv', index=False)
    print(df.head(15))
