import pandas as pd


def preprocess(df,region_df):
   

    # keep only required columns
    region_df = region_df[['NOC', 'region']]

    # remove old region column if already exists
    df = df.drop(columns=['region'], errors='ignore')

    # filter summer olympics
    df = df[df['Season'] == 'Summer']

    # remove duplicates
    df = df.drop_duplicates()

    # merge
    df = df.merge(region_df, on='NOC', how='left')

    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df