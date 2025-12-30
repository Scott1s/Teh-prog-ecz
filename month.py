def get_days_in_month(month_name):
    
    months = {
        "січень": 31,
        "лютий": 28, 
        "березень": 31,
        "квітень": 30,
        "травень": 31,
        "червень": 30,
        "липень": 31,
        "серпень": 31,
        "вересень": 30,
        "жовтень": 31,
        "листопад": 30,
        "грудень": 31
    }
    
    month_lower = month_name.strip().lower()
    
    if month_lower not in months:
        raise ValueError(f"Місяць '{month_name}' не знайдено")
    
    return months[month_lower]


def main():
    try:
        month = input("Введіть назву місяця : ")
        days = get_days_in_month(month)
        print(f"У місяці '{month}' {days} днів.")
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()