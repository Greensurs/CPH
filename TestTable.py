import tkinter as tk
from tkinter import ttk

# Настройки окна
CPH = tk.Tk()
CPH.title("CPH 0.24 TableTest")
CPH.geometry("500x400")


def get_choose():
    result = choose.get()
    # Рассчет количества поршней
    def get_piston():
        sum_piston =  Number.get()
        if int(sum_piston) <= 1000: 
            table_result = ttk.Treeview(CPH)
            table_result['columns']=('Name', 'Result', 'Stacks', 'no_stacks')
            table_result.column('#0', width=0, stretch= "NO")
            table_result.column('Name', width=90)
            table_result.column('Result',  width=90)
            table_result.column('Stacks',  width=90)
            table_result.column('no_stacks', width=90)
            
            table_result.place(x = 65, y = 140)
            
            table_result.heading('#0', text='', )
            table_result.heading('Name', text='Ингредиент')
            table_result.heading('Result', text='Количество')
            table_result.heading('Stacks', text='В стаках')
            table_result.heading('no_stacks', text='Остаток')
            table_result.insert(parent='', index=0, iid=0, text='', values=('Булыжник',int(sum_piston)*4, int(sum_piston)*4//64, int(sum_piston)*4 - int(sum_piston)*4//64*64))
            table_result.insert(parent='', index=1, iid=1, text='', values=('Доски',int(sum_piston)*3,int(sum_piston)*3//64, int(sum_piston)*3 - int(sum_piston)*3//64*64))
            table_result.insert(parent='', index=2, iid=2, text='', values=('Редстоун пыль',sum_piston,int(sum_piston)//64,int(sum_piston) - int(sum_piston)//64*64))
            table_result.insert(parent='', index=3, iid=3, text='', values=('Жел. слитки',sum_piston,int(sum_piston)//64, int(sum_piston) - int(sum_piston)//64*64))
    def get_observer():
        sum_observer =  Number.get()
        if int(sum_observer) <= 1000: 
            table_result = ttk.Treeview(CPH)
            table_result['columns']=('Name', 'Result', 'Stacks', 'no_stacks')
            table_result.column('#0', width=0, stretch= "NO")
            table_result.column('Name', width=90)
            table_result.column('Result',  width=90)
            table_result.column('Stacks',  width=90)
            table_result.column('no_stacks', width=90)
                
            table_result.place(x = 65, y = 140)
                
            table_result.heading('#0', text='', )
            table_result.heading('Name', text='Ингредиент')
            table_result.heading('Result', text='Количество')
            table_result.heading('Stacks', text='В стаках')
            table_result.heading('no_stacks', text='Остаток')
            table_result.insert(parent='', index=0, iid=0, text='', values=('Булыжник',int(sum_observer)*6, int(sum_observer)*6//64, int(sum_observer)*6 - int(sum_observer)*6//64*64))
            table_result.insert(parent='', index=2, iid=2, text='', values=('Редстоун пыль',int(sum_observer)*2,int(sum_observer)*2//64,int(sum_observer) - int(sum_observer)*2//64*64))
            table_result.insert(parent='', index=3, iid=3, text='', values=('кварц',sum_observer,int(sum_observer)//64, int(sum_observer) - int(sum_observer)//64*64))
            
            
            
    if result == resepts[0]:
        # Скрывание
        choose.destroy()
        button_get.destroy()
        # Добавление ввода данных
        
            # Добавление заголовка про количество поршней
        resept = tk.Label(text="Сколько поршней?", width=25, anchor = "w")
        resept.pack()
        resept.place(x = 65, y = 35)
        
            # Добавление места для ввода количества поршней
        Number = tk.Entry(CPH, width = 23)
        Number.pack()
        Number.place(x = 65, y = 65)
        
        buttonPiston = tk.Button(text="Расcчёт", width=15, command=get_piston)
        buttonPiston.pack()
        buttonPiston.place(x = 65, y = 110)
    elif result == resepts[1]:
        choose.destroy()
        button_get.destroy()
        # Добавление ввода данных
        
            # Добавление заголовка про количество поршней
        resept = tk.Label(text="Сколько наблюдателей?", width=35, anchor = "w")
        resept.pack()
        resept.place(x = 65, y = 35)
        
            # Добавление места для ввода количества поршней
        Number = tk.Entry(CPH, width = 23)
        Number.pack()
        Number.place(x = 65, y = 65)
        
        buttonPiston = tk.Button(text="Расcчёт", width=15, command=get_observer)
        buttonPiston.pack()
        buttonPiston.place(x = 65, y = 110)

resource = tk.Label(text="Впиши название ресурса", width=20)
button_get = tk.Button(text="Выбор", width=15, command=get_choose)
resepts = ("Поршень", "Наблюдатель")
choose = ttk.Combobox(CPH, values=resepts)

# Размещение объектов
resource.pack()
choose.pack()
button_get.pack()

# Расположение объектов
button_get.place(x = 280, y = 30)
choose.place(x = 65, y = 35)
CPH.mainloop()