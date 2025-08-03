import re
import pandas as pd
def process(data):
    lines=data.splitlines()
    pattern = r"^\[(.*?)\] (.*)"
    df = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            datetime_part = match.group(1)  
            message_part = match.group(2)   
            df.append([datetime_part, message_part])
    df_final = pd.DataFrame(df, columns=['datetime', 'name_message'])
    df_final['datetime'] = df_final['datetime'].str.replace(r'\s?(AM|PM)', '', regex=True)
    df_final['datetime'] = pd.to_datetime(df_final['datetime'], format='%d/%m/%y, %H:%M:%S')
    users=[]
    messages=[]
    for i in df_final['name_message']:
        entry=re.split(r'([\w\W]+?):\s',i)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df_final['users']=users
    df_final['messages']=messages
    df_final.drop(columns=['name_message'],inplace=True)
    df_final['year']=df_final['datetime'].dt.year
    df_final['month']=df_final['datetime'].dt.month_name()
    df_final['day']=df_final['datetime'].dt.day
    df_final['hour']=df_final['datetime'].dt.hour
    df_final['minute']=df_final['datetime'].dt.minute
    df_final['date']=df_final['datetime'].dt.date
    df_final['day_name']=df_final['datetime'].dt.day_name()
    period=[]
    for hour in df_final['hour']:
        if hour==12:
            period.append(str(hour)+"- 1")
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df_final['period']=period

    return df_final
