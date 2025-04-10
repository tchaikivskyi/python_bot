# PYTHON BOT by InTeam

Консольний помічник для роботи з контактами та нотатками.



## 📦 Встановлення

1. Клонувати репозиторій

```bash
git clone https://github.com/tchaikivskyi/python_bot
cd python_bot
```
2. Створити та активувати віртуальне середовище

```bash
python -m venv .venv
source .venv/bin/activate  
.venv\Scripts\activate # Windows
```
3. Встановити залежності

```bash
pip install -r requirements.txt
```
4. Запуск

```bash
python main.py
```

## 🛠 Команди

Введіть одну з команд, наприклад:


```bash
"contact add" # — додати контакт
"contact edit" # — редагувати контакт
"contact all" # — переглянути всі контакти
"contact search ..." # — пошук контакту
"contact show-birthday" # — дні народження найближчим часом
"note add" # — додати нотатку
"note all" # — переглянути всі нотатки
"note search-by-tag <тег> " # — пошук нотатки за тегом
"note sort-by-tag" # — сортувати нотатки за тегами
"help" # — список всіх доступних команд
"exit / close" # — вихід та збереження даних
```
Збереження даних
```
Контакти та нотатки зберігаються у файлах. Всі зміни автоматично записуються при завершенні сесії (exit / close).
```

---
---
---
---
---

# Інформація для розробників

## Віртуальне середовище

### Створення віртуального середовища
```bash
python -m venv .venv 
``` 
### Активація віртуального середовища
```bash
source .venv/bin/activate
.venv\Scripts\Activate.ps1 # windows
.venv\Scripts\activate.bat # windows
``` 

### Встановлення всіх необхідних залежностей з requirements.txt
```bash
pip install -r requirements.txt 
```
### Збереження списку встановлених залежностей (використовувати після встановлення нових пакетів)
```bash 
pip freeze > requirements.txt 
```

## Робота з git
### Клонування репозиторію
```bash 
git clone https://github.com/tchaikivskyi/python_bot 
cd python_bot
```

### Створити  перейти на свою гілку
```bash
git checkout -b 'назва вашої гілки' 
```

### Додавання змін до коміту
```bash 
git add . 
```
### Створення коміту зі змінами
``` bash
git commit -m "ваш коміт"
 ```

### Отримання змін з віддаленої основної гілки (main) у вашу локальну гілку
``` bash
git checkout 'назва вашої гілки'
 ``` 
переконайтесь, що ви у своїй гілці

### підтягування змін з main

``` bash 
git pull origin main
```   
### Після цього вирішіть конфлікти (якщо є) і зробіть новий коміт

### Відправка своєї гілки на GitHub
``` bash
git push origin 'назва вашої гілки'
 ```

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