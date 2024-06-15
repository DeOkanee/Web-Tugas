import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    save_location = location_entry.get()

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        messagebox.showinfo("Info", f"Unduhan {yt.title} sedang dimulai...")
        stream.download(output_path=save_location)
        messagebox.showinfo("Info", "Unduhan selesai.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def browse_location():
    folder_path = filedialog.askdirectory()
    if folder_path:
        location_entry.delete(0, tk.END)
        location_entry.insert(0, folder_path)

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Pengunduh Video YouTube")

url_label = tk.Label(root, text="URL Video YouTube:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

location_label = tk.Label(root, text="Lokasi Penyimpanan:")
location_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

location_entry = tk.Entry(root, width=50)
location_entry.grid(row=1, column=1, padx=10, pady=5)

browse_button = tk.Button(root, text="Telusuri", command=browse_location)
browse_button.grid(row=1, column=2, padx=10, pady=5)

download_button = tk.Button(root, text="Unduh", command=download_video)
download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
