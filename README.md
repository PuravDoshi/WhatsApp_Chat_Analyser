# 📊 WhatsApp Chat Analyser

**Analyse your WhatsApp group or personal chats like never before!**

Turn your raw WhatsApp exported chats into beautiful, interactive visualisations and insights with this **Streamlit-powered dashboard**. Whether you're curious about your most active days, top contributors, most used words, or just want to see who sends the most emojis — this app has you covered!

---

## 🔍 Features

✅ Upload your exported WhatsApp chat (`.txt` file)  
✅ Get **automated group-level and individual-level analytics**  
✅ Stunning, interactive **visualizations using Streamlit and Matplotlib**  

---

### 💡 What You Can Discover

| Analysis | Description |
|----------|-------------|
| 📈 **Messages Over Time** | Visual trend of messages sent across months and years |
| 📆 **Daily Timeline** | Day-wise breakdown of activity |
| 🏆 **Top Stats** | Total messages, total words, total links |
| 🗓️ **Busiest Days** | Find the most active day of the week |
| 🗓️ **Busiest Months** | Discover when the most chatter happened |
| 🔥 **Activity Heatmap** | Hourly activity pattern across all weekdays |
| 💬 **Most Common Words** | What words do people use the most? |
| 😂 **Most Used Emojis** | Who’s the emoji king/queen? |
| 👥 **User-Level Insights** | Per-user breakdown of all the above |

---

## 🛠️ File Structure
```bash
WhatsApp_Chat_Analyser/
│
├── app.py # Main Streamlit app and dashboard layout
├── processor.py # Loads and prepares the WhatsApp data
├── helper.py # Contains core analysis and visualisation logic
└── README.md # You are here!
```


---

## 🚀 How to Run Locally

1. **Clone the repository**  
   git clone https://github.com/PuravDoshi/WhatsApp_Chat_Analyser.git
   cd WhatsApp_Chat_Analyser
2. **Create a virtual environment**
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
3. **Run the App**
    streamlit run app.py

## 📤 How to Export WhatsApp Chat
1. Open WhatsApp on your phone
2. Go to the chat or group you want to analyze
3. Tap on > More > Export Chat
4. Choose Without Media and save/share the .txt file
5. Upload it in the dashboard interface

## 🙌 Contributing
Have ideas? 

Found bugs? 

Want to add a new chart?

We welcome all contributions!

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).


## 🙋‍♂️ Author
Made with ❤️ by Purav Doshi

If you found this project useful, consider ⭐ starring the repo and sharing it!