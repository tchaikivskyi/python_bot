# PYTHON BOT by InTeam
A Python bot project developed collaboratively by the InTeam team.


## Віртуального середовище

### Створення віртуального середовища
``` python -m venv .venv ```
### Активація віртуального середовища
``` source .venv/bin/activate ``` - mac або linux

``` .venv\Scripts\Activate.ps1 ``` - windows

``` .venv\Scripts\activate.bat ``` - windows
### Встановлення всіх необхідних залежностей з requirements.txt
``` pip install -r requirements.txt ```
### Збереження списку встановлених залежностей (використовувати після встановлення нових пакетів)
``` pip freeze > requirements.txt ```
####

## Робота з git
### Клонування репозиторію
``` git clone https://github.com/tchaikivskyi/python_bot ```

``` cd python_bot ```

### Створити  перейти на свою гілку
``` git checkout -b 'назва вашої гілки' ```

### Додавання змін до коміту
``` git add . ```
### Створення коміту зі змінами
``` git commit -m "ваш коміт" ```

### Отримання змін з віддаленої основної гілки (main) у вашу локальну гілку
``` git checkout 'назва вашої гілки' ``` - переконайтесь, що ви у своїй гілці

``` git pull origin main ```  - підтягування змін з main
### Після цього вирішіть конфлікти (якщо є) і зробіть новий коміт

### Відправка своєї гілки на GitHub
``` git push origin 'назва вашої гілки' ```

### Відправка своєї гілки на GitHub
1. Кожен учасник працює у своїй гілці, яка має назву відповідно до його імені (git branch your_name).
2. Не вносьте зміни напряму в main. Усі зміни додаються через Pull Request (PR).
3. Щоб додати свій код у main, потрібно:
    - Переконатися, що в гілці main є останні зміни (git pull origin main).
    - Об'єднати ці зміни у свою гілку (як описано вище).
    - Відправити свою гілку на GitHub (git push origin your_branch_name).
    - Створити Pull Request з вашої гілки у main.
### Інструкція як створити Pull Request:
[ GitHub Docs – About pull requests]()