import tkinter as tk
from tkinter import filedialog
from videoPlayer import Player
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.title("流媒体播放器")
        self.geometry("950x550")
        self.create_video_view()
        self.create_control_view()
        self.bind_all("<space>", self.pause_click)

    def create_video_view(self):
        self._canvas = tk.Canvas(self, bg="black", width=800, height=450)
        self._canvas.place(x=150, y=40)
        self.player.set_window(self._canvas.winfo_id())
        tk.Button(self, text="播放/暂停", width=20, command=lambda: self.click(1)).place(x=470, y=500)



    def create_control_view(self):
        frame = tk.Frame(self, width=100, height=1000)
        tk.Button(frame, text="选择视频", width=13, command=lambda: self.click(0)).place(x=0, y=130)
        tk.Button(frame, text="停止", width=13, command=lambda: self.click(2)).place(x=0, y=330)
        frame.place(x=20, y=0)

    def click(self, action):
        if action == 0:
            videoPath = filedialog.askopenfilename()
            self.player.play(videoPath)
        elif action == 1:
            if self.player.get_state() == 1:
                self.player.pause()
            else:
                self.player.resume()
        else:
            self.player.stop()

    def pause_click(self, event):
        if self.player.get_state() == 1:
            self.player.pause()
        else:
            self.player.resume()
        print(self.player.get_position()*self.player.get_length())


if "__main__" == __name__:
    app = App()
    app.mainloop()
