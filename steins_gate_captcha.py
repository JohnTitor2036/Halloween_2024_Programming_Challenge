# To compile this script into a Windows executable, use PyInstaller:
# Install PyInstaller: pip install pyinstaller
# Compile: pyinstaller --onefile --windowed steins_gate_captcha.py


import tkinter as tk
from tkinter import messagebox
import random
import os
import sys

world_lines = [
    {
        'title': 'Operation Urd: Experimenting with D-Mails',
        'events': [
            'Discover the PhoneWave (name subject to change) can send messages to the past.',
            'Begin experimenting with sending D-Mails.',
            'Observe changes in the world lines.',
            'Realize the consequences of altering the past.',
            'Face unexpected outcomes from the experiments.'
        ]
    },
    {
        'title': 'Operation Verthandi: Creating the Time Leap Machine',
        'events': [
            'Use the PhoneWave (name subject to change) to develop the Time Leap Machine.',
            'Successfully send consciousness back in time.',
            'Use time leaping to try to save Mayuri.',
            'Decide to erase all previous D-Mails.',
            'Reverse the D-Mails to revert to the Beta Attractor Field.'
        ]
    },
    {
        'title': 'Operation Skuld: Saving Kurisu',
        'events': [
            'Reawaken Hououin Kyouma persona.',
            'Devise a plan to save both Mayuri and Kurisu.',
            'Record a video message to his past self.',
            'Travel back in time using the time machine.',
            'Fake Kurisu’s death to deceive the world line.'
        ]
    },
    {
        'title': 'Operation Arc-Light: Mayuri’s Resolve',
        'events': [
            'Mayuri decides to help Okabe regain his resolve.',
            'Mayuri and Suzuha travel back in time.',
            'Mayuri delivers a message to her past self.',
            'Helps Okabe to get back on his feet.',
            'Prepares Okabe for Operation Skuld.'
        ]
    },
    {
        'title': 'Operation Eldhrimnir: Suzuha’s Farewell Party',
        'events': [
            'Plan to hold a party for Suzuha.',
            'Shop for party supplies and food.',
            'Invite Suzuha to the celebration.',
            'Enjoy the party together.',
            'Say farewell to Suzuha.'
        ]
    },
    {
        'title': 'Operation Vega: Assisting Mayuri and Suzuha',
        'events': [
            'Reawaken as Hououin Kyouma.',
            'Devise a plan to help Mayuri and Suzuha time travel.',
            'Attempt to prevent DURPA’s interference.',
            'Send a D-RINE to prevent Amadeus’ development.',
            'Successfully send Mayuri and Suzuha to the past.'
        ]
    },
    {
        'title': 'Operation Audhumbla: Reassuring Mayuri',
        'events': [
            'Mayuri worries about Okabe’s well-being.',
            'Okabe creates Operation Audhumbla to soothe her.',
            'They go shopping together for Suzuha’s party.',
            'Prepare food and supplies for the celebration.',
            'Enjoy time together, easing Mayuri’s worries.'
        ]
    }
]

class SteinsGateChallenge:
    def __init__(self, future_gadget_lab):
        self.future_gadget_lab = future_gadget_lab
        self.future_gadget_lab.title('Operation: El Psy Kongroo')
        self.future_gadget_lab.geometry('800x600')
        self.future_gadget_lab.configure(bg='#0f0f0f')  # Keep the black background
        self.world_line = random.choice(world_lines)
        self.correct_events = self.world_line['events']
        self.shuffled_events = self.correct_events.copy()
        random.shuffle(self.shuffled_events)
        self.initialize_future_gadgets()

    def initialize_future_gadgets(self):
        operation_title = 'El Psy Kongroo: ' + self.world_line['title']
        title_label = tk.Label(
            self.future_gadget_lab,
            text=operation_title,
            font=('Helvetica', 20, 'bold'),
            bg='#0f0f0f',
            fg='#00ff00',
            wraplength=750,
            justify='center'
        )
        title_label.pack(pady=20)

        self.lab_frame = tk.Frame(self.future_gadget_lab, bg='#0f0f0f')
        self.lab_frame.pack(pady=20)

        self.event_selector = tk.Listbox(
            self.lab_frame,
            selectmode=tk.SINGLE,
            width=80,
            height=len(self.shuffled_events),
            bg='#1a1a1a',
            fg='#00ff00',
            font=('Helvetica', 12)
        )
        for event in self.shuffled_events:
            self.event_selector.insert(tk.END, event)
        self.event_selector.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)

        self.event_selector.bind('<Double-1>', self.shift_event_in_timeline)

        execute_button = tk.Button(
            self.future_gadget_lab,
            text='Execute The Operation',
            command=self.verify_world_line,
            bg='#00ff00',
            activebackground='#00cc00',
            fg='black',
            font=('Helvetica', 14, 'bold')
        )
        execute_button.pack(pady=20)

        instructions_text = 'Double-click to shift events and help Hououin Kyouma reach Steins Gate.'
        instructions_label = tk.Label(
            self.future_gadget_lab,
            text=instructions_text,
            font=('Helvetica', 12),
            bg='#0f0f0f',
            fg='#00ff00'
        )
        instructions_label.pack(pady=10)

    def shift_event_in_timeline(self, event):
        widget = event.widget
        try:
            index = widget.curselection()[0]
            value = widget.get(index)

            if index > 0:
                widget.delete(index)
                widget.insert(index - 1, value)
                widget.selection_set(index - 1)
        except IndexError:
            pass

    def verify_world_line(self):
        user_events = self.event_selector.get(0, tk.END)
        if list(user_events) == self.correct_events:
            messagebox.showinfo('Steins Gate', "We've reached 1.048596%, the Steins Gate world line!")
            self.future_gadget_lab.destroy()
        else:
            messagebox.showerror(
                'World Line Divergence',
                'Failed to reach Steins Gate. Divergence Meter remains below 1%. Try again.'
            )

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

def main():
    future_gadget_lab = tk.Tk()
    _app = SteinsGateChallenge(future_gadget_lab)
    future_gadget_lab.mainloop()

if __name__ == '__main__':
    main()
