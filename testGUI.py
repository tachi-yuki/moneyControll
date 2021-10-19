import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
import calendar
import moneycontroller

year_list = ['2020', '2021', '2022', '2023', '2024']
month_list = [str(date).zfill(2) for date in range(1, 13)]
date_list = [str(date).zfill(2) for date in range(1, 32)]


def change_date(item, money):
    last_day = calendar.monthrange(int(cb_year.get()), int(cb_month.get()))[1]
    date = cb_year.get()+'-'+cb_month.get()+'-'+cb_date.get()
    moneycontroller.moneycontrol(date, item, money)
    print("Date = ", date)
    print("item = ", item)
    print("money = ", money)


root = tk.Tk()
root.title('家計簿')

frame1 = ttk.Frame(root, padding=16)
frame2 = ttk.Frame(root, padding=16)
frame3 = ttk.Frame(root, padding=16)

cb_year = ttk.Combobox(frame1, values=year_list, width=5, state='readonly')
cb_year.set(year_list[0])

label_slash1 = ttk.Label(frame1, text='/')

cb_month = ttk.Combobox(frame1, values=month_list, width=5, state='readonly')
cb_month.set(month_list[0])

label_slash2 = ttk.Label(frame1, text='/')

cb_date = ttk.Combobox(frame1, values=date_list, width=5, state='readonly')
cb_date.set(date_list[0])

label_item = ttk.Label(frame2, text='用途')
label_money = ttk.Label(frame2, text='金額')

module = ('ご飯', '勉強', '本', 'ゲーム', 'グッズ', 'その他')
item_entry = ttk.Combobox(frame2, values = module, width = 20)

money = StringVar()
money_entry = ttk.Entry(frame2, textvariable = money, width = 20)

button_save = ttk.Button(frame3, text='保存', command=lambda: change_date(item_entry.get(), money.get()))

frame1.pack()
cb_year.pack(side='left')
label_slash1.pack(side='left')
cb_month.pack(side='left')
label_slash2.pack(side='left')
cb_date.pack(side='left')
frame2.pack()
label_item.pack(side='left')
item_entry.pack(side='left')
label_money.pack(side='left')
money_entry.pack(side='left')
frame3.pack()
button_save.pack(side='bottom')

root.mainloop()
