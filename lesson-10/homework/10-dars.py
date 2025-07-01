##HOMEWORK 10

#1
from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, status="pending"):
        self.title = title
        self.description = description
        self.due_date = due_date  # kutilayotgan datetime obyekt
        self.status = status      # "pending", "in progress", "completed"

    def mark_completed(self):
        self.status = "completed"

    def update_status(self, new_status):
        if new_status in ["pending", "in progress", "completed"]:
            self.status = new_status
        else:
            raise ValueError("Yaroqsiz status: faqat 'pending', 'in progress' yoki 'completed' bo'lishi mumkin.")

    def is_overdue(self):
        if self.due_date and datetime.now() > self.due_date:
            return True
        return False

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "Mavjud emas"
        return f"📌 {self.title} — {self.status.upper()}\n📝 {self.description}\n⏰ Tugash vaqti: {due}\n"
    
    # datetime kutubxonasini chaqirish
from datetime import datetime, timedelta

# Task yaratish
task1 = Task(
    title="Loyiha yakunlash",
    description="ToDoList loyihasini tugatish va testdan o‘tkazish",
    due_date=datetime.now() + timedelta(days=2)
)

print(task1)

# Statusni o‘zgartirish
task1.update_status("in progress")
print("\nHolati yangilandi:")
print(task1)

# Bajarildi deb belgilash
task1.mark_completed()
print("\nTopshiriq bajarildi:")
print(task1)

# Tugash muddati o‘tib ketganmi?
print("\nTugash muddati o‘tib ketgan:", task1.is_overdue())


#2
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    
    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✔️" if task["completed"] else "✘"
            print(f"{i}. {task['task']} [{status}]")

    def show_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task["completed"]:
                print(f"{i}. {task['task']} [✘]")

# Bu yerda class tugaganidan keyin ishlatish kerak:
todo = ToDoList()
todo.add_task("Dars qilish")
todo.add_task("Mashq bajarish")

print("Barcha vazifalar:")
todo.list_tasks()

print("\n1-vazifa bajarildi:")
todo.mark_complete(0)

print("\nYangi holat:")
todo.list_tasks()

print("\nBajarilmagan vazifalar:")
todo.show_incomplete_tasks()




#3
from datetime import datetime

# ===== 1. TASK SINFI =====
class Task:
    def __init__(self, title, description="", due_date=None, status="pending"):
        self.title = title
        self.description = description
        self.due_date = due_date  # datetime obyekt bo'lishi kerak
        self.status = status      # "pending", "in progress", "completed"

    def mark_completed(self):
        self.status = "completed"

    def is_overdue(self):
        if self.due_date and datetime.now() > self.due_date:
            return True
        return False

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "Mavjud emas"
        overdue_note = " (⏰ KECHIKKAN!)" if self.is_overdue() and self.status != "completed" else ""
        return f"{self.title} — {self.status.upper()}{overdue_note}\n📝 {self.description}\n⏰ Tugash muddati: {due}\n"

# ===== 2. TODOLIST SINFI =====
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("❗️ Noto‘g‘ri indeks.")

    def list_tasks(self):
        if not self.tasks:
            print("📭 Hozircha hech qanday vazifa yo‘q.")
            return
        for i, task in enumerate(self.tasks):
            print(f"[{i}] {task}")


    def show_incomplete_tasks(self):
        incomplete_found = False
        for i, task in enumerate(self.tasks):
            if task.status != "completed":
                print(f"[{i}] {task}")
                incomplete_found = True
        if not incomplete_found:
            print("✅ Bajarilmagan vazifalar yo‘q!")

