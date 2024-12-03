import re
import pandas as pd


def print_with_line_breaks(word_list, words_per_line=12):
    for i in range(0, len(word_list), words_per_line):
        print(', '.join(word_list[i:i + words_per_line]))


def process_task1():
    with open('task1-ru.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    capitalized_words_russian = sorted(set(re.findall(r'\b[А-ЯЁ][а-яё]+\b', text)))
    words_after_colon_russian = sorted(set(re.findall(r'\b[а-яёА-ЯЁ]+\b(?=:)', text)))

    print("Уникальные слова на русском языке, начинающиеся с заглавной буквы:")
    print_with_line_breaks(capitalized_words_russian)

    print("\nУникальные слова на русском языке, за которыми следует двоеточие:")
    print_with_line_breaks(words_after_colon_russian)


def process_task2():
    with open('task2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    closing_tags = re.findall(r'</([a-zA-Z][a-zA-Z0-9]*)>', html_content)
    unique_closing_tags = sorted(set(closing_tags))

    print("Все закрывающие теги без повторений:")
    print_with_line_breaks([f"</{tag}>" for tag in unique_closing_tags])


def process_task3():
    with open("task3.txt", "r", encoding="utf-8") as file:
        content = file.read()

    id_pattern = r"\d+"
    last_name_pattern = r"[A-Za-z]+"
    email_pattern = r"[\w\.-]+@[\w\.-]+"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    site_pattern = r"https?://[^\s]+"

    ids = re.findall(id_pattern, content)
    last_names = re.findall(last_name_pattern, content)
    emails = re.findall(email_pattern, content)
    dates = re.findall(date_pattern, content)
    sites = re.findall(site_pattern, content)

    data = list(zip(ids, last_names, emails, dates, sites))

    df = pd.DataFrame(data, columns=["ID", "Last Name", "Email", "Registration Date", "Website"])

    df["ID"] = pd.to_numeric(df["ID"])

    df_sorted = df.sort_values(by="ID")

    print(df_sorted)

    df_sorted.to_csv("task3_sorted.csv", index=False, encoding="utf-8")

    print("task3 saved in : task3_sorted.csv")


def main():
    while True:
        print("Выберите задачу, которую вы хотите выполнить:")
        print("1. Обработка задачи 1 (task1-ru.txt)")
        print("2. Обработка задачи 2 (task2.html)")
        print("3. Обработка задачи 3 (task3.txt)")
        print("0. Выход  ")

        choice = input("Введите номер задачи: ")

        if choice == '1':
            process_task1()
        elif choice == '2':
            process_task2()
        elif choice == '3':
            process_task3()
        elif choice == '0':
            print("Выход")

        else:
            print("Неправильный выбор! Пожалуйста, введите правильный номер.")


if __name__ == "__main__":
    main()
