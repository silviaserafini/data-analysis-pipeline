# You have to import all the functions you would you on this
# file to make it work.
# But since we only call to methods of pd.DataFrame, those
# are integrated into the objects.

def tableColumns(df):
    for col in df.columns:
        yield col

def tableValues(df):
    for _,row in df.iterrows():
        yield row 