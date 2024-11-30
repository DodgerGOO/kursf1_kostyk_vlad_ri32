from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image as PILImage
from tkinter import messagebox
import os
import json

# Вікно авторизації
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизація")
        self.root.geometry("1920x1080")     


        # Фонова панель
        self.bg = PhotoImage(file=r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\images\login_background.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Панель авторизації
        frame = Frame(self.root, bg="white")
        frame.place(x=100, y=50, width=1600, height=900)   
        
        self.username = Entry(frame, font=("times new roman", 15))
        self.username.place(x=900, y=200, width=200)    
        
        bg_image_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\images\login_background1.png"
        bg_image = PILImage.open(bg_image_path).resize((816, 900))  # Зміна розміру під вікно
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(frame, image=bg_photo)
        bg_label.image = bg_photo  # Зберігаємо посилання на зображення            
        bg_label.place(x=-392, y=0, relwidth=1, relheight=1)      

                       
        panel = Frame(frame, bg="#0096cb")
        panel.place(x=816, y=0, width=785, height=900)
        
        panel = Frame(frame, bg="#84cce3")
        panel.place(x=816, y=0, width=785, height=95)
        
        panel = Frame(frame, bg="#84cce3")
        panel.place(x=816, y=380, width=785, height=95)
        
        panel = Frame(frame, bg="#3ab3d4")
        panel.place(x=816, y=471, width=785, height=8)
        
        panel = Frame(frame, bg="#3ab3d4")
        panel.place(x=816, y=376, width=785, height=8)
        
        panel = Frame(frame, bg="#3ab3d4")
        panel.place(x=816, y=95, width=785, height=8)
        
        panel = Frame(frame, bg="#001423")
        panel.place(x=816, y=480, width=785, height=600)
        
        panel = Frame(frame, bg="#2c3238")
        panel.place(x=816, y=574, width=785, height=8)
        
        panel = Frame(frame, bg="#2c3238")
        panel.place(x=816, y=748, width=785, height=8)
        
        panel = Frame(frame, bg="#000b14")
        panel.place(x=816, y=480, width=785, height=95)      

        panel = Frame(frame, bg="#001c2f")
        panel.place(x=816, y=756, width=785, height=150)    
        
        bg_image_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\images\login_background2.png"
        bg_image = PILImage.open(bg_image_path).resize((500, 300))  # Зміна розміру під вікно
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(frame, image=bg_photo)
        bg_label.image = bg_photo  # Зберігаємо посилання на зображення            
        bg_label.place(x=1185, y=150, relwidth=0.25, relheight=0.13)   
        
        Label(frame, text="F1Racecast", font=("times new roman", 40, "bold"), bg="#0096cb").place(x=1250, y=270)
        
        Label(frame, text="Немає аккаунту?", font=("times new roman", 10, "bold"), bg="#000b14", fg="white").place(x=950, y=492)        
       
        
        
        Label(frame, text="Логін", font=("times new roman", 25, "bold"), bg="#0096cb", fg="white").place(x=850, y=170)
        self.username = Entry(frame, font=("times new roman", 15))
        self.username.place(x=850, y=220, width=300)

        Label(frame, text="Пароль", font=("times new roman", 25, "bold"), bg="#0096cb", fg="white").place(x=850, y=250)
        self.password = Entry(frame, font=("times new roman", 15), show="*")
        self.password.place(x=850, y=300, width=300)

        Button(frame, text="Увійти", command=self.login, font=("times new roman", 15, "bold"), bg="#0096cb", fg="white").place(x=950, y=405, width=100)
        Button(frame, text="Реєстрація", command=self.new_user_register, font=("times new roman", 15), bg="#000b14", fg="white").place(x=950, y=525)
        Button(frame, text="Забули пароль?", command=self.forgot_password, font=("times new roman", 10), bg="#0096cb", fg="white").place(x=1051, y=262)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username == "admin" and password == "admin":
            messagebox.showinfo("Успіх", "Успішний вхід!")
            main_root = Tk()
            main_app = MainApp(main_root)
            main_root.mainloop()
            main_bg_photo = ImageTk.PhotoImage(PILImage.open(r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\images\login_background2.png").resize((1920, 1080)))
            MainApp(self.root, main_bg_photo)
        else:
            messagebox.showerror("Помилка", "Невірний логін або пароль")

    def new_user_register(self):
        """
        Відображення форми для реєстрації нового користувача.
        """
        def register():
            # Отримання даних нового користувача
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            email = entry_email.get()
            phone = entry_phone.get()
            new_username = entry_username.get()
            new_password = entry_password.get()

            if not all([first_name, last_name, email, phone, new_username, new_password]):
                messagebox.showerror("Помилка", "Заповніть усі поля")
            else:
                # Симуляція збереження користувача
                messagebox.showinfo("Успіх", f"Користувач {new_username} успішно зареєстрований")
                register_window.destroy()

        # Нове вікно для реєстрації
        register_window = Toplevel(self.root)
        register_window.title("Реєстрація")
        register_window.geometry("1920x1080")
        
                    
        # Червона панель
        panel = Frame(register_window, bg="#0096cb")
        panel.place(x=760, y=0, width=400, height=550)       
    

        Label(register_window, text="Реєстрація нового користувача", font=("times new roman", 15, "bold")).pack(pady=10)

        # Поля для вводу даних
        Label(register_window, text="Ім'я", font=("times new roman", 12)).pack(pady=5)
        entry_first_name = Entry(register_window, font=("times new roman", 12))
        entry_first_name.pack(pady=5)

        Label(register_window, text="Прізвище", font=("times new roman", 12)).pack(pady=5)
        entry_last_name = Entry(register_window, font=("times new roman", 12))
        entry_last_name.pack(pady=5)

        Label(register_window, text="Електронна пошта", font=("times new roman", 12)).pack(pady=5)
        entry_email = Entry(register_window, font=("times new roman", 12))
        entry_email.pack(pady=5)

        Label(register_window, text="Номер телефону", font=("times new roman", 12)).pack(pady=5)
        entry_phone = Entry(register_window, font=("times new roman", 12))
        entry_phone.pack(pady=5)

        Label(register_window, text="Логін", font=("times new roman", 12)).pack(pady=5)
        entry_username = Entry(register_window, font=("times new roman", 12))
        entry_username.pack(pady=5)

        Label(register_window, text="Пароль", font=("times new roman", 12)).pack(pady=5)
        entry_password = Entry(register_window, font=("times new roman", 12), show="*")
        entry_password.pack(pady=5)

        # Кнопка для реєстрації
        Button(register_window, text="Зареєструватися", command=register, font=("times new roman", 12), bg="green", fg="white").pack(pady=20)
          
        
    def forgot_password(self):
        """
        Відображення форми для скидання пароля.
        """
        def reset_password():
            reset_user = reset_username.get()
            if reset_user == "":
                messagebox.showerror("Помилка", "Введіть ім'я користувача")
            else:
                # Симуляція скидання пароля
                messagebox.showinfo("Скидання пароля", f"Пароль для користувача {reset_user} скинуто!")
                reset_window.destroy()

        # Нове вікно для скидання пароля
        reset_window = Toplevel(self.root)
        reset_window.title("Скидання пароля")
        reset_window.geometry("1920x1080")

        Label(reset_window, text="Скидання пароля", font=("times new roman", 15, "bold")).pack(pady=10)

        Label(reset_window, text="Введіть ваш логін", font=("times new roman", 12)).pack(pady=5)
        reset_username = Entry(reset_window, font=("times new roman", 12))
        reset_username.pack(pady=5)

        Button(reset_window, text="Скинути пароль", command=reset_password, font=("times new roman", 12), bg="blue", fg="white").pack(pady=20)
        

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("F1 Predictions")
        self.root.geometry("1920x1080")
        
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=1920, height=1080)   
        
        self.username = Entry(frame, font=("times new roman", 15))
        self.username.place(x=900, y=200, width=200)
        
        # Кнопки
        Button(self.root, text="Перегляд прогнозів", command=self.view_predictions, font=("times new roman", 20, "bold")).place(x=800, y=100, width=300, height=50)
        Button(self.root, text="Статистика", command=self.view_statistics, font=("times new roman", 20, "bold")).place(x=800, y=200, width=300, height=50)
        Button(self.root, text="Пілоти та команди", command=self.view_drivers_teams, font=("times new roman", 20, "bold")).place(x=800, y=300, width=300, height=50)
        
        
        panel = Frame(frame, bg="#0096cb")
        panel.place(x=700, y=5, width=500, height=500)
          
    def view_predictions(self):
        # Відкриває вікно з прогнозами
        PredictionWindow(self.root)

    def view_statistics(self):
        # Відкриває вікно зі статистикою
        StatisticsWindow(self.root)

    def view_drivers_teams(self):
        # Відкриває вікно з інформацією про пілотів і команди
        DriversTeamsWindow(self.root)



# Вікно прогнозів
class PredictionWindow:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Прогнози")
        self.root.geometry("1920x1080")

        Label(self.root, text="Прогнози на сезон 2025", font=("times new roman", 20, "bold")).pack(pady=20)

        predictions = self.get_predictions()
        if predictions:
            for pred in predictions:
                Label(self.root, text=pred, font=("times new roman", 15)).pack(pady=5)
        else:
            Label(self.root, text="Дані про прогнози відсутні.", font=("times new roman", 15)).pack(pady=20)

    def get_predictions(self):
        file_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\forecast\forecast.json"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                forecast = data.get("forecast", [])
                return [f"{entry['name']}: {entry['details']}" for entry in forecast]
        except FileNotFoundError:
            print(f"Файл не знайдено: {file_path}")
        except json.JSONDecodeError:
            print(f"Помилка декодування JSON у файлі: {file_path}")
        return []


# Вікно статистики
class StatisticsWindow:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Статистика")
        self.root.geometry("1920x1080")

        Label(self.root, text="Статистика сезону 2023", font=("times new roman", 20, "bold")).pack(pady=20)

        # Завантаження даних із JSON-файлу
        self.data = self.load_stats()

        # Вибір Гран-прі
        Label(self.root, text="Оберіть Гран-прі:", font=("times new roman", 15)).pack(pady=10)
        self.grand_prix = ttk.Combobox(self.root, values=[gp["name"] for gp in self.data])
        self.grand_prix.pack(pady=10)
        self.grand_prix.bind("<<ComboboxSelected>>", self.show_statistics)

        self.result_label = Label(self.root, text="", font=("times new roman", 15), justify="left", wraplength=800)
        self.result_label.pack(pady=20)

    def load_stats(self):
        """
        Завантажує дані статистики з JSON-файлу.
        """
        stats_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\stats\stats.json"
        try:
            with open(stats_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("stats", [])
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити дані: {e}")
            return []

    def show_statistics(self, event):
        """
        Відображає статистику для вибраного Гран-прі.
        """
        selected_gp = self.grand_prix.get()
        for gp in self.data:
            if gp["name"] == selected_gp:
                self.result_label.config(text=gp["details"])
                return
        self.result_label.config(text="Дані відсутні.")

# Вікно пілотів та команд
class DriversTeamsWindow:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Пілоти та Команди")
        self.root.geometry("1920x1080")

        Label(self.root, text="Інформація про пілотів і команди", font=("times new roman", 20, "bold")).pack(pady=20)

        # Вибір між пілотами та командами
        Button(self.root, text="Переглянути пілотів", command=self.show_drivers, font=("times new roman", 15)).pack(pady=10)
        Button(self.root, text="Переглянути команди", command=self.show_teams, font=("times new roman", 15)).pack(pady=10)

    def load_data(self, file_path):
        """
        Завантажує дані з JSON-файлу.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити дані: {e}")
            return []

    def show_drivers(self):
        """
        Відображає список пілотів з JSON-файлу.
        """
        pilots_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\pilots\pilots.json"
        data = self.load_data(pilots_path)
        drivers = data.get("drivers", [])  # Перевіряємо, чи є ключ "drivers"

        if not drivers:
            messagebox.showinfo("Інформація", "Список пілотів порожній.")
            return

        list_window = Toplevel(self.root)
        list_window.title("Список пілотів")
        list_window.geometry("1920x1080")

        Label(list_window, text="Список пілотів", font=("times new roman", 20, "bold")).pack(pady=10)

        for driver in drivers:
            Button(
                list_window, 
                text=driver["name"], 
                command=lambda d=driver: self.display_info("Пілот", d), 
                font=("times new roman", 15)
            ).pack(pady=5)

    def show_teams(self):
        """
        Відображає список команд з JSON-файлу.
        """
        teams_path = r"C:\Users\Vlad\Desktop\poly\f1_predictions_system-main\f1_predictions_system\PROJECT\teams\teams.json"
        data = self.load_data(teams_path)
        teams = data.get("teams", [])  # Перевіряємо, чи є ключ "teams"

        if not teams:
            messagebox.showinfo("Інформація", "Список команд порожній.")
            return

        list_window = Toplevel(self.root)
        list_window.title("Список команд")
        list_window.geometry("1920x1080")

        Label(list_window, text="Список команд", font=("times new roman", 20, "bold")).pack(pady=10)

        for team in teams:
            Button(
                list_window, 
                text=team["name"], 
                command=lambda t=team: self.display_info("Команда", t), 
                font=("times new roman", 15)
            ).pack(pady=5)

    def display_info(self, title, data):
        """
        Відображає детальну інформацію про пілота чи команду.
        """
        info_window = Toplevel(self.root)
        info_window.title(data["name"])
        info_window.geometry("1920x1080")

        Label(info_window, text=f"{title}: {data['name']}", font=("times new roman", 20, "bold")).pack(pady=10)
        Label(info_window, text=data["details"], font=("times new roman", 15), wraplength=500, justify=LEFT).pack(pady=10)

# Запуск програми
if __name__ == "__main__":
    root = Tk()
    login_app = LoginWindow(root)
    root.mainloop()

