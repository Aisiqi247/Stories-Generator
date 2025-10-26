import tkinter as tk
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import messagebox
import random


class StoryGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Story Generator")
        self.window.geometry("500x400")
        self.window.resizable(False, False)

        # set colors and fonts
        self.bg_color = "#f0f8ff"
        self.entry_color = "#e6f3ff"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"
        self.title_font = ("Arial", 16, "bold")
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 11)
        self.button_font = ("Arial", 12, "bold")

        self.window.configure(bg=self.bg_color)

        # create UI elements
        self.create_widgets()

    def create_widgets(self):
        # title
        title_label = tk.Label(self.window, text="Story Generator",
                               font=self.title_font, bg=self.bg_color, fg=self.text_color)
        title_label.pack(pady=15)

        # instruction text
        instruction_label = tk.Label(self.window,
                                     text="Fill in Time, Place, Character and Item below, then click Generate Story",
                                     font=("Arial", 10), bg=self.bg_color, fg=self.text_color)
        instruction_label.pack(pady=5)

        # input frame
        input_frame = tk.Frame(self.window, bg=self.bg_color)
        input_frame.pack(pady=20)

        # time input
        time_label = tk.Label(input_frame, text="Time:", font=self.label_font,
                              bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        time_label.grid(row=0, column=0, padx=5, pady=10)
        self.time_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color,
                                   width=20, relief="solid", bd=1)
        self.time_entry.grid(row=0, column=1, padx=5, pady=10)
        self.time_entry.insert(0, "e.g.: A sunny morning")

        # place input
        place_label = tk.Label(input_frame, text="Place:", font=self.label_font,
                               bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        place_label.grid(row=1, column=0, padx=5, pady=10)
        self.place_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color,
                                    width=20, relief="solid", bd=1)
        self.place_entry.grid(row=1, column=1, padx=5, pady=10)
        self.place_entry.insert(0, "e.g.: Deep in the forest")

        # character input
        character_label = tk.Label(input_frame, text="Character:", font=self.label_font,
                                   bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        character_label.grid(row=2, column=0, padx=5, pady=10)
        self.character_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color,
                                        width=20, relief="solid", bd=1)
        self.character_entry.grid(row=2, column=1, padx=5, pady=10)
        self.character_entry.insert(0, "e.g.: Brave Little Red Riding Hood")

        # item input
        item_label = tk.Label(input_frame, text="Item:", font=self.label_font,
                              bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        item_label.grid(row=3, column=0, padx=5, pady=10)
        self.item_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color,
                                   width=20, relief="solid", bd=1)
        self.item_entry.grid(row=3, column=1, padx=5, pady=10)
        self.item_entry.insert(0, "e.g.: A magical key")

        # bind events to clear placeholder text when user focuses
        self.time_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "e.g.: A sunny morning"))
        self.place_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "e.g.: Deep in the forest"))
        self.character_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "e.g.: Brave Little Red Riding Hood"))
        self.item_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "e.g.: A magical key"))

        # button frame
        button_frame = tk.Frame(self.window, bg=self.bg_color)
        button_frame.pack(pady=10)

        # generate story button
        self.generate_button = tk.Button(button_frame, text="Generate Story", font=self.button_font,
                                         bg=self.button_color, fg="white", relief="raised",
                                         bd=0, padx=20, pady=8, command=self.generate_story)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        # clear button
        clear_button = tk.Button(button_frame, text="Clear", font=self.button_font,
                                 bg="#f44336", fg="white", relief="raised",
                                 bd=0, padx=20, pady=8, command=self.clear_entries)
        clear_button.pack(side=tk.LEFT, padx=10)

        # story display area
        story_frame = tk.Frame(self.window, bg=self.bg_color)
        story_frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)

        story_label = tk.Label(story_frame, text="Generated Story:", font=self.label_font,
                               bg=self.bg_color, fg=self.text_color, anchor="w")
        story_label.pack(fill=tk.X)

        self.story_text = tk.Text(story_frame, font=("Arial", 11), bg="white",
                                 fg=self.text_color, wrap=tk.WORD, height=8,
                                 relief="solid", bd=1, padx=10, pady=10)
        self.story_text.pack(fill=tk.BOTH, expand=True)

    def clear_placeholder(self, event, placeholder_text):
        """Clear placeholder text from entry"""
        if event.widget.get() == placeholder_text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")  # set text color to black

    def clear_entries(self):
        """Clear all entries and story display"""
        self.time_entry.delete(0, tk.END)
        self.place_entry.delete(0, tk.END)
        self.character_entry.delete(0, tk.END)
        self.item_entry.delete(0, tk.END)
        self.story_text.delete(1.0, tk.END)

        # reset placeholder text
        self.time_entry.insert(0, "e.g.: A sunny morning")
        self.place_entry.insert(0, "e.g.: Deep in the forest")
        self.character_entry.insert(0, "e.g.: Brave Little Red Riding Hood")
        self.item_entry.insert(0, "e.g.: A magical key")

        # set placeholder text color to gray
        self.time_entry.config(fg="gray")
        self.place_entry.config(fg="gray")
        self.character_entry.config(fg="gray")
        self.item_entry.config(fg="gray")

    def generate_story(self):
        """Generate a story"""
        print("Generate Story button clicked!")  # debug

        # get user input
        time = self.time_entry.get().strip()
        place = self.place_entry.get().strip()
        character = self.character_entry.get().strip()
        item = self.item_entry.get().strip()

        print(f"Input - Time: {time}, Place: {place}, Character: {character}, Item: {item}")  # debug

        # check for empty input
        if not time or not place or not character or not item:
            messagebox.showwarning("Incomplete input", "Please fill in all four fields!")
            return

        # check for placeholder/default text
        default_texts = ["e.g.: A sunny morning", "e.g.: Deep in the forest",
                         "e.g.: Brave Little Red Riding Hood", "e.g.: A magical key"]

        if time in default_texts or place in default_texts or character in default_texts or item in default_texts:
            messagebox.showwarning("Invalid input", "Please enter your own content instead of using the example text!")
            return

        # story templates
        story_templates = [
            f"{time}, at {place}, {character} discovered a mysterious {item}. This {item} possessed incredible powers and led {character} on a wondrous adventure. Along the way, {character} faced many challenges, but with wisdom and courage, ultimately succeeded.",

            f"{character} arrived at {place} at {time}. Here, {character} unexpectedly found {item}. With this {item}, {character} solved a long-standing problem and helped those around them.",

            f"The story takes place at {time} in {place}. {character} brought {item} here and embarked on an exhilarating exploration. In the end, {character} used the power of {item} to achieve their wish and gained valuable experience.",

            f"At {time}, {character} met {item} by chance in {place}. This {item} changed {character}'s destiny and led to an unforgettable journey. This experience helped {character} grow a lot.",

            f"At {time} in {place}, {character} used {item} to accomplish a great feat. This {item} was not only a tool but also a symbol of {character}'s courage. When the story spread, everyone was moved by {character}'s spirit."
        ]

        # randomly choose a template
        story = random.choice(story_templates)
        print(f"Generated story: {story}")  # debug

        # display story
        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, story)

        # ensure visible
        self.story_text.see(1.0)

    def run(self):
        """Run the application"""
        # initial: set placeholder text color to gray
        self.time_entry.config(fg="gray")
        self.place_entry.config(fg="gray")
        self.character_entry.config(fg="gray")
        self.item_entry.config(fg="gray")

        self.window.mainloop()


if __name__ == "__main__":
    app = StoryGenerator()
    app.run()