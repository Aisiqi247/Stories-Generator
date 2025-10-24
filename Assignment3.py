import tkinter as tk
from tkinter import messagebox
import random

class StoryGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("故事生成器")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # 设置颜色和字体
        self.bg_color = "#f0f8ff"
        self.entry_color = "#e6f3ff"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"
        self.title_font = ("Arial", 16, "bold")
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 11)
        self.button_font = ("Arial", 12, "bold")
        
        self.window.configure(bg=self.bg_color)
        
        # 创建界面元素
        self.create_widgets()
        
    def create_widgets(self):
        # 标题
        title_label = tk.Label(self.window, text="故事生成器", 
                              font=self.title_font, bg=self.bg_color, fg=self.text_color)
        title_label.pack(pady=15)
        
        # 说明文字
        instruction_label = tk.Label(self.window, 
                                    text="请在下方填写时间、地点、人物和道具，然后点击生成故事按钮",
                                    font=("Arial", 10), bg=self.bg_color, fg=self.text_color)
        instruction_label.pack(pady=5)
        
        # 创建输入框架
        input_frame = tk.Frame(self.window, bg=self.bg_color)
        input_frame.pack(pady=20)
        
        # 时间输入
        time_label = tk.Label(input_frame, text="时间:", font=self.label_font, 
                             bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        time_label.grid(row=0, column=0, padx=5, pady=10)
        self.time_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color, 
                                  width=20, relief="solid", bd=1)
        self.time_entry.grid(row=0, column=1, padx=5, pady=10)
        self.time_entry.insert(0, "例如：一个阳光明媚的早晨")
        
        # 地点输入
        place_label = tk.Label(input_frame, text="地点:", font=self.label_font, 
                              bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        place_label.grid(row=1, column=0, padx=5, pady=10)
        self.place_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color, 
                                   width=20, relief="solid", bd=1)
        self.place_entry.grid(row=1, column=1, padx=5, pady=10)
        self.place_entry.insert(0, "例如：森林深处")
        
        # 人物输入
        character_label = tk.Label(input_frame, text="人物:", font=self.label_font, 
                                  bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        character_label.grid(row=2, column=0, padx=5, pady=10)
        self.character_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color, 
                                       width=20, relief="solid", bd=1)
        self.character_entry.grid(row=2, column=1, padx=5, pady=10)
        self.character_entry.insert(0, "例如：勇敢的小红帽")
        
        # 道具输入
        item_label = tk.Label(input_frame, text="道具:", font=self.label_font, 
                             bg=self.bg_color, fg=self.text_color, width=8, anchor="e")
        item_label.grid(row=3, column=0, padx=5, pady=10)
        self.item_entry = tk.Entry(input_frame, font=self.entry_font, bg=self.entry_color, 
                                  width=20, relief="solid", bd=1)
        self.item_entry.grid(row=3, column=1, padx=5, pady=10)
        self.item_entry.insert(0, "例如：一把神奇的钥匙")
        
        # 绑定事件，当用户点击输入框时清空默认文本
        self.time_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "例如：一个阳光明媚的早晨"))
        self.place_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "例如：森林深处"))
        self.character_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "例如：勇敢的小红帽"))
        self.item_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, "例如：一把神奇的钥匙"))
        
        # 按钮框架
        button_frame = tk.Frame(self.window, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        # 生成故事按钮
        self.generate_button = tk.Button(button_frame, text="生成故事", font=self.button_font, 
                                       bg=self.button_color, fg="white", relief="raised", 
                                       bd=0, padx=20, pady=8, command=self.generate_story)
        self.generate_button.pack(side=tk.LEFT, padx=10)
        
        # 清空按钮
        clear_button = tk.Button(button_frame, text="清空", font=self.button_font, 
                                bg="#f44336", fg="white", relief="raised", 
                                bd=0, padx=20, pady=8, command=self.clear_entries)
        clear_button.pack(side=tk.LEFT, padx=10)
        
        # 故事显示区域
        story_frame = tk.Frame(self.window, bg=self.bg_color)
        story_frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)
        
        story_label = tk.Label(story_frame, text="生成的故事:", font=self.label_font, 
                              bg=self.bg_color, fg=self.text_color, anchor="w")
        story_label.pack(fill=tk.X)
        
        self.story_text = tk.Text(story_frame, font=("Arial", 11), bg="white", 
                                 fg=self.text_color, wrap=tk.WORD, height=8, 
                                 relief="solid", bd=1, padx=10, pady=10)
        self.story_text.pack(fill=tk.BOTH, expand=True)
        
    def clear_placeholder(self, event, placeholder_text):
        """清空输入框的默认文本"""
        if event.widget.get() == placeholder_text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")  # 设置文本颜色为黑色
    
    def clear_entries(self):
        """清空所有输入框和故事显示区域"""
        self.time_entry.delete(0, tk.END)
        self.place_entry.delete(0, tk.END)
        self.character_entry.delete(0, tk.END)
        self.item_entry.delete(0, tk.END)
        self.story_text.delete(1.0, tk.END)
        
        # 重新设置默认文本
        self.time_entry.insert(0, "例如：一个阳光明媚的早晨")
        self.place_entry.insert(0, "例如：森林深处")
        self.character_entry.insert(0, "例如：勇敢的小红帽")
        self.item_entry.insert(0, "例如：一把神奇的钥匙")
        
        # 设置默认文本颜色为灰色
        self.time_entry.config(fg="gray")
        self.place_entry.config(fg="gray")
        self.character_entry.config(fg="gray")
        self.item_entry.config(fg="gray")
    
    def generate_story(self):
        """生成故事"""
        print("生成故事按钮被点击了！")  # 调试信息
        
        # 获取用户输入
        time = self.time_entry.get().strip()
        place = self.place_entry.get().strip()
        character = self.character_entry.get().strip()
        item = self.item_entry.get().strip()
        
        print(f"输入内容 - 时间: {time}, 地点: {place}, 人物: {character}, 道具: {item}")  # 调试信息
        
        # 检查输入是否为空
        if not time or not place or not character or not item:
            messagebox.showwarning("输入不完整", "请填写所有四个字段！")
            return
        
        # 检查是否是默认文本
        default_texts = ["例如：一个阳光明媚的早晨", "例如：森林深处", 
                        "例如：勇敢的小红帽", "例如：一把神奇的钥匙"]
        
        if time in default_texts or place in default_texts or character in default_texts or item in default_texts:
            messagebox.showwarning("输入无效", "请填写您自己的内容，而不是使用示例文本！")
            return
        
        # 故事模板列表
        story_templates = [
            f"{time}，在{place}，{character}发现了一个神秘的{item}。这个{item}拥有不可思议的力量，它带领{character}踏上了一段奇妙的冒险之旅。在这个过程中，{character}遇到了许多挑战，但凭借智慧和勇气，最终取得了成功。",
            
            f"{character}在{time}来到了{place}。在这里，{character}意外地找到了{item}。凭借这个{item}，{character}解决了一个困扰已久的难题，也让周围的人受益匪浅。",
            
            f"故事发生在{time}的{place}。{character}带着{item}来到这里，展开了一场惊心动魄的探索。最终，{character}通过{item}的力量，实现了自己的愿望，也收获了宝贵的经验。",
            
            f"{time}，{character}在{place}偶遇了{item}。这个{item}改变了{character}的命运，让{character}经历了一段难忘的旅程。这段经历让{character}成长了许多。",
            
            f"在{time}的{place}，{character}使用{item}完成了一项伟大的壮举。这个{item}不仅是工具，更是{character}勇气的象征。故事传开后，大家都被{character}的精神所感动。"
        ]
        
        # 随机选择一个故事模板
        story = random.choice(story_templates)
        print(f"生成的故事: {story}")  # 调试信息
        
        # 清空故事显示区域并显示新故事
        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, story)
        
        # 确保故事显示区域可见
        self.story_text.see(1.0)
    
    def run(self):
        """运行程序"""
        # 初始设置默认文本颜色为灰色
        self.time_entry.config(fg="gray")
        self.place_entry.config(fg="gray")
        self.character_entry.config(fg="gray")
        self.item_entry.config(fg="gray")
        
        self.window.mainloop()

# 创建并运行程序
if __name__ == "__main__":
    app = StoryGenerator()
    app.run()