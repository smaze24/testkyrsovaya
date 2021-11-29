import random
import sqlite3
import time
import datetime
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

def gen_clients():
    while True:
        pass_id = random.randint(1000000000,9999999999)
        c.execute("SELECT pass_id FROM clients WHERE pass_id = ?", (pass_id,))
        result = c.fetchall()
        if result == []:
            break



    tmp = random.randint(0, 1)

    mass_familia_men = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Федоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров', 'Павлов', 'Козлов', 'Степанов', 'Николаев']
    mass_familia_women = ['Иванова','Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Петрова', 'Сколова', 'Михайлова', 'Новикова', 'Федорова', 'Морозова', 'Волкова', 'Алексеева', 'Лебедева', 'Семенова', 'Егорова', 'Павлова', 'Козлова', 'Степанова', 'Николаева']

    if tmp == 0:
        familia = random.randint(0, len(mass_familia_men)-1)
        familia = mass_familia_men[familia]
    else:
        familia = random.randint(0, len(mass_familia_women)-1)
        familia = mass_familia_women[familia]

    mass_name_men = ['Александр', 'Сергей', 'Владимир', 'Андрей', 'Алексей', 'Николай', 'Иван', 'Дмитрий', 'Михаил', 'Евгений', 'Виктор', 'Василий', 'Игорь', 'Анатолий', 'Олег', 'Павел', 'Максим', 'Виталий', 'Роман', 'Денис']
    mass_name_women = ['Елена', 'Татьяна', 'Ольга', 'Наталья', 'Анна', 'Ирина', 'Мария', 'Светлана', 'Екатерина', 'Анастасия', 'Юлия', 'Валентина', 'Галина', 'Людмила', 'Надежда', 'Марина', 'Александра', 'Нина', 'Виктория', 'Любовь']

    if tmp == 0:
        name = random.randint(0, len(mass_name_men)-1)
        name = mass_name_men[name]
    else:
        name = random.randint(0, len(mass_name_women)-1)
        name = mass_name_women[name]

    mass_otchestvo_men = ['Александрович', 'Сергеевич', 'Владимирович', 'Андреевич', 'Алексеевич', 'Николаевич', 'Иванович', 'Дмитриевич', 'Михайлович', 'Евгеньевич', 'Викторович', 'Васильевич','Игоревич', 'Анатольевич', 'Олегович', 'Павлович', 'Максимович', 'Витальевич', 'Романович', 'Денисович']
    mass_otchestvo_women = ['Александровна', 'Сергеевна', 'Владимировна', 'Андреевна', 'Алексеевна', 'Николаевна', 'Ивановна', 'Дмитриевна', 'Михайловна', 'Евгеньевна', 'Викторовна', 'Васильевна', 'Игоревна', 'Анатольевна', 'Олеговна', 'Павловна', 'Максимовна', 'Витальевна', 'Романовна', 'Денисовна']

    if tmp == 0:
        otchestvo = random.randint(0, len(mass_otchestvo_men)-1)
        otchestvo = mass_otchestvo_men[otchestvo]
    else:
        otchestvo = random.randint(0, len(mass_otchestvo_women)-1)
        otchestvo = mass_otchestvo_women[otchestvo]

    year = random.randint(1940, 2003)
    mouth = random.randint(1, 12)
    if mouth == 1 or mouth == 3 or mouth == 5 or mouth == 7 or mouth == 8 or mouth == 10 or mouth == 12:
        day = random.randint(1, 31)
    elif mouth == 4 or mouth == 6 or mouth == 9 or mouth == 11:
        day = random.randint(1, 30)
    else:
        if year % 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    purch = [(None, pass_id, f'{familia} {name} {otchestvo}', f'{day}.{mouth}.{year}', datetime.datetime.now())]
    c.executemany('INSERT INTO clients VALUES(?,?,?,?,?)', purch)
    conn.commit()

def gen_devices():
    c.execute("SELECT idenf FROM clients")
    result = c.fetchall()
    tmp = random.randint(0, len(result)-1)
    idenf = result[tmp][0]


    while True:
        number = random.randint(10000000000, 99999999999)
        c.execute("SELECT number FROM devices WHERE number = ?", (number,))
        result = c.fetchall()
        if result == []:
            break

    tmp = random.randint(0, 1)
    if tmp == 0:
        type_device = 'мобильный'
    else:
        type_device = 'стационарный'

    balance = random.randint(100, 5000)

    c.execute("SELECT id_plan FROM subscription")
    result = c.fetchall()

    tmp = random.randint(0, len(result)-1)

    subscription = result[tmp][0]

    purch = [(idenf, number, type_device, balance, subscription, datetime.datetime.now())]
    c.executemany('INSERT INTO devices VALUES(?,?,?,?,?,?)', purch)
    conn.commit()

def gen_calls():
    c.execute("SELECT number FROM devices")
    result = c.fetchall()

    tmp = random.randint(0, len(result)-1)
    number1 = result[tmp][0]

    c.execute("SELECT number FROM devices WHERE number != ?", (number1,))
    result = c.fetchall()

    tmp = random.randint(0, len(result)-1)
    number2 = result[tmp][0]

    time = random.randint(0, 120)

    c.execute("SELECT devices.number, devices.balance, subscription.cost FROM devices, subscription WHERE devices.number = ? and devices.id_plan = subscription.id_plan", (number1,))
    result = c.fetchall()



    balance = result[0][1]


    t = [(balance-(time*result[0][2]), number1)]
    c.executemany("UPDATE devices SET balance=? WHERE number=?", t)
    conn.commit()

    purch = [(number1, number2, time, datetime.datetime.now())]
    c.executemany('INSERT INTO calls VALUES(?,?,?,?)', purch)
    conn.commit()

def gen_balance():
    c.execute("SELECT number, balance FROM devices")
    result = c.fetchall()


    tmp = random.randint(0, len(result)-1)
    number = result[tmp][0]
    balance = result[tmp][1]

    summ = random.randint(100, 5000)
    t = [(balance+summ, number)]
    c.executemany("UPDATE devices SET balance=? WHERE number=?", t)
    conn.commit()
