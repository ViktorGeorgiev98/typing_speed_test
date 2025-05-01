import tkinter as tk
import time
import random


class Typing_Speed(tk):
    def __init__(self):
        super().init__()
        self.title("Typing speed test")
        self.geometry("700x480")
        self.resizable(False, False)

        self.text_to_type = self.StringVar()
        self.text_to_type.set(random.choice(sample_texts))