# ===== 3. MAIN() FUNKSIYASI =====
def main():
    todo = ToDoList()

    while True:
        print("\n=== ToDo CLI Menu ===")
        print("1. Vazifa qo‘shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Bajarilmagan vazifalarni ko‘rish")
        print("5. Chiqish")

        tanlov = input("Tanlovni kiriting (1-5): ")

        if tanlov == "1":
            sarlavha = input("📝 Sarlavhani kiriting: ")
            tavsif = input("📌 Tavsif (ixtiyoriy): ")
            sana_str = input("📅 Tugash muddati (YYYY-MM-DD HH:MM) [ixtiyoriy]: ")
            sana = None
            if sana_str:
                try:
                    sana = datetime.strptime(sana_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("❗️ Sana noto‘g‘ri formatda. Muddatsiz qo‘shiladi.")
            task = Task(title=sarlavha, description=tavsif, due_date=sana)
            todo.add_task(task)
            print("✅ Vazifa qo‘shildi.")

        elif tanlov == "2":
            try:
                index = int(input("🔢 Qaysi vazifa bajarildi? Indeksini kiriting: "))
                todo.mark_complete(index)
                print("✅ Vazifa bajarildi deb belgilandi.")
            except ValueError:
                print("❗️ Raqam kiriting.")

        elif tanlov == "3":
            print("\n📋 Barcha vazifalar:")
            todo.list_tasks()

        elif tanlov == "4":
            print("\n📋 Faqat bajarilmagan vazifalar:")
            todo.show_incomplete_tasks()

        elif tanlov == "5":
            print("🔚 Chiqilmoqda... Yaxshi kunlar tilaymiz! 👋")
            break

        else:
            print("❗️ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

# ===== 4. DASTURNI ISHGA TUSHIRISH =====
if __name__ == "__main__":
    main()

#4

from datetime import datetime, timedelta

# === Task sinfi ===
class Task:
    def __init__(self, title, description="", due_date=None, status="pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_completed(self):
        self.status = "completed"

    def is_overdue(self):
        if self.due_date and datetime.now() > self.due_date:
            return True
        return False

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "Mavjud emas"
        overdue_note = " (⏰ KECHIKKAN!)" if self.is_overdue() and self.status != "completed" else ""
        return f"{self.title} — {self.status.upper()}{overdue_note}\n📝 {self.description}\n⏰ Tugash muddati: {due}\n"


# === ToDoList sinfi ===
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("❗️ Noto‘g‘ri indeks.")

    def list_tasks(self):
        if not self.tasks:
            print("📭 Hech qanday vazifa mavjud emas.")
            return
        for i, task in enumerate(self.tasks):
            print(f"[{i}] {task}")

    def show_incomplete_tasks(self):
        incomplete_found = False
        for i, task in enumerate(self.tasks):
            if task.status != "completed":
                print(f"[{i}] {task}")
                incomplete_found = True
        if not incomplete_found:
            print("✅ Bajarilmagan vazifalar yo‘q!")


# === Test funksiyasi ===
def test_application():
    print("===== ToDoList Test Dasturi =====")

    # 1. ToDoList obyektini yaratamiz
    todo = ToDoList()


    # 2. Task obyektlari
    task1 = Task(
        title="Python darsini tugatish",
        description="Sinflar va obyektlar bo‘yicha mashqlarni bajarish",
        due_date=datetime.now() + timedelta(days=1)
    )

    task2 = Task(
        title="Uy ishlarini bajarish",
        description="Kir yuvish, xona yig‘ishtirish",
        due_date=datetime.now() + timedelta(hours=5)
    )

    task3 = Task(
        title="Do‘stlar bilan uchrashuv",
        description="Soat 18:00 da kafeda uchrashuv",
        due_date=datetime.now() + timedelta(days=2)
    )

    # 3. Ularni ro‘yxatga qo‘shish
    todo.add_task(task1)
    todo.add_task(task2)
    todo.add_task(task3)

    # 4. Barcha vazifalarni ko‘rish
    print("\n📋 Barcha vazifalar:")
    todo.list_tasks()

    # 5. Faqat bajarilmaganlarni ko‘rish
    print("\n📋 Faqat bajarilmagan vazifalar:")
    todo.show_incomplete_tasks()

    # 6. Ikkinchi vazifani bajarilgan deb belgilash
    print("\n✅ Ikkinchi vazifani bajarilgan deb belgilayapmiz...")
    todo.mark_complete(1)

    # 7. Yangi holat bo‘yicha barcha vazifalar
    print("\n📋 Yangilangan barcha vazifalar:")
    todo.list_tasks()

    # 8. Faqat bajarilmaganlarni qaytadan ko‘rish
    print("\n📋 Qolgan bajarilmagan vazifalar:")
    todo.show_incomplete_tasks()


# === Dastur ishga tushishi ===
if __name__ == "__main__":
    test_application()


from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.views = 0

    def display_summary(self):
        """Post sarlavhasi, muallifi va sanasini ko‘rsatadi."""
        print(f"📝 {self.title}")
        print(f"✍️  Muallif: {self.author}")
        print(f"📅 Sana: {self.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"👁 Ko‘rishlar soni: {self.views}")

    def display_full_post(self):
        """To‘liq postni ko‘rsatadi va ko‘rishlar sonini oshiradi."""
        self.views += 1
        print("\n=== POST BOSHI ===")
        self.display_summary()
        print("\n📄 Matn:\n" + self.content)
        print("=== POST OXIRI ===\n")

    def edit_content(self, new_content):
        """Post matnini yangilaydi."""
        self.content = new_content
        print("✅ Post matni yangilandi.")

        # Post yaratish
post1 = Post(
    title="Yangi Python Darsligi",
    content="Bugun biz Python'dagi sinflarni o‘rganamiz.",
    author="Akmal D."
)

# Xulosa chiqarish
post1.display_summary()

# To‘liq postni ko‘rsatish
post1.display_full_post()

# Matnni tahrirlash
post1.edit_content("Yangi versiyada sinflarga chuqurroq qaraymiz.")
post1.display_full_post()


from datetime import datetime

# === 1. POST SINFI ===
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.views = 0

    def mark_viewed(self):
        self.views += 1

    def display_summary(self):
        print(f"📝 {self.title}")
        print(f"✍️  Muallif: {self.author}")
        print(f"📅 Sana: {self.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"👁 Ko‘rishlar soni: {self.views}")

    def display_full(self):
        self.mark_viewed()
        print("\n=== POST BOSHI ===")
        self.display_summary()
        print("\n📄 Matn:\n" + self.content)
        print("=== POST OXIRI ===\n")

    def __str__(self):
        return f"{self.title} — {self.author} ({self.created_at.strftime('%Y-%m-%d')})"


# === 2. BLOG SINFI ===
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"✅ Post '{post.title}' qo‘shildi.")

    def list_all_posts(self):
        if not self.posts:
            print("📭 Blogda hech qanday post yo‘q.")
            return
        print("📚 Barcha postlar:")
        for i, post in enumerate(self.posts):
            print(f"[{i}] {post}")


    def list_posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author.lower() == author.lower()]
        if not filtered:
            print(f"❌ '{author}' tomonidan hech qanday post topilmadi.")
            return
        print(f"✍️ {author} tomonidan yozilgan postlar:")
        for post in filtered:
            print(f"- {post}")


# === 3. TEST FUNKSIYASI ===
def test_blog():
    print("=== BLOG TIZIMI TESTI ===")

    blog = Blog()

    # Postlar yaratamiz
    post1 = Post("Python Asoslari", "Bugun sinflar haqida o‘rganamiz.", "Akmal")
    post2 = Post("SQL Maslahatlari", "Indekslar va JOIN turlari haqida.", "Abror")
    post3 = Post("OOP Design Patterns", "Strategy va Observer patternlari.", "Akmal")

    # Blogga qo‘shamiz
    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)

    # Barcha postlarni ko‘rsatamiz
    print("\n--- Barcha postlar ---")
    blog.list_all_posts()

    # Akmal tomonidan yozilgan postlar
    print("\n--- Akmal tomonidan yozilgan postlar ---")
    blog.list_posts_by_author("Akmal")

    # Bitta postni to‘liq ko‘rish (ko‘rishlar soni o‘sadi)
    print("\n--- Birinchi postni to‘liq ko‘rsatamiz ---")
    post1.display_full()

    # Yana ko‘rsatamiz, ko‘rishlar soni 2 bo‘ladi
    print("\n--- Qayta to‘liq ko‘rsatamiz ---")
    post1.display_full()

# === 4. ISHGA TUSHIRISH ===
if __name__ == "__main__":
    test_blog()

from datetime import datetime

# === 1. POST SINFI ===
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.views = 0

    def display_summary(self):
        print(f"📝 {self.title}")
        print(f"✍️  Muallif: {self.author}")
        print(f"📅 Sana: {self.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"👁 Ko‘rishlar: {self.views}")

    def display_full(self):
        self.views += 1
        print("\n=== POST BOSHI ===")
        self.display_summary()
        print(f"\n📄 Matn:\n{self.content}")
        print("=== POST OXIRI ===\n")

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content
        print("✏️ Post muvaffaqiyatli tahrirlandi.")

    def __str__(self):
        return f"{self.title} — {self.author} ({self.created_at.strftime('%Y-%m-%d')})"


# === 2. BLOG SINFI ===
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"✅ Post '{post.title}' qo‘shildi.")

    def list_all_posts(self):
        if not self.posts:
            print("📭 Postlar yo‘q.")
            return
        for i, post in enumerate(self.posts):
            print(f"[{i}] {post}")

    def list_posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author.lower() == author.lower()]
        if not filtered:
            print(f"❌ '{author}' tomonidan postlar topilmadi.")
            return
        for post in filtered:
            print(f"- {post}")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"🗑 Post '{removed.title}' o‘chirildi.")
        else:
            print("❗️ Noto‘g‘ri indeks.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
        else:
            print("❗️ Noto‘g‘ri indeks.")

    def show_latest_posts(self, count=3):
        sorted_posts = sorted(self.posts, key=lambda p: p.created_at, reverse=True)
        print(f"🆕 Eng so‘nggi {count} ta post:")
        for post in sorted_posts[:count]:
            print(f"- {post}")


# === 3. CLI INTERFACE ===
def run_blog_cli():
    blog = Blog()


    while True:
        print("\n=== 📚 BLOG MENYU ===")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlar")
        print("4. Postni tahrirlash")
        print("5. Postni o‘chirish")
        print("6. Eng so‘nggi postlar")
        print("7. Dasturdan chiqish")

        tanlov = input("👉 Tanlovni kiriting (1-7): ")

        if tanlov == "1":
            title = input("📝 Sarlavha: ")
            content = input("📄 Matn: ")
            author = input("✍️  Muallif: ")
            blog.add_post(Post(title, content, author))

        elif tanlov == "2":
            print("\n📋 Barcha postlar:")
            blog.list_all_posts()

        elif tanlov == "3":
            author = input("✍️  Muallif ismini kiriting: ")
            blog.list_posts_by_author(author)

        elif tanlov == "4":
            try:
                index = int(input("🔢 Tahrir qilinadigan post raqami: "))
                new_title = input("🆕 Yangi sarlavha: ")
                new_content = input("🆕 Yangi matn: ")
                blog.edit_post(index, new_title, new_content)
            except ValueError:
                print("❗️ Indeks raqam bo‘lishi kerak.")

        elif tanlov == "5":
            try:
                index = int(input("🗑 O‘chiriladigan post raqami: "))
                blog.delete_post(index)
            except ValueError:
                print("❗️ Indeks raqam bo‘lishi kerak.")

        elif tanlov == "6":
            blog.show_latest_posts()

        elif tanlov == "7":
            print("👋 Dasturdan chiqilmoqda. Xayr!")
            break

        else:
            print("❗️ Noto‘g‘ri tanlov.")

# === 4. TEST DASTUR ISHGA TUSHIRILADI ===
if __name__ == "__main__":
    run_blog_cli()


## Project name: Banking Project
## Project topic: python class, OOP
## Project goal, create a program to communicate with user and give a chance to add account and deposit, withdraw, check balance operations.
## classes -- Account, Bank

import datetime


class Account:
    def __init__(self,id,holder_name):
        opened_date = datetime.datetime.today()
        self.id = id
        self.holder_name = holder_name
        self.opened_date = opened_date
        self.closed_date = None
        self.balance = 0
    def deposit_money(self,deposit):
        self.balance += deposit
        return self.balance
    def withdraw_money(self,withdraw):
        if self.balance >withdraw:
            self.balance -= withdraw
            return True
        return False
    def close_account(self):
        self.closed_date = datetime.datetime.today()
    def __str__(self):
        return f"Account Number: {self.id} | Holder name: {self.holder_name} | Balance: {self.balance}"


class Bank:
    account_list = []
    last_id = 0
    def __init__(self,name):
        self.name = name
    def add_account(self):
        self.last_id += 1
        holder_name = input('Enter Your Name ')
        account_obj = Account(self.last_id,holder_name)
        self.account_list.append(account_obj)
        print(f'Account Number {self.last_id} was added successfully!')
    def search(self,id):
        for i in self.account_list:
            if i.id == id:
                return i
        return False
    def deposit_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            deposit_amount = int(input('Enter your money! ex: 1000$ '))
            balance = a.deposit_money(deposit_amount)
            print(f'depositing process is completed successfully | Current Balance: {balance}')
        else:
            print(f'Account number {id} is not found')
    def withdraw_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            withdraw_amount = int(input('Enter withdraw amount '))
            result = a.withdraw_money(withdraw_amount)
            if result:
                print(f'The withdraw process completed sucessfully! withdraw Amount: {withdraw_amount} | Current Balance: {a.balance}')
            else:
                print(f'Your account has not available amount!  Amount: {withdraw_amount} | Current Balance: {a.balance}')
    def show_accounts_details(self):
        for i in self.account_list:
            print(i)
    def show_account_detail(self,id):
        a = self.search(id)
        print(a)
    def close_account(self,id):
        a = self.search(id)
        a.close_account()
        print(f'Account Number: {a.id} is closed')

milly_bank = Bank('milliy bank')
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")

while True:
    a = print_menu()
    command = input('Enter a number ')
    if command == '1':
        milly_bank.add_account()
    elif command == '2':
        milly_bank.show_accounts_details()
    elif command == '3':
        account_number = int(input('Enter your account '))
        milly_bank.deposit_account(account_number)
    elif command == '4':
        account_number = int(input('Enter your account '))
        milly_bank.withdraw_account(account_number)
    elif command == '5':
        account_number = int(input('Enter your account '))
        milly_bank.show_account_detail(account_number)
    else:
        exit()


class Bank:
    account_list = []
    last_id = 0
    def __init__(self,name):
        self.name = name
    def add_account(self):
        self.last_id += 1
        holder_name = input('Enter Your Name ')
        account_obj = Account(self.last_id,holder_name)
        self.account_list.append(account_obj)
        print(f'Account Number {self.last_id} was added successfully!')
    def search(self,id):
        for i in self.account_list:
            if i.id == id:
                return i
        return False
    def deposit_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            deposit_amount = int(input('Enter your money! ex: 1000$ '))
            balance = a.deposit_money(deposit_amount)
            print(f'depositing process is completed successfully | Current Balance: {balance}')
        else:
            print(f'Account number {id} is not found')
    def withdraw_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            withdraw_amount = int(input('Enter withdraw amount '))
            result = a.withdraw_money(withdraw_amount)
            if result:
                print(f'The withdraw process completed sucessfully! withdraw Amount: {withdraw_amount} | Current Balance: {a.balance}')
            else:
                print(f'Your account has not available amount!  Amount: {withdraw_amount} | Current Balance: {a.balance}')
    def show_accounts_details(self):
        for i in self.account_list:
            print(i)
    def show_account_detail(self,id):
        a = self.search(id)
        print(a)
    def close_account(self,id):
        a = self.search(id)
        a.close_account()
        print(f'Account Number: {a.id} is closed')

milly_bank = Bank('milliy bank')
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")

while True:
    a = print_menu()
    command = input('Enter a number ')
    if command == '1':
        milly_bank.add_account()
    elif command == '2':
        milly_bank.show_accounts_details()
    elif command == '3':
        account_number = int(input('Enter your account '))
        milly_bank.deposit_account(account_number)
    elif command == '4':
        account_number = int(input('Enter your account '))
        milly_bank.withdraw_account(account_number)
    elif command == '5':
        account_number = int(input('Enter your account '))
        milly_bank.show_account_detail(account_number)
    else:
        exit()


