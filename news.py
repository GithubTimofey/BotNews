import requests
from bs4 import BeautifulSoup
import datetime
from aiogram import types, executor, Dispatcher, Bot
TOKEN = '5784940404:AAE2FU1EOBHRAAMXV8f5K5mRfJxy_HXKElo'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    arkupreply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("IT новости 💵")
    btn2 = types.KeyboardButton("World новости 🌍")
    btn3 = types.KeyboardButton("Crypto новости 🪙")
    markupreply = types.InlineKeyboardMarkup(row_width=4)
    rus = types.InlineKeyboardButton(text="Начать", callback_data="1")
    markupreply.add(rus)   
    arkupreply.add(btn1, btn2,btn3)
    await bot.send_message(message.chat.id,'''*Добрый день {0.first_name}*! *Меня зовут Джек 🤖.
"Что я могу сделать ?" - Может быть, вы спросите меня.
Собираю информацию из разных источников и передаю вам
Три главные новости сразу из трех областей*'''.format(message.from_user),parse_mode='Markdown',reply_markup=markupreply)
    await bot.send_message(message.chat.id,'*Вы можете также выбрать один из вариантов (Новости IT, Новости Мир, Новости Крипта)*',reply_markup=arkupreply,parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == '1')
async def query_handler(call: types.CallbackQuery):
    now = datetime.datetime.now()
    url_eur = 'https://ria.ru/world/'
    response_eur = requests.get(url_eur)
    soup_eur = BeautifulSoup(response_eur.text,'lxml')
    quete_eur = soup_eur.find_all('div',class_='list list-tags')
    for i in quete_eur:
        News1 = i.find_all('a',class_='list-item__title color-font-hover-only')[0].text
        href = i.find_all('a',class_='list-item__title color-font-hover-only')[0].get('href')

    url_hadr = 'https://habr.com/ru/news/'
    response_hadr = requests.get(url_hadr)
    soup_hadr = BeautifulSoup(response_hadr.text,'lxml')
    quete_hadr = soup_hadr.find_all('div',class_='tm-articles-list')
    for i in quete_hadr:
        IT = i.find_all('article')[0]

    url_crypto = 'https://cryptonews.net/ru/'
    response_crypto = requests.get(url_crypto)
    soup_crypto = BeautifulSoup(response_crypto.text,'lxml')
    quete_crypto = soup_crypto.find_all('section',class_='col-xs-12 col-sm')
    for i in quete_crypto:
        Crypto = i.find_all('div',class_='row news-item start-xs')[0]
    # bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id = call.message.id, text='''
*Дата: {0}*

*Мир:*
[{1}]({2})

*IT:*
[{3}]({4})

*Криптовалюта:*
[{5}]({6})

'''.format(now.strftime('%d-%m-%Y'),News1,href,str(IT).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0],str(Crypto).partition('data-title="')[2].partition('"')[0],str(Crypto).partition('data-link="')[2].partition('"')[0]),parse_mode="Markdown")


@dp.message_handler(content_types=['text'])
async def more(message: types.Message):
    if (message.text == 'IT новости 💵'):
        url_hadr = 'https://habr.com/ru/news/'
        response_hadr = requests.get(url_hadr)
        soup_hadr = BeautifulSoup(response_hadr.text,'lxml')
        quete_hadr = soup_hadr.find_all('div',class_='tm-articles-list')
        for i in quete_hadr:
            IT = i.find_all('article')[0]
            IT1 = i.find_all('article')[1]
            IT2 = i.find_all('article')[2]
            IT3 = i.find_all('article')[3]
            IT4 = i.find_all('article')[4]
        await bot.send_message(message.chat.id,'''
*1 Новость*
[{0}]({1})

*2 Новость*
[{2}]({3})

*3 Новость*
[{4}]({5})

*4 Новость*
[{6}]({7})

