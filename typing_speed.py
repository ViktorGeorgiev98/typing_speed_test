import tkinter as tk
import time
import random
from sample_texts import sample_texts


class Typing_Speed(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.geometry("800x500")
        self.resizable(False, False)

        self.text_to_type = tk.StringVar()
        self.text_to_type.set(random.choice(sample_texts))

        self.start_time = None
        self.remaining_time = 60
        self.timer_running = False
        self.timer_id = None

        # Widgets
        tk.Label(self, text="Typing Speed Test", font=("Arial", 24)).pack(pady=10)

        self.sample_label = tk.Label(
            self,
            textvariable=self.text_to_type,
            wraplength=700,
            font=("Arial", 14),
            fg="gray",
        )
        self.sample_label.pack(pady=20)

        self.entry = tk.Text(self, height=6, width=90, font=("Courier", 12))
        self.entry.pack()
        self.entry.bind("<Key>", self.start_timer)

        self.timer_label = tk.Label(self, text="Time: 60s", font=("Arial", 14))
        self.timer_label.pack(pady=5)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack()

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event=None):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.countdown()

    def countdown(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time: {self.remaining_time}s")
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.countdown)
        else:
            self.timer_running = False
            self.calculate_results()

    def calculate_results(self):
        typed_text = self.entry.get("1.0", tk.END).strip()
        word_count = len(typed_text.split())
        wpm = word_count  # since it's per 60 seconds

        accuracy = self.calculate_accuracy(typed_text)

        self.result_label.config(
            text=f"Your speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )

        # Add Reset button after the test is over
        self.reset_button.config(text="New Test", command=self.reset)

    def calculate_accuracy(self, typed_text):
        original = self.text_to_type.get().split()
        typed = typed_text.split()
        correct = sum(1 for o, t in zip(original, typed) if o == t)
        return (correct / len(original)) * 100 if original else 0

    def reset(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)

        self.timer_running = False
        self.remaining_time = 60
        self.start_time = None
        self.text_to_type.set(random.choice(sample_texts))
        self.timer_label.config(text="Time: 60s")
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.reset_button.config(text="Reset", command=self.reset)
