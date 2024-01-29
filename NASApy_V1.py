from tkinter import *
import requests
import webbrowser

def get_news():
    button_update.pack_forget()
    # Make the text widget editable and clear its content
    text_widget.config(state='normal')
    text_widget.delete("1.0", END)

    # Make a request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        news_title = data['title']
        news_content = data['explanation']
        image_url = data['url']

        # Inserting text into the widget
        text_widget.insert(END, news_title + '\n\n')
        text_widget.insert(END, news_content)

        # Set up the clickable link
        link_label.config(text="last photo we get from space.🪐\n click here to see ✅ ", fg="white", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new(image_url))
    else:
        text_widget.insert(END, "Failed to retrieve data from NASA API")
    
    # Make the text widget read-only again
    text_widget.config(state='disabled')

# Your NASA API key
api_key = 's5wbNzUTiboZEKfFqp0OPnZHhIjmQ08seWUMDABB'

# NASA APOD API URL
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

# Create the main window
root = Tk()
root.title("NASA News")

# Create a Text widget
text_widget = Text(root, height=20, width=50, wrap='word')
text_widget.pack()

# Create a label for the clickable link
link_label = Label(root)
link_label.pack()

# Create an update button
button_update = Button(root, text="Update News", command=get_news)
button_update.pack()

# Initially, make the text widget read-only
text_widget.config(state='disabled')

# Run the application
root.mainloop()
