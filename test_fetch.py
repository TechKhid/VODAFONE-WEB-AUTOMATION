import pandas as pd

df = pd.read_excel (r'C:\Users\Samuel Mensah\OneDrive\Desktop\IS_Database\learners_database.xlsx')
names = []
phones = []
for stud_ in range(len(df)):
    name = df["Full name"][stud_]
    phone = df["Phone number "][stud_]
    print(name, phone)
    names.append(name)
    phones.append(phone)
# print (df["Full name"])


