# <img  alt="SalonKrasBot" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/Телеграм%20-бот%20Салона%20красоты.png" width="1100px"/>

<h1 align="center">"Помощник администратора салона красоты"</h1>


<h3 align="center">
<p>Данное руководство написано с целью демонастрации функционала телеграмм-бота, и кратким описанием основных особенностей проекта.</p>
<p>Саму реализацию данного проекта можно найти в телеграмме по ссылке @salon_krasoti_bot. 
Бот будет полезен как салонам красоты, так и самозанятым мастерам маникюра, педикюра и другим и станет дополнительным каналом продаж данных услуг.</p>
</h3>

<h2>Особенности проекта</h2>

* Сделан модуль для фильтрации и удаления нецензурных сообщений, с возможностью обновления списка слов по инструкции прилагаемой к модулю

* Возможность добавления/удаления процедур с полным описанием в базу данных администратором через телеграмм

* Работа админской части в боте написана с ипользование конечных автоматов (finite-state machine-далее FMS). FMS -  упрощенная модель компьютера имеющая конечное число состояний, которая жертвует всеми особенностями компьютеров такие как ОЗУ, постоянная память, устройства ввода-вывода и процессорными ядрами в обмен на простоту понимания, удобство рассуждения и легкость программной или аппаратной реализации.

<h2>Используемые библиотеки в проекте</h2>

- aiogram - это простой и полностью асинхронный фреймворк для Telegram Bot API, написанный на Python 3.7 с asyncio и aiohttp, помогает сделать ботов быстрее и проще
- os - для возможности чтения токена из batch-файла
- emoji - библиотека для использования эмодзи в кнопка для клиентов, с целью улучшения визуализации
- sqlite3 - обладает практически всеми возможностями, которых можно ожидать от реляционной СУБД, но при этом всё хранится в единственном файле
- json - используется в данном проекте для конвертирования списка нецензурных слов из формата .txt в .json
- string - для приведения нецензурных слов из сообщений к одному типу, с целью прохождения в дальнейшем сравнительной фильтрации

<h2>Модули</h2>

- BotTelegpy.py - основной файл, являющийся точкой входа бота и запуска функций для работы с Handlers
- CreateBot.py - в нем создается сам экземпляр бота
- Cenzura.json - готовый файл с нецензурными словами для фильтра сообщений
- requirements.txt - зависимости, при клонировании репозитория на другой компьютер или сервер выполните (предварительно создав и активировав нужное виртуальное окружение): 
```
$ pip install -r requirements.txt
```

<h3>Директории</h3>
*в каждой директории есть файл __init__.py - для организации пакета и удобства импортов из директории в которой находимся (Handlers, Keyboards и др.)

<h4>Handlers</h4>

- Admin.py - работа админской части в боте написана с ипользование FMS (описание подробнее выше в разделе особенности проекта). 
При работе с загрузкой данных в БД вопросы выстроены в определнном порядке и на любом этапе можно отменить вносимые данные
- Client.py - записаны функции для всех кнопок используемых в работе с клиентом
- Other.py - написан код для сравнения текста сообщения с запрещенных словами, и в случае иимеющихся таких, удаления данного сообщения

<h4>Keyboards(используются кнопки 2-х видов: ReplyKeyboardMarkup (клавиатура показывается вместо основной и не привязана ни к какому сообщению) и InlineKeyboardMarkup (привязывается к сообщению, с которым была отправлена)</h4>

- AdminKb.py и ClientKb.py - создание самих кнопок и их расположение при использовании в телеграмме

<h4>DB</h4>

- SqliteDb.py - прописана вся логика создания БД и формат внесения в нее данных

<h2>Использование</h2>

<font size="3">

  1. Запуск файла bot_run.bat

<img src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/1a.png"> 
  
<p>Для безопасного хранения TOKENа используется batch-файл в котором прописаны команды для запуска приложения. Номер токена в файле bot_run.bat не выложен на github.com из соображений безопасности</p>
  
```
 @echo off
 call %~dp0salon_bot\venv\Scripts\activate
 cd %~dp0salon_bot
 set TOKEN= введение № без кавычек
 python BotTelegpy.py
 pause

```

  2. Если запуск пройден успешно, в окно будут выведенны данные фразы

<img src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/2.png"> 
  
  3. Для живого общения между администраторами и клиентами создана группа по ссылке https://t.me/+ryDy7lLxtQU3Y2My, чтобы перейти к телеграмм боту внизу справа необходмо нажать на клавишу "/"
  и выбрать /start(либо в ручную ввести в диалоговом окне <strong>/start</strong>)

<img src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/3.png"> 
  
  4. В случае использования участниками общения нецензурной лексики данные сообщения удаляются с оповещение о том что "Материться запрещено"
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/14a.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/14b.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>

  5. После автоматического ответа от телеграмм бота выбирите одну из предложенных кнопок для получения быстрого ответа (расположения, контакты, список всех процедур, прайс и т.д.)
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/4.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/5.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/6.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/7.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>

  
  6. В случае если нужная информация не найдена, есть возможность либо обратиться в группе к администратору либо отправить свой номер для обратного звонка (данный функцинал в процессе разработки)
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/8a.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/8b.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>
  
  7. Для перехода администратора к своей части в боте, необходимо в группе написать запрос в диалоговм окне <strong>/moderator</strong>, после чего бот предоставит скрытую панель кнопок для дальнейшей работы, а запрос в группе будет удален (во избежания доступа клиентов к админской части в приложении прописана проверка на права администратора, которые настраиваются в управлении группой)
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/9.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/10.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/15.png" alt=""width="500" height="450"/></a> </td>
</tr>
</table>
  
  8. Чтобы загрузить описание новой процедуры в БД, нажимается кнопка <strong>/Загрузить</strong>, после чего запускается сценарий последовательных вопросов (Загрузка фото->Название процедуры->Описание->Цена). После введения цены, сценарий будет остановлен без оповещения администратора
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/11a.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/11b.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>

  
  9. В случае, если при введении данных замечена ошибка и графа <strong> Цена </strong> еще не пройдена, в диалоговом окне необходимо написать <strong>/отмена</strong>, при успешном выполнении будет сообщение об остановке введения данных
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/12a.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/12b.png" alt=""width="500" height="450"/></a></td>
</tr>
</table>  
  
  10. Если ошибка обнаружена после заполнени всех данных, с помощью кнопки <strong>/удалить</strong> выгружается вся БД с инлайн кнопками для удаления полностью данных одной процедуры
<table>
<tr>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/13a.png" alt=""width="500" height="450"/></a> </td>
<td><img title="Описание" src="https://github.com/PakKseniya/salon_krasoti_TelegramBot/blob/master/Screenshots/13b.png" alt=""width="500" height="450"/></a></td>
</tr>
</table> 

</font>
  



