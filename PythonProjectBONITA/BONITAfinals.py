import tkinter as tk
import random
from PIL import Image, ImageTk

cards = [
    {"question": "Happy is to Joyful as Sad is to ____?", "choices": ["Depressed", "Angry", "Tired", "Excited"],
     "answer": "Depressed"},
    {"question": "Brave is to Courageous as Cowardly is to ____?", "choices": ["Fearful", "Bold", "Timid", "Weak"],
     "answer": "Fearful"},
    {"question": "Big is to Large as Small is to ____?", "choices": ["Tiny", "Short", "Narrow", "Light"],
     "answer": "Tiny"},
    {"question": "Fast is to Quick as Slow is to ____?", "choices": ["Sluggish", "Lazy", "Late", "Weak"],
     "answer": "Sluggish"},
    {"question": "Smart is to Intelligent as Foolish is to ____?", "choices": ["Ignorant", "Dull", "Naive", "Weak"],
     "answer": "Ignorant"},
    {"question": "Hot is to Cold as Warm is to ____?", "choices": ["Cool", "Freezing", "Mild", "Boiling"],
     "answer": "Cool"},
    {"question": "Light is to Bright as Dark is to ____?", "choices": ["Dim", "Heavy", "Soft", "Pale"],
     "answer": "Dim"},
    {"question": "Angry is to Mad as Calm is to ____?", "choices": ["Peaceful", "Sad", "Tired", "Happy"],
     "answer": "Peaceful"},
    {"question": "Beautiful is to Pretty as Ugly is to ____?", "choices": ["Unattractive", "Plain", "Dull", "Weak"],
     "answer": "Unattractive"},
    {"question": "Near is to Close as Far is to ____?", "choices": ["Distant", "Away", "Remote", "All of these"],
     "answer": "All of these"},
    {"question": "Easy is to Simple as Hard is to ____?",
     "choices": ["Difficult", "Complicated", "Tough", "All of these"], "answer": "All of these"},
    {"question": "Generous is to Benevolent as Selfish is to ____?",
     "choices": ["Greedy", "Mean", "Unkind", "All of these"], "answer": "All of these"},
    {"question": "Lucky is to Fortunate as Unlucky is to ____?", "choices": ["Unfortunate", "Sad", "Depressed", "Weak"],
     "answer": "Unfortunate"},
    {"question": "Bright is to Shiny as Dull is to ____?", "choices": ["Dim", "Dark", "Boring", "All of these"],
     "answer": "All of these"},
    {"question": "Strong is to Powerful as Weak is to ____?",
     "choices": ["Feeble", "Fragile", "Delicate", "All of these"], "answer": "All of these"},
]

