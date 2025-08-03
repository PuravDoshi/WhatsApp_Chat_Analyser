from urlextract import URLExtract
import pandas as pd 
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from collections import Counter
import emoji

def stats(selected_user,df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    num_messages=df.shape[0]
    words=[]
    for msg in df['messages']:
        words.extend(msg.split())
    links=[]
    extractor=URLExtract()
    for msg in df['messages']:
        links.extend(extractor.find_urls(msg))
    return num_messages, words, links

def busy_user(df):
    x=df['users'].value_counts().head()
    df2=(df['users'].value_counts()/df.shape[0]*100).reset_index().rename(columns={'count':'percent'})
    return x,df2

def create_word_cloud(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    
    wc=WordCloud(width=300, height=300, min_font_size=8, background_color='white')
    df_wc=wc.generate(df['messages'].str.cat(sep=" "))
    return df_wc

def most_used_words(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    w=[]
    for i in df['messages']:
        for word in i.lower().split():
            if word not in stop_words:
                w.append(word)
    df3=pd.DataFrame(Counter(w).most_common(20)).rename(columns={0:'word',1:'count'})
    return df3

def most_used_emoji(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    emojis=[]
    for i in df['messages']:
        for e in i:
            if e in emoji.EMOJI_DATA:
                emojis.append(e)
    return emojis

def message_progress(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    df_prog=df.groupby(['year', 'month']).count()['messages'].reset_index()
    time = []
    for i in range(df_prog.shape[0]):
        time.append(str(df_prog['year'][i]) + "-" + str(df_prog['month'][i]))
    df_prog['time']=time
    df_prog.drop(columns=['year','month'],inplace=True)
    return df_prog

def message_progress_daily(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    df5=df.groupby(['date']).count()['messages'].reset_index()
    return df5

def active_day(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    return df['day_name'].value_counts()

def active_month(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    return df['month'].value_counts()

def heatmap(selected_user, df):
    if selected_user!='Overall':
        df=df[df['users']==selected_user]
    return df