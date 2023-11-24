import tkinter as tk
import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'quit':
                break
            message_listbox.insert(tk.END, message)
        except ConnectionAbortedError:
            break

def send_message(event=None):
    message = my_message.get()
    if message:
        message_listbox.insert(tk.END, f"You: {message}")
        client_socket.send(bytes(message, 'utf-8'))
        my_message.set("")

def on_closing(event=None):
    my_message.set("quit")
    send_message()
    client_socket.close()
    root.quit()

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    root = tk.Tk()
    root.title("Chat Client")

    username_label = tk.Label(root, text="Enter your username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    message_frame = tk.Frame(root)
    my_message = tk.StringVar()
    my_message.set("")
    scrollbar = tk.Scrollbar(message_frame)
    message_listbox = tk.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    message_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    message_listbox.pack()
    message_frame.pack()

    entry_field = tk.Entry(root, textvariable=my_message)
    entry_field.bind("<Return>", send_message)
    entry_field.pack()
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

if __name__ == "__main__":
    start_client()