word_of_the_day_list = [
    {"word": "Eloquent", "meaning": "Fluent or persuasive in speaking or writing"},
    {"word": "Serendipity", "meaning": "Finding something good without looking for it"},
    {"word": "Resilient", "meaning": "Able to recover quickly from difficulties"},
    {"word": "Ephemeral", "meaning": "Lasting for a very short time"},
    {"word": "Ubiquitous", "meaning": "Present, appearing, or found everywhere"},
    {"word": "Candid", "meaning": "Truthful and straightforward; frank"},
    {"word": "Inevitable", "meaning": "Certain to happen; unavoidable"},
    {"word": "Ambiguous", "meaning": "Open to more than one interpretation"},
    {"word": "Benevolent", "meaning": "Well meaning and kindly"},
    {"word": "Meticulous", "meaning": "Showing great attention to detail"},
    {"word": "Tenacious", "meaning": "Persistent, determined"},
    {"word": "Vivid", "meaning": "Producing strong, clear images"},
    {"word": "Fortuitous", "meaning": "Happening by chance, often lucky"},
    {"word": "Pragmatic", "meaning": "Dealing with things sensibly and realistically"},
    {"word": "Lucid", "meaning": "Expressed clearly and easy to understand"}
]


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Antonyms & Synonyms")
        self.root.geometry("800x650")
        self.root.resizable(False, False)

        self.gradient_canvas = tk.Canvas(self.root, width=800, height=650)
        self.gradient_canvas.pack(fill="both", expand=True)

        self.title_font = ("Arial", 30, "bold")
        self.subtitle_font = ("Arial", 24, "bold")
        self.text_font = ("Arial", 16)
        self.text_italic_font = ("Arial", 16, "italic")
        self.button_font = ("Arial", 18, "bold")

        self.current_index = 0
        self.score = 0

        self.show_dashboard()

        self.show_word_of_the_day()

    def draw_gradient(self, start_color=(255, 255, 255), end_color=(200, 200, 200)):
        self.gradient_canvas.delete("all")
        for i in range(0, 650):
            r = start_color[0] + (end_color[0] - start_color[0]) * i // 650
            g = start_color[1] + (end_color[1] - start_color[1]) * i // 650
            b = start_color[2] + (end_color[2] - start_color[2]) * i // 650
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.gradient_canvas.create_line(0, i, 800, i, fill=color)

    def show_word_of_the_day(self):
        word_data = random.choice(word_of_the_day_list)
        pronunciation = " - ".join([word_data['word'][i:i + 2] for i in range(0, len(word_data['word']), 2)])

        popup = tk.Toplevel(self.root)
        popup.title("Word of the Day")
        beige = "#F5F5DC"
        frame = tk.Frame(popup, bg=beige, width=500, height=300)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="WORD OF THE DAY", font=self.subtitle_font, bg=beige).pack(pady=(15, 5))
        tk.Label(frame, text=word_data['word'], font=self.title_font, bg=beige).pack()
        tk.Label(frame, text=f"Pronunciation: {pronunciation}", font=self.text_italic_font, bg=beige).pack(pady=(5, 10))
        tk.Label(frame, text=f"Meaning:\n{word_data['meaning']}", font=self.text_font, bg=beige, wraplength=450,
                 justify="center").pack(pady=10)
        tk.Button(frame, text="Close", font=self.button_font, command=popup.destroy, bg="#2196F3", fg="white", padx=25,
                  pady=12).pack(pady=10)

        self.root.after(30000, self.show_word_of_the_day)

    def create_modern_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            font=self.button_font,
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2",
            activeforeground="white",
            bd=0,
            relief="flat",
            padx=25,
            pady=12,
            cursor="hand2"
        )
        btn.bind("<Enter>", lambda e: btn.config(bg="#1976D2"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#2196F3"))
        btn.config(command=command)
        btn.pack(pady=20, ipadx=15, ipady=8)
        return btn

    def show_dashboard(self):
        self.clear_root()
        self.current_index = 0
        self.score = 0

        self.draw_gradient(start_color=(255, 255, 180), end_color=(255, 220, 120))

        logo = tk.Label(self.gradient_canvas, text="Same Sense or Reverse Game",
                        font=self.subtitle_font)
        logo.pack(pady=20)

        title = tk.Label(self.gradient_canvas, text="Learn Synonyms and Antonyms",
                         font=self.title_font)
        title.pack(pady=15)

        panel = tk.Frame(self.gradient_canvas, bg="#ffffff", bd=0, relief="flat")
        panel.pack(pady=25, padx=40, fill="x")

        intro_text = (
            "Welcome to the Same Sense or Reverse Game!\n\n"
            "Learn antonyms and synonyms interactively.\n"
            "Each question has multiple choices.\n"
            "Wrong answers will show the correct answer instantly!"
        )
        tk.Label(panel, text=intro_text, font=self.text_font, bg="#ffffff", fg="#333333", justify="center",
                 pady=12).pack(padx=25)

        self.create_modern_button(self.gradient_canvas, "Learn Now", self.show_lessons)

    def show_lessons(self):
        self.clear_root()
        self.draw_gradient(start_color=(180, 220, 255), end_color=(120, 180, 255))

        title = tk.Label(self.gradient_canvas, text="LEARN: ANTONYMS & SYNONYMS",
                         font=self.title_font)
        title.pack(pady=25)

        lesson_frame = tk.Frame(self.gradient_canvas, bg="white", bd=0, relief="flat")
        lesson_frame.pack(pady=25, padx=25, fill="both", expand=True)

        self.img_paths = [
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\ah.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\first.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\examplee.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\one.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\two.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\learnn.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\second.png",
            r"C:\Users\Lhea\PycharmProjects\PythonProjectBONITA\ha.png"
        ]
        self.lesson_images = []
        for path in self.img_paths:
            try:
                img = Image.open(path)
                img = img.resize((500, 300), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.lesson_images.append(photo)
            except Exception as e:
                print(f"Error loading image {path}: {e}")

        self.current_img_index = 0

        self.lesson_img_label = tk.Label(lesson_frame, image=self.lesson_images[self.current_img_index], bg="white")
        self.lesson_img_label.pack(pady=10)

        btn_frame = tk.Frame(lesson_frame, bg="white")
        btn_frame.pack(pady=5)

        prev_btn = tk.Button(btn_frame, text="Previous", font=self.button_font, bg="#2196F3", fg="white",
                             command=self.prev_image)
        prev_btn.pack(side="left", padx=20)
        next_btn = tk.Button(btn_frame, text="Next", font=self.button_font, bg="#2196F3", fg="white",
                             command=self.next_image)
        next_btn.pack(side="left", padx=20)

        self.create_modern_button(self.gradient_canvas, "Start Quiz", self.start_flashcards)
        self.create_modern_button(self.gradient_canvas, "Back to Dashboard", self.show_dashboard)

    def next_image(self):
        self.current_img_index = (self.current_img_index + 1) % len(self.lesson_images)
        self.lesson_img_label.config(image=self.lesson_images[self.current_img_index])

    def prev_image(self):
        self.current_img_index = (self.current_img_index - 1) % len(self.lesson_images)
        self.lesson_img_label.config(image=self.lesson_images[self.current_img_index])

    def start_flashcards(self):
        self.clear_root()
        self.draw_gradient(start_color=(180, 220, 255), end_color=(120, 180, 255))

        if self.current_index >= len(cards):
            self.show_scoreboard()
            return

        self.current_card = cards[self.current_index]
        question_label = tk.Label(self.gradient_canvas,
                                  text=f"Q{self.current_index + 1}. {self.current_card['question']}",
                                  font=self.title_font, wraplength=700, justify="center")
        question_label.pack(pady=30)

        for choice in self.current_card["choices"]:
            self.create_modern_button(self.gradient_canvas, choice, lambda c=choice: self.check_answer(c))

        self.create_modern_button(self.gradient_canvas, "Back to Dashboard", self.show_dashboard)

    def check_answer(self, selected):
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")
        result_window.geometry("450x250")
        result_window.resizable(False, False)
        result_window.config(bg="#ffffff")

        if selected == self.current_card["answer"]:
            msg = "Correct! Well done!"
            self.score += 1
        else:
            msg = f"Incorrect! The right answer is:\n {self.current_card['answer']}"

        tk.Label(result_window, text=msg, font=self.text_font, bg="#ffffff", wraplength=400, justify="center").pack(
            padx=20, pady=30)
        tk.Button(result_window, text="Next Card", font=self.button_font, bg="#2196F3", fg="white",
                  activebackground="#1976D2", activeforeground="white", bd=0, relief="flat",
                  padx=25, pady=12,
                  command=lambda: [result_window.destroy(), self.next_card()]).pack(pady=15)

    def next_card(self):
        self.current_index += 1
        self.start_flashcards()

    def show_scoreboard(self):
        self.clear_root()
        self.draw_gradient(start_color=(180, 220, 255), end_color=(120, 180, 255))

        tk.Label(self.gradient_canvas, text="SCOREBOARD", font=self.title_font).pack(pady=30)
        tk.Label(self.gradient_canvas, text=f"You answered {self.score} out of {len(cards)} correctly!",
                 font=self.text_font).pack(pady=25)

        self.create_modern_button(self.gradient_canvas, "Back to Dashboard", self.show_dashboard)

    def clear_root(self):
        for widget in self.gradient_canvas.winfo_children():
            widget.destroy()


root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
















