from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворення рядка в об'єкт date
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'.")

    today = datetime.today().date()
    days_difference = (today - given_date).days
    return days_difference

if __name__ == "__main__":
    user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
    try:
        difference = get_days_from_today(user_input)
        print(f"Кількість днів від заданої дати до сьогодні: {difference}")
    except ValueError as e:
        print(e)
