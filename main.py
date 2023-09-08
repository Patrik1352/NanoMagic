import tkinter as tk
import catboost

def update_scale_from_text(text_widget, scale_widget):
    try:
        value = float(text_widget.get())
        if scale_widget == scale1:
            if 20 <= value <= 1000:
                scale1.set(value)
        elif scale_widget == scale2:
            if 0.05 <= value <= 2:
                scale2.set(value)
        elif scale_widget == scale3:
            if 0 <= value <= 5000:
                scale3.set(value)
    except ValueError:
        pass

def update_text_from_scale(scale_value, text_widget):
    text_widget.delete(0, tk.END)
    text_widget.insert(0, scale_value)

def calculate_values():
    scale1_value = scale1.get()
    scale2_value = scale2.get()
    scale3_value = scale3.get()

    cat = catboost.CatBoostRegressor(iterations=200)
    cat.load_model('model.cbm')

    text4.delete(0, tk.END)
    text4.insert(0, round(cat.predict([[scale3_value, scale1_value, scale2_value]])[0], 4))

# Создание главного окна
root = tk.Tk()
root.geometry("800x300")
root.title("Расчет размера наночастицы")

# Создание Scale виджетов
scale1 = tk.Scale(root, from_=20, to=1000, orient="horizontal", command=lambda value: update_text_from_scale(value, text1))
scale2 = tk.Scale(root, from_=0.05, to=2, orient="horizontal", command=lambda value: update_text_from_scale(value, text2),
                  digits=3, resolution=0.01)
scale3 = tk.Scale(root, from_=0, to=5000, orient="horizontal", command=lambda value: update_text_from_scale(value, text3))

# Создание текстовых полей
text1 = tk.Entry(root)
text2 = tk.Entry(root)
text3 = tk.Entry(root)

# Создание кнопки "Рассчитать"
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_values)

label_variable1 = tk.Label(root, text="Амплитуда напояженности магнитного поля, А/м")
label_variable2 = tk.Label(root, text="Частота магнитного поля, Гц")
label_variable3 = tk.Label(root, text="Удельный коэффициент поглощения, Вт/кг")

text4 = tk.Entry(root)
# Размещение виджетов на главном окне
label_variable1.grid(column=0, row=0)
label_variable2.grid(column=1, row=0)
label_variable3.grid(column=2, row=0)
scale1.grid(column=0, row=2)
text1.grid(column=0, row=1)
scale2.grid(column=1, row=2)
text2.grid(column=1, row=1)
scale3.grid(column=2, row=2)
text3.grid(column=2, row=1)
calculate_button.grid(column=1, row=3)
text4.grid(column=1, row=4)

# Обновление текстовых полей при вводе
text1.bind("<FocusOut>", lambda event: update_scale_from_text(text1, scale1))
text2.bind("<FocusOut>", lambda event: update_scale_from_text(text2, scale2))
text3.bind("<FocusOut>", lambda event: update_scale_from_text(text3, scale3))

# Запуск главного цикла
root.mainloop()
