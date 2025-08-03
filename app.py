# When you use plt.subplots(), you're creating a Figure (fig) and one or more Axes objects (ax), 
# where each Axes is an individual plot area. By default, calling plt.subplots() without arguments 
# is the same as plt.subplots(1, 1) — it gives you one plotting area. The ax object lets you control 
# the plot more directly (like adding bars, lines, titles, labels, etc.) compared to the simpler plt.plot() 
# or plt.bar(). Using subplots makes your code more flexible — if you later want multiple charts
# (like side-by-side plots), you just change the number of rows/columns. It's especially useful with Streamlit, 
# where st.pyplot(fig) needs a fig object.

# Example:
# fig, ax = plt.subplots(1, 2, figsize=(10, 4))  -- 1 row, 2 columns
# x = [1, 2, 3, 4]
# y1 = [10, 20, 15, 30]
# y2 = [5, 15, 25, 10]

# ax[0].plot(x, y1)           -- First subplot
# ax[0].set_title("Line Plot")

# ax[1].bar(x, y2)            -- Second subplot
# ax[1].set_title("Bar Chart")

# plt.tight_layout()          -- Avoid overlap
# plt.show()

import streamlit as st 
import processor, helper
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyser")
uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=processor.process(data)
    # st.dataframe(df)
    
    user_list=df['users'].unique().tolist()
    user_list=sorted(user_list)
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show analysis with respect to:",user_list)
    if st.sidebar.button("Show Analysis"):
        st.title("Messages sent over time")
        df_prog=helper.message_progress(selected_user, df)
        fig, ax=plt.subplots()
        ax.plot(df_prog['time'],df_prog['messages'], color='green')
        plt.xticks(rotation=90)
        st.pyplot(fig)
        
        st.title("Messages sent per day")
        df_prog2=helper.message_progress_daily(selected_user, df)
        fig, ax=plt.subplots()
        ax.plot(df_prog2['date'],df_prog2['messages'], color='orange')
        plt.xticks(rotation=90)
        st.pyplot(fig)
        
        st.title("Activity Map")
        col1, col2=st.columns(2)
        with col1:
            st.header("Most Active Days")
            z=helper.active_day(selected_user, df)
            fig, ax=plt.subplots()
            ax.bar(z.index, z.values, color='pink')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        with col2:
            st.header("Most Active Months")
            z2=helper.active_month(selected_user, df)
            fig, ax=plt.subplots()
            ax.bar(z2.index, z2.values, color='purple')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        df_last=helper.heatmap(selected_user, df)
        st.title("Period when users are most active")
        fig, ax=plt.subplots()
        pivot=df_last.pivot_table(index='day_name',columns='period',values='messages',aggfunc='count').fillna(0)
        sns.heatmap(pivot, ax=ax)
        st.pyplot(fig)
            
        num_messages, words, links=helper.stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3=st.columns(3)
        with col1:
            st.header("Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(len(words))
        with col3:
            st.header("Total Links")
            st.title(len(links))
            
        if selected_user=='Overall':
            st.title("Busiest Users")
            x, df2=helper.busy_user(df)
            col1, col2=st.columns(2)
            with col1:
                fig, ax=plt.subplots()
                ax.bar(x.index,x.values)
                plt.xticks(rotation=45)
                st.pyplot(fig)
            
            with col2:
                st.dataframe(df2)
        
        df_wc=helper.create_word_cloud(selected_user,df)
        fig,ax=plt.subplots()
        st.title("Worldcloud")
        ax.imshow(df_wc)
        st.pyplot(fig)
        
        most_common_df=helper.most_used_words(selected_user, df)
        st.title("Most Common Words")
        fig, ax=plt.subplots()
        ax.barh(most_common_df['word'],most_common_df['count'], color='red')
        st.pyplot(fig)

        emote=helper.most_used_emoji(selected_user, df)
        x2=pd.DataFrame(emote)
        st.title("Most Common Emojis")
        fig, ax=plt.subplots()
        ax.pie(x2[0].value_counts().values[0:5], labels=x2[0].value_counts().index[0:5], autopct='%0.2f')
        st.pyplot(fig)
        
        
        