# coding:utf8
import platform
import tkinter as tk
from tkinter import ttk


class MyGUI(tk.Tk):
    def __init__(self, processor):
        super().__init__()
        self.ctrl_i = 0
        if 'Windows' == platform.system():
            self.iconbitmap(processor.configurator.config['ICONS']['app'])
        self.title('less word')
        self.processor = processor
        self.batch_flag = 0
        self.batch_size = 10
        self.x = 950
        self.y = 800
        self.attributes("-alpha", 0.98)
        self.geo_conf = str(self.x) + 'x' + str(self.y)
        self.geometry(self.geo_conf)
        self.resizable(width=False, height=False)
        self.build()
        self.fresh_word()
        self.fresh_current_batch()
        self.mainloop()

    def word_list_click(self, *args):
        cur_s = self.word_list.curselection()
        if not cur_s:
            return
        name = self.word_list.get(cur_s).split('.')[1]
        while self.target_word_name.get():
            self.target_word_name.delete(0)
        self.target_word_name.insert(tk.END, name)
        self.fresh_word()

    def fresh_word_batch(self, word_batch):
        while self.word_list.size() > 0:
            self.word_list.delete(tk.END)
        for i, word in zip(range(len(word_batch)), word_batch):
            self.word_list.insert(tk.END, str(i + 1) + '.' + word['name'][0])

    def fresh_current_batch(self):
        word_dict = list(self.processor.myDict.value.values())
        if len(word_dict) < self.batch_flag + self.batch_size:
            self.next_word_batch()

    def init_word_batch(self):
        word_dict = list(self.processor.myDict.value.values())
        self.fresh_word_batch(
            word_dict[self.batch_flag:self.batch_flag + self.batch_size])

    def previous_word_batch(self):
        word_dict = list(self.processor.myDict.value.values())
        stop = self.batch_flag - self.batch_size
        while stop <= 0:
            stop += self.batch_size
        start = stop - self.batch_size
        current_batch = word_dict[start:stop]
        self.fresh_word_batch(current_batch)
        self.batch_flag = stop

    def next_word_batch(self):
        word_dict = list(self.processor.myDict.value.values())
        start = self.batch_flag + self.batch_size
        while start > len(word_dict):
            start -= self.batch_size
        stop = start + self.batch_size
        current_batch = word_dict[start:stop]
        self.fresh_word_batch(current_batch)
        self.batch_flag = stop

    def fresh_word(self, *args):
        if self.target_word_name:
            target_word = self.target_word_name.get()
        else:
            target_word = self.processor.word.name
        self.processor.word.name = target_word
        self.set_word_name()
        self.set_word_interpretation()
        self.set_word_eg_sentences()
        self.fresh_current_batch()

    def set_word_name(self):
        self.target_word_display.set(self.processor.word.name)

    def set_word_interpretation(self):
        word_interpretation = ''
        for one_interpretation in self.processor.word.interpretation:
            word_interpretation += '\n' + one_interpretation
        word_interpretation += '\n'
        self.target_word_interpretation.set(word_interpretation)

    def set_word_eg_sentences(self):
        self.target_word_sentences.config(state=tk.NORMAL)
        self.target_word_sentences.delete(0.0, tk.END)
        list_len = len(self.processor.word.example_sentences)
        es_str = '\n'
        for i, example_sentence in zip(range(list_len), self.processor.word.example_sentences):
            if i % 2 == 0:
                es_str = '\n' + str(int(i / 2 + 1)) + '.' + example_sentence
                self.target_word_sentences.insert(tk.END, es_str)
            else:
                es_str = '\n' + ' ' * 3 + example_sentence + '\n'
                self.target_word_sentences.insert(tk.END, es_str)
        self.target_word_sentences.config(state=tk.DISABLED)

    def build(self):
        main_padx = 3
        main_pady = 3
        self.pre_data = self.init_data()
        main_frame = tk.Frame(self, bg='#E3EDCD', width=self.x -
                              main_padx * 2, height=self.y - 2 * main_pady)
        left_frame = tk.Frame(main_frame, bg='#C7EDCC', width=640, height=790)
        right_frame = tk.Frame(main_frame, bg='#C7EDCC', width=310, height=790)
        main_frame.grid_propagate(0)
        main_frame.grid(
            padx=3,
            pady=3,
            sticky=(tk.N, tk.E, tk.S, tk.W)
        )
        left_frame.grid_propagate(0)
        left_frame.grid(
            column=0,
            row=0,
            sticky=tk.W,
            padx=1
        )
        right_frame.grid_propagate(0)
        right_frame.grid(
            column=1,
            row=0,
            sticky=tk.N,
            padx=1
        )
        self.build_left_frame(left_frame)
        self.build_right_frame(right_frame)

    def get_img(self, name, getter=None):
        if getter is None:
            getter = self.processor.configurator.config
        name_l = name.split('.')
        img_path = getter
        for name in name_l:
            img_path = img_path[name]
        return tk.PhotoImage(file=img_path)

    def init_data(self):
        img = {
            'search_bg_img': self.get_img('ICONS.search_0'),
            'go_previous_bg_img': self.get_img('ICONS.go_pre_0'),
            'go_next_bg_img': self.get_img('ICONS.go_next_0'),
            'fill_bg_img': self.get_img('ICONS.fill_0'),
        }
        return img

    def build_left_frame(self, master):
        # search Entry
        self.target_word_name = ttk.Entry(
            master,
            width=28,
            font=('Ostrich Sans', 30),
        )
        self.target_word_name.grid(
            column=0,
            row=0,
            columnspan=8,
            sticky=(tk.EW),
            pady=2,
            padx=1
        )
        self.target_word_name.bind('<Return>', self.fresh_word)
        # search Button
        tk.Button(
            master,
            image=self.pre_data['search_bg_img'],
            borderwidth=0,
            relief='ridge',
            command=self.fresh_word
        ).grid(
            column=8,
            row=0,
            columnspan=2,
            sticky=(tk.EW),
            pady=1,
            padx=1
        )
        # display the target word
        # target word
        self.target_word_display = tk.StringVar()
        tk.Label(
            master,
            textvariable=self.target_word_display,
            font=('Ostrich Sans', 40),
            background='#C7EDCC',
            justify=tk.LEFT,
            anchor=tk.W
        ).grid(
            column=0,
            row=1,
            columnspan=10,
            sticky=(tk.EW),
            pady=2,
            padx=1
        )
        # target word interpretation
        # info
        tk.Label(
            master, text='interpretation:', font=('楷体', 19), background='Lavender', justify=tk.LEFT, anchor=tk.W
        ).grid(
            column=0, row=2, columnspan=10, sticky=(tk.EW), pady=2, padx=1
        )
        # interpretation
        self.target_word_interpretation = tk.StringVar()
        tk.Label(
            master,
            textvariable=self.target_word_interpretation,
            font=('Ostrich Sans', 18),
            background='#C7EDCC',
            wraplength=640,
            justify=tk.LEFT,
            anchor=tk.W
        ).grid(
            column=0,
            row=3,
            columnspan=10,
            sticky=(tk.EW),
            pady=2,
            padx=1
        )
        # target word example sentences
        # info
        tk.Label(
            master, text='example sentences:', font=('楷体', 19), background='Lavender', justify=tk.LEFT, anchor=tk.W
        ).grid(
            column=0, row=4, columnspan=10, sticky=(tk.EW), pady=2, padx=1
        )
        # example sentences frame
        master.rowconfigure(5, weight=1)
        master.update()
        self.target_word_sentences = tk.Text(
            master,
            borderwidth=0,
            font=('Ostrich Sans', 19),
            width=0,
            wrap=tk.WORD,
            bg='#C7EDCC'
        )
        self.target_word_sentences.grid(
            column=0,
            row=5,
            columnspan=10,
            sticky=tk.NSEW
        )

    def build_right_frame(self, master):
        # use a listbox to display words
        list_frame = tk.Frame(master, bg='Lavender', width=300, height=750)
        list_frame.grid_propagate(0)
        list_frame.grid(
            column=0,
            row=0,
            pady=2,
        )
        self.word_list = tk.Listbox(
            list_frame,
            borderwidth=0,
            highlightthickness=0,
            selectbackground='#C7EDCC',
            selectforeground='blue',
            font=('Ostrich Sans', 19),
            width=300,
            height=40,
            bg='#C7EDCC'
        )
        self.word_list.grid(
            column=0,
            row=0,
        )
        # bind event
        self.word_list.bind('<Double-Button-1>', self.word_list_click)
        # two button to go previous or next
        button_frame = tk.Frame(
            master,
            bg='Lavender',
            width=300,
            height=36
        )
        button_frame.grid_propagate(0)
        button_frame.grid(
            column=0,
            row=1,
        )
        # button go previous
        tk.Button(
            button_frame,
            image=self.pre_data['go_previous_bg_img'],
            borderwidth=0,
            relief='ridge',
            command=self.previous_word_batch
        ).grid(
            column=0,
            row=0,
            columnspan=1,
            sticky=(tk.N, tk.W),
        )
        commands = [self.ctrl_c, self.ctrl_t, self.ctrl_r, self.ctrl_l]
        text_ctrl = ['c', 't', 'r', 'l']
        for i, command in zip(range(4), commands):
            tk.Button(
                button_frame,
                text=text_ctrl[i],
                font=('', 19),
                fg='blue',
                command=command,
                compound='center',
                image=self.pre_data['fill_bg_img'],
                bd=0,
                padx=0,
                pady=0,
            ).grid(
                column=i + 2,
                row=0,
                sticky=tk.NS,
            )
        # button go next
        tk.Button(
            button_frame,
            image=self.pre_data['go_next_bg_img'],
            borderwidth=0,
            relief='ridge',
            command=self.next_word_batch
        ).grid(
            column=6,
            row=0,
            columnspan=1,
            sticky=(tk.N, tk.W),
        )

    def ctrl_c(self):
        self.ctrl_i = 1

    def ctrl_t(self):
        if self.ctrl_i != 1:
            self.ctrl_i = 0
            return
        self.ctrl_i += 1

    def ctrl_r(self):
        if self.ctrl_i != 2:
            self.ctrl_i = 0
            return
        self.ctrl_i += 1

    def ctrl_l(self):
        if self.ctrl_i < 3:
            self.ctrl_i = 0
            return
        if self.ctrl_i < 7:
            self.ctrl_i += 1
            return
        self.processor.myDict.flush()
        self.next_word_batch()
