import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
from tkinter import ttk
import yt_dlp
import threading

# Determine base path depending on whether we're frozen (exe) or not
if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys._MEIPASS)  # _MEIPASS is the temp folder where PyInstaller stores data
else:
    BASE_PATH = Path(__file__).resolve().parent

FFMPEG_DIR = BASE_PATH / "bin"                 # Folder with ffmpeg.exe and ffprobe.exe
ASSETS_PATH = BASE_PATH / "assets" / "frame0"  # Folder with image files

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

def select_directory():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        entry_2.delete(0, 'end')
        entry_2.insert(0, selected_directory)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def update_progress_bar(progress_bar):
    for i in range(101):
        progress_bar['value'] = i
        window.update_idletasks()
        progress_bar.after(10)

def download_mp3():
    url = entry_1.get()
    output_path = entry_2.get()
    if not url or not output_path:
        messagebox.showerror("Error", "Please provide both YouTube URL and output path.")
        return
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ffmpeg_location': str(FFMPEG_DIR),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        threading.Thread(target=update_progress_bar, args=(progress_bar,)).start()
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        progress_bar['value'] = 100
        messagebox.showinfo("Success", "Downloaded and converted to MP3 successfully!")
        progress_bar['value'] = 0
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

window = Tk()
window.title("Welcome: Sound Saver")
window.configure(bg="#FFFFFF")
window_width, window_height = 350, 490
center_window(window, window_width, window_height)

canvas = Canvas(window, bg="#FFFFFF", height=490, width=350, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate", maximum=100)
progress_bar.place(x=25, y=112)
progress_bar.configure(style="green.Horizontal.TProgressbar")
style = ttk.Style()
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(175.0, 245.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(175.0, 70.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
canvas.create_image(182.0, 69.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(306.0, 69.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
canvas.create_image(58.0, 69.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
canvas.create_image(182.0, 177.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
canvas.create_image(62.0, 248.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
canvas.create_image(73.0, 348.0, image=image_image_8)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_directory,
    relief="flat"
).place(x=294.0, y=333.0, width=25.0, height=25.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(175.0, 279.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=25.0, y=264.0, width=300.0, height=28.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(175.0, 379.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_2.place(x=25.0, y=364.0, width=300.0, height=28.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=download_mp3,
    relief="flat"
).place(x=115.0, y=424.0, width=120.0, height=50.0)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
canvas.create_image(181.0, 217.0, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
canvas.create_image(335.0, 477.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
canvas.create_image(57.0, 478.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
canvas.create_image(15.0, 474.0, image=image_image_12)

window.resizable(False, False)
window.mainloop()
