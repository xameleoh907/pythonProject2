# Рассылка писем
def check_mail (mail): # функция проверки корректности фдреса
# функция фозвращает True если найдены несоответсвия адреса и False если несоответствий не найдено
    check_list = ['.com', '.ru', '.net']
    for i in check_list:
        if i in mail and '@' in mail: # проверка одновременного наличия @ и домена почны
            return False
    else:
        return True

def send_email (message, recipient, *,sender = "university.help@gmail.com"):
    if check_mail(recipient) or check_mail(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient in sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender in 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
       print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mailru', sender='university.help@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')