*5 Новость*
[{8}]({9})'''.format(str(IT).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0],str(IT1).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT1).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0],str(IT2).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT2).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0],str(IT3).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT3).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0],str(IT4).partition('<span>')[2].partition('</span>')[0],'https://habr.com'+str(IT4).partition('data-test-id="article-snippet-title-link" href="')[2].partition('"')[0]),parse_mode='Markdown')
    elif message.text == 'World новости 🌍':
        url_eur = 'https://ria.ru/world/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='list list-tags')
        for i in quete_eur:
            News1 = i.find_all('a',class_='list-item__title color-font-hover-only')[0].text
            href = i.find_all('a',class_='list-item__title color-font-hover-only')[0].get('href')
            News2 = i.find_all('a',class_='list-item__title color-font-hover-only')[1].text
            href2 = i.find_all('a',class_='list-item__title color-font-hover-only')[1].get('href')
            News3 = i.find_all('a',class_='list-item__title color-font-hover-only')[2].text
            href3 = i.find_all('a',class_='list-item__title color-font-hover-only')[2].get('href')
            News4 = i.find_all('a',class_='list-item__title color-font-hover-only')[3].text
            href4 = i.find_all('a',class_='list-item__title color-font-hover-only')[3].get('href')
            News5 = i.find_all('a',class_='list-item__title color-font-hover-only')[4].text
            href5 = i.find_all('a',class_='list-item__title color-font-hover-only')[4].get('href')
        await bot.send_message(message.chat.id,'''
*1 Новость*
[{0}]({1})

*2 Новость*
[{2}]({3})

*3 Новость*
[{4}]({5})

*4 Новость*
[{6}]({7})

*5 Новость*
[{8}]({9})
'''.format(News1,href,News2,href2,News3,href3,News4,href4,News5,href5),parse_mode='Markdown')
    elif message.text == 'Crypto новости 🪙':
        markupreply = types.InlineKeyboardMarkup(row_width=4)
        rus = types.InlineKeyboardButton(text="Перейти",url='https://t.me/tracepython_bot')
        markupreply.add(rus) 

        url_crypto = 'https://cryptonews.net/ru/'
        response_crypto = requests.get(url_crypto)
        soup_crypto = BeautifulSoup(response_crypto.text,'lxml')
        quete_crypto = soup_crypto.find_all('section',class_='col-xs-12 col-sm')
        for i in quete_crypto:
            Crypto = i.find_all('div',class_='row news-item start-xs')[0]
            Crypto1 = i.find_all('div',class_='row news-item start-xs')[1]
            Crypto2 = i.find_all('div',class_='row news-item start-xs')[2]
            Crypto3 = i.find_all('div',class_='row news-item start-xs')[3]
            Crypto4 = i.find_all('div',class_='row news-item start-xs')[4]

        await bot.send_message(message.chat.id,'''
*1 Новость*
[{0}]({1})

*2 Новость*
[{2}]({3})

*3 Новость*
[{4}]({5})

*4 Новость*
[{6}]({7})

*5 Новость*
[{8}]({9})
'''.format(str(Crypto).partition('data-title="')[2].partition('"')[0],str(Crypto).partition('data-link="')[2].partition('"')[0],str(Crypto1).partition('data-title="')[2].partition('"')[0],str(Crypto1).partition('data-link="')[2].partition('"')[0],str(Crypto2).partition('data-title="')[2].partition('"')[0],str(Crypto2).partition('data-link="')[2].partition('"')[0],str(Crypto3).partition('data-title="')[2].partition('"')[0],str(Crypto3).partition('data-link="')[2].partition('"')[0],str(Crypto4).partition('data-title="')[2].partition('"')[0],str(Crypto4).partition('data-link="')[2].partition('"')[0]),parse_mode='Markdown')
        await bot.send_message(message.chat.id,'*Если хотите посмотреть подробные курсы криптовальт можете нажать на кнопку*',reply_markup=markupreply,parse_mode='Markdown')
def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()

