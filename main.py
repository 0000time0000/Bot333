import discord
import random
import asyncio
import time
import json
import os
from discord.ext import commands
from discord import app_commands
import re
# Ваш токен бота
TOKEN = 'MTEzNjM4NDM4MzIyNjQ4MjY4OA.GUzU2I._RIWaRAx8cuAlaCqh9AjVuxKMOsoGlq83Hz9nk'
client = discord.Client(intents=discord.Intents.all())

# Список возможных ответов для команды !шар
magic_8_ball_responses = [
    "https://cdn.discordapp.com/attachments/1018623841586659330/1141135653124460604/ask.png",
    "https://media.discordapp.net/attachments/1018623841586659330/1141135767029162115/idk.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141135857294790666/maybe.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141135911631982633/no.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141135959820357751/nono.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141136015269044384/prob.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141136075553787984/yes.png?width=682&height=682",
    "https://media.discordapp.net/attachments/1018623841586659330/1141136116175605952/yesyes.png?width=682&height=682",
]

# Создание объекта intents и указание нужных нам интентов
intents = discord.Intents.all()
intents.voice_states = True
intents.message_content = True
intents.presences = True
intents.reactions = True

# Создание клиента Discord с указанием intents

initial_extensions = [
    'keys',  # Замените на имя вашего файла cog (без расширения .py)
]




bot = commands.Bot(command_prefix='!', intents=intents)

if os.path.exists('balances.json'):
    with open('balances.json', 'r') as f:
        balances = json.load(f)
else:
    balances = {}

def save_balances():
    with open('balances.json', 'w') as f:
        json.dump(balances, f)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

async def kick_user(user, reason):
    await user.kick(reason=reason)

# Функция для бана пользователя
async def ban_user(user, reason):
    await user.ban(reason=reason)

# Функция для мута пользователя
async def mute_user(user, time, reason):
    muted_role = discord.utils.get(user.guild.roles, name="Muted")

    if not muted_role:
        # Создаем роль "Muted", если она не существует
        muted_role = await user.guild.create_role(name="Muted")

        # Отключаем возможность отправки сообщений для роли "Muted"
        for channel in user.guild.text_channels:
            await channel.set_permissions(muted_role, send_messages=False)

    # Выдаем роль "Muted" пользователю
    await user.add_roles(muted_role, reason=reason)

    if time == 0:
        # Если время равно 0, мут навсегда
        return

    # Ждем указанное время и затем снимаем мут
    await asyncio.sleep(time)
    await user.remove_roles(muted_role, reason="Истекло время мута")
# Событие запуска бота

last_opened_time = {}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='!команды | 🏮'))
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(f"Bot is on {len(client.guilds)} servers")
    print("NamelessBot is ready :)")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("")



# Событие при получении сообщения
@client.event
async def on_message(message):
    # Игнорировать сообщения от самого бота, чтобы избежать зацикливания
    if message.author == client.user:
        return

    # Проверка наличия команды "!монетка"
    if "!монетка" in message.content:
        # Выбираем случайную картинку из списка для монетки
        random_image = random.choice(['https://media.discordapp.net/attachments/1018623841586659330/1141136320136237076/mno.png?width=682&height=682', 'https://media.discordapp.net/attachments/1018623841586659330/1141136329883783348/myes.png?width=682&height=682'])

        # Создаем эмбед
        embed = discord.Embed(title="Вы подбросили монетку, вам выпало:", color=discord.Color.gold())
        embed.set_image( url=f'{random_image}')
        # Отправляем эмбед без вложения
        message = await message.channel.send(embed=embed)
        

    # Проверка наличия команды "!шар"
    if "!шар" in message.content:
        # Выбираем случайную картинку из списка для шара
        random_response = random.choice(magic_8_ball_responses)

        # Создаем эмбед
        embed = discord.Embed(title="Ответ шара:", color=discord.Color.dark_grey())
        embed.set_footer(text="Вам понравился ответ шара?")
        embed.set_image( url=f'{random_response}')
        # Отправляем эмбед без вложения
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        # Открываем файл и отправляем вложение с картинкой шара
        
            

    if "!заказ" in message.content:
        # Проверяем, является ли автор сообщения администратором
        if message.author.guild_permissions.administrator:
            # Отправляем запрос на ввод информации о заказе
            await message.channel.send("✔ **Укажите на что будет заказ**")

            # Ожидаем ответа от автора сообщения
            def check(m):
                return m.author == message.author and m.channel == message.channel

            try:
                order_name = await client.wait_for('message', check=check, timeout=60)  # Ожидаем 60 секунд

                await message.channel.send("✔ **Укажите цену на которую будет заказ**")

                price = await client.wait_for('message', check=check, timeout=60)  # Ожидаем 60 секунд

                # Формируем текст с информацией о заказе
                await message.channel.purge(limit=6)
                order_message = f"@everyone **Новый заказ!**\n{order_name.content}, {price.content}\nНажмите на эмодзи 🍁 **если хотите взяться за заказ.**"

                # Отправляем сообщение с информацией о заказе и запоминаем его ID
                order_info_msg = await message.channel.send(order_message)
                
                # Ставим эмодзи на сообщение
                await order_info_msg.add_reaction("🍁")

                # Ожидаем реакции от пользователей
                def reaction_check(reaction, user):
                    return user != client.user and str(reaction.emoji) == "🍁" and reaction.message.id == order_info_msg.id

                reaction, user = await client.wait_for('reaction_add', check=reaction_check, timeout=3600)  # Ожидаем 1 час (3600 секунд)

                # Обновляем сообщение, чтобы отобразить, кто взялся за заказ и время закрытия
                order_message += f"\n\n❌ Заказ закрыт, взялся : {user.mention}"
                await order_info_msg.edit(content=order_message)

                # Удаляем предыдущие сообщения пользователя
                await message.channel.purge(limit=2, check=lambda m: m.author == message.author)

                # Удаляем предыдущие сообщения бота (кроме сообщения о заказе)
                await message.channel.purge(limit=2, check=lambda m: m.author == client.user and m.id != order_info_msg.id)

            except asyncio.TimeoutError:
                # В случае превышения времени ожидания
                await message.channel.send("Превышено время ожидания, заказ отменен.")
        else:
            # Если у пользователя нет нужных прав, отправляем сообщение об ошибке
            await message.channel.send("Недостаточно прав для использования этой команды!")


    embed = discord.Embed(title="", color=0xD4263D)

    if "!сервер" in message.content:
    # Получаем информацию о сервере из объекта message.guild
        server = message.guild
        name = server.name
        member_count = server.member_count
        owner = None
        try:
            owner = server.owner  # Получаем информацию о владельце сервера, если есть права
        except AttributeError:
            pass

        icon_url = server.icon.url if server.icon else None  # Получаем URL аватарки сервера
        banner_url = server.banner.url if server.banner else None  # Получаем URL баннера сервера

    # Создаем эмбед с информацией о сервере
        embed = discord.Embed(title=f"Информация о сервере {name}", color=0xD4263D)
        embed.add_field(name="Количество участников:", value=member_count, inline=True)

    # Добавляем информацию о владельце сервера в эмбед
        if owner:
            guild = client.get_guild(server.id)
            owner_mention = guild.get_member(owner.id).mention if guild.get_member(owner.id) else "Не найден"
            embed.add_field(name="Владелец сервера:", value=owner_mention, inline=False)
        else:
            embed.add_field(name="Владелец сервера:", value="Не найден", inline=False)

    # Получаем подвиды участников на сервере
        online_members = sum(member.status == discord.Status.online for member in server.members)
        idle_members = sum(member.status == discord.Status.idle for member in server.members)
        dnd_members = sum(member.status == discord.Status.dnd for member in server.members)
        offline_members = sum(member.status == discord.Status.offline for member in server.members)
        bots_count = sum(member.bot for member in server.members)

    # Добавляем информацию о подвидах участников в эмбед
        embed.add_field(name="🟢 В сети:", value=online_members, inline=True)
        embed.add_field(name="🟡 Не активен:", value=idle_members, inline=True)
        embed.add_field(name="🔴 Не беспокоить:", value=dnd_members, inline=True)
        embed.add_field(name="⚫ Оффлайн:", value=offline_members, inline=True)
        embed.add_field(name="🤖 Боты:", value=bots_count, inline=True)

    # Добавляем аватарку и баннер сервера к эмбеду
        if icon_url:
            embed.set_thumbnail(url=icon_url)
        if banner_url:
            embed.set_image(url=banner_url)

    # Отправляем эмбед с информацией о сервере
        await message.channel.send(embed=embed)


    if "!очистить" in message.content:
        # Проверяем, есть ли у пользователя права администратора или управления сообщениями на этом канале
        if message.author.guild_permissions.administrator or message.author.guild_permissions.manage_messages:
            # Получаем количество сообщений для удаления (по умолчанию 5, если количество не указано)
            args = message.content.split()
            num_messages = 5  # По умолчанию удаляем 5 сообщений
            if len(args) > 1:
                try:
                    num_messages = int(args[1]) + 1  # +1 для удаления исходной команды
                except ValueError:
                    pass

            # Удаляем сообщения
            deleted = await message.channel.purge(limit=num_messages)
            response = f'🗑 Удалено {len(deleted)} сообщений!'
            await message.channel.send(response, delete_after=5)  # Удалить сообщение с ответом через 5 секунд
        else:
            # Если у пользователя нет нужных прав, отправляем сообщение об ошибке
            await message.channel.send("❌ У вас недостаточно прав для выполнения этой команды!")



        # Отправляем эмбед с информацией о сервере
        await message.channel.send(embed=embed)




    if "!слоты" in message.content:
        emojis = ["🍒", "🍊", "🍋", "🍇", "🍉"]
        weights = [30, 30, 15, 15, 10]
        
        user_id = str(message.author.id)
        
        if user_id in balances and balances[user_id] >= 10:
            balances[user_id] -= 10
            save_balances()
            
            slots = random.choices(emojis, weights=weights, k=3)
            result = ' '.join(slots)
            
            await message.channel.send(result)
            
            if slots[0] == slots[1] or slots[1] == slots[2]:
                if slots[0] == "🍇" or slots[1] == "🍋":
                    balances[user_id] += 25
                else:
                    balances[user_id] += 10
                save_balances()
                await message.channel.send(f"🎉 Поздравляем! Вы выиграли {'25' if '🍉' in slots else '10'} рублей!")
            elif slots[0] == slots[1] == slots[2]:
                if slots[0] == "🍉":
                    balances[user_id] += 50
                else:
                    balances[user_id] += 25
                save_balances()
                await message.channel.send(f"🎉 Поздравляем! Вы выиграли {'50' if slots[0] == '🍉' else '25'} рублей!")
        else:
            await message.channel.send("❌ У вас недостаточно монет для ставки.")




    if message.content.startswith("!<@") and message.content.endswith(">"):
        # Получаем упоминание пользователя
        user_mention = message.content[2:-1]
        
        # Проверяем, является ли автор сообщения администратором
        if message.author.guild_permissions.administrator:
            # Отправляем меню действий для данного пользователя
            menu_message = await message.channel.send(f"**Что вы хотите сделать с <{user_mention}>?\n1️⃣. Кикнуть\n2️⃣. Забанить\n3️⃣. Замутить\n🖼. Аватар**")

            # Добавляем реакции на сообщение с меню
            reactions = ['🏮', '1️⃣', '2️⃣', '3️⃣', '🖼', '⛩']
            for reaction in reactions:
                await menu_message.add_reaction(reaction)

            # Ожидаем реакции от пользователей
            def reaction_check(reaction, user):
                return user == message.author and str(reaction.emoji) in reactions and reaction.message.id == menu_message.id

            try:
                reaction, _ = await client.wait_for('reaction_add', check=reaction_check, timeout=60)  # Ожидаем 60 секунд

                # Обрабатываем выбранную реакцию
                if str(reaction.emoji) == '1️⃣':
                    await message.channel.purge(limit=1)
                    
                    await message.channel.send(f"Вы выбрали **кик**, пока-пока <{user_mention}>")
                    user = message.mentions[0]
                    
                    await kick_user(user, "Администратор кикнул человека, не указав причину.")
                    
                elif str(reaction.emoji) == '2️⃣':
                    await message.channel.purge(limit=1)
                    await message.channel.send(f"Вы выбрали **бан**, пока-пока навсегда <{user_mention}>")
                    user = message.mentions[0]
                    
                    await ban_user(user, "Администратор забанил человека, не указав причину.")
                elif str(reaction.emoji) == '3️⃣':
                    await message.channel.purge(limit=1)
                    mute_menu_message = await message.channel.send(f"**Времено не работает, воспользуйтесь меню тайм-аута. 🚧**")

                elif str(reaction.emoji) == '🖼':
                    member = message.mentions[0]
                    await message.channel.purge(limit=1)
                    embed = discord.Embed(title="Аватар пользователя", color=discord.Color.blue())
                    embed.set_image(url=member.avatar.url)
                
                    await message.channel.send(embed=embed)


                    mute_reactions = ['1️⃣', '2️⃣', '3️⃣', '🏮', '4️⃣', '5️⃣', '6️⃣']
                    for reaction in mute_reactions:
                        await mute_menu_message.add_reaction(reaction)

                    def mute_reaction_check(reaction, user):
                        return user == message.author and str(reaction.emoji) in mute_reactions and reaction.message.id == mute_menu_message.id

                    try:
                        mute_reaction, _ = await client.wait_for('reaction_add', check=mute_reaction_check, timeout=60)  # Ожидаем 60 секунд

                        # Обрабатываем выбранное время мута
                        if str(mute_reaction.emoji) == '1️⃣':
                            time = 10 * 60  # 10 минут в секундах
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** на **10 минут**")
                        elif str(mute_reaction.emoji) == '2️⃣':
                            time = 30 * 60  # 30 минут в секундах
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** на **30 минут**")
                        elif str(mute_reaction.emoji) == '3️⃣':
                            time = 60 * 60  # 1 час в секундах
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** на **1 час**")
                        elif str(mute_reaction.emoji) == '4️⃣':
                            time = 12 * 60 * 60  # 12 часов в секундах
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** на **12 часов**")
                        elif str(mute_reaction.emoji) == '5️⃣':
                            time = 24 * 60 * 60  # 1 день в секундах
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** на **1 день**")
                        elif str(mute_reaction.emoji) == '6️⃣':
                            time = 0  # Навсегда
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"<{user_mention}> был **замучен** **навсегда!**")


                        user = message.mentions[0]
                        await mute_user(user, time, "Причина мута")

                        if time == 0:
                            print("замутили кагото навсегда чтооо")
                        else:
                            print("что")
                    except asyncio.TimeoutError:
                        await message.channel.send("Превышено время ожидания, меню мута отменено.")
                else:
                    await message.channel.send("Неверная реакция, меню действий отменено.")
            except asyncio.TimeoutError:
                await message.channel.send("Превышено время ожидания, меню действий отменено.")
        else:
            # Если у пользователя нет нужных прав, отправляем сообщение об ошибке
            await message.channel.send("Недостаточно прав для использования этой команды!")



    if "!команды" in message.content:
        commands_text = """# Основное
- !сервер `показывает полезную информацию о сервере, которая может быть интересна пользователю сервера.`
- !очистить [1-1000] `позволяет очистить определённое кол-во сообщений если-же вам это наскучило делать это вручную и вы хотите оптимизировать данный процесс`

# Пинг пользователя 
- ![пинг любого участника] `открывает меню с выбором действий над пользователем`
1. "кикнуть" `кикает пользователя с сервера, человек сможет обратно зайти`
2. "забанить" `банить пользователя с сервера, человек не сможет обратно зайти`
3. "замутить" `создает роль "muted" и автоматически дает её пользователю которого вы выбрали в меню, вы можете выбрать время на которое замутить пользователя. Человек не сможет писать во всех чатах.`

# Для продавцов
!заказ `позволяет вам создать "заказ", вы можете выбрать имя а такжке сумму на которую будет заказ. Пингует everyone и ставит эмодзи на своё сообщение, по нажатию на бот закроет заказ и сделает его недоступным для принятие другими пользователями.`

# Развлечения
- !шар `шар предсказаний, который основывается на случайном выборе картинки, так что не стоит ему верить.`
- !монетка `подбросить монетку которая даст вам ответ да или-же нет.`
- !кость `вы бросаете кость и получаете случайное число от 1 до 6.`
- !число `вы можете выбрать число от которого до которого будет происходить случайная генерация.`
- !угадайка `запускает мини-игру в которой участники сервера должны угадать число от 1 до 100.`
- !безподсказок `запускает угадайку, но только без подсказок меньше или больше, что делает игру интеерстнее для большого круга людей.`

# Экономика
- !передать [пинг человека] [сумма] `передаете сумму участнику которому захотите`
- !баланс `показывает ваш текущий баланс`
- !лидеры `показывает топ по деньгам`
- !кейс 50на50 `открывает кейс за 20рублей из которого может выпасть 30`"""

        max_length = 2000
        parts = [commands_text[i:i + max_length] for i in range(0, len(commands_text), max_length)]

        for part in parts:
            await message.channel.send(part)





    if "!кейсы" in message.content:
        embed = discord.Embed(title="Список кейсов", description="""Пример как правильно писать команду с кейсами : !кейс [название кейса]
        
        **50на50** __25р__ - Хороший кейс для того что-бы проверить свою удачу в равном соревнавание удачи

        **30процентов __10__ - Окупаемый кейс если-же вам выпадет тот самый шанс в 30 процентов

        **дешовый** __5__ - Кейс для начального заработка, поможет выбраться из самого плохого денежного состаяния

        **неоновый** __25р__ - Кейс с легендарным дропов в 150р, поможет окупится
        
        **лиственный** __10р__ - Можно сказать кейс который похож на дешовый по окупаемости, красивое оформление""", color=discord.Color.blue())
        embed.set_image(url="https://media.discordapp.net/attachments/1018623841586659330/1143995116428734554/31313212.png?width=1911&height=916")
        await message.channel.send(embed=embed)


    if "!кость" in message.content:
        number = random.randint(1, 6)
        await message.channel.send(f'Вы бросили кость, и вам выпало число **{number}** 🎲')





    if "!число" in message.content:
        params = message.content.split(" ")
        if len(params) < 2:
            await message.channel.send("Используйте формат: !число [начальное число]-[конечное число]. Пример : !число 1-100")
            return

        params = params[1]
        if '-' in params:
            start, end = map(int, params.split('-'))
            if start > end:
                await message.channel.send("❌ **Неверный** диапазон чисел.")
                return
            number = random.randint(start, end)
            
            message = await message.channel.send(f'🏮 Генерирую случайное число от **{start}** до **{end}**')
            await asyncio.sleep(1)
            await message.edit(content=f'🍁 Генерирую случайное число от **{start}** до **{end}**')
            await asyncio.sleep(1)
            await message.edit(content=f'🔴 Генерирую случайное число от **{start}** до **{end}**')
            await asyncio.sleep(1)
            await message.edit(content=f'📕 Генерирую случайное число от **{start}** до **{end}**')
            await asyncio.sleep(1)
            await message.edit(content=f'🩸 Генерирую случайное число от **{start}** до **{end}**')
            await asyncio.sleep(1)
            await message.edit(content=f'**{number}**')
        else:
            await message.channel.send("Используйте формат: !число [начальное число]-[конечное число]")





    if "!угадайка" in message.content:
        if message.author.guild_permissions.administrator:
            number_to_guess = random.randint(1, 100)
            attempts = 10
            await message.channel.send(f"Я загадал число от **1 до 100**. У вас есть {attempts} попыток.")
            print(f"Я загадал число : {number_to_guess}. Чшшшш")

            def check(m):
                return m.content.isdigit() and m.channel == message.channel

            while attempts > 0:
                try:
                    guess = await client.wait_for('message', check=check)
                    guess = int(guess.content)

                    if guess == number_to_guess:
                        await message.channel.send(f"**✅ Поздравляю, {guess} - это правильное число!**")
                        return
                    elif guess < number_to_guess:
                        await message.channel.send("🔼 Загаданное число **больше**.")
                    else:
                        await message.channel.send("🔽 Загаданное число **меньше**.")

                    attempts -= 1
                    if attempts > 0:
                        await message.channel.send(f"Осталось попыток: **{attempts}**")
                    else:
                        await message.channel.send(f"У вас закончились попытки. Загаданное число было: {number_to_guess}")
                        return

                except ValueError:
                    await message.channel.send("Пожалуйста, введите целое число.")





    if "!безподсказок" in message.content:
        if message.author.guild_permissions.administrator:
            number_to_guess = random.randint(1, 100)
            attempts = 150
            await message.channel.send(f"Я загадал число от **1 до 100**. У вас есть {attempts} попыток.")
            print(f"Я загадал число : {number_to_guess}. Чшшшш ")

            def check(m):
                return m.content.isdigit() and m.channel == message.channel

            while attempts > 0:
                try:
                    guess = await client.wait_for('message', check=check)
                    guess = int(guess.content)

                    if guess == number_to_guess:
                        await message.channel.send(f"✅ **Поздравляю, {guess} - это правильное число!**")
                        return
                    elif guess < number_to_guess:
                        await message.channel.send("❌ Данное число неверное!")
                    else:
                        await message.channel.send("❌ Данное число неверное!")

                    attempts -= 1
                    if attempts > 0:
                        await message.channel.send(f"Осталось попыток: **{attempts}**")
                    else:
                        await message.channel.send(f"У вас закончились попытки. Загаданное число было: {number_to_guess}")
                        return

                except ValueError:
                    await message.channel.send("Пожалуйста, введите целое число.")
                    return






    if message.content == "!коробка":
        user_id = message.author.id

        if user_id in last_opened_time and discord.utils.utcnow().timestamp() - last_opened_time[user_id] < 3 * 60 * 60:
            await message.channel.send("Вы уже открывали коробку в последние 3 часа. Пожалуйста, подождите.")
            return

        image_url = "https://media.discordapp.net/attachments/1018623841586659330/1142250224174243981/42342324234.png?width=682&height=682"
        description = "вы желаете открыть коробку? Там могут выпасть негативные вещи виде мута."
        
        embed = discord.Embed(title="Коробка", description=description, color=0xa33b3b)
        embed.set_image(url=image_url)
        
        sent_message = await message.channel.send(embed=embed)
        await sent_message.add_reaction("✅")
        await sent_message.add_reaction("❌")

        def reaction_check(reaction, user):
            return user == message.author and str(reaction.emoji) in ["✅", "❌"] and reaction.message.id == sent_message.id

        try:
            reaction, _ = await client.wait_for("reaction_add", timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            await message.channel.send("Прошло слишком много времени, выбор отменен.")
            return

        last_opened_time[user_id] = discord.utils.utcnow().timestamp()  # Записываем время открытия

        if str(reaction.emoji) == "✅":
            chances = [
                ("https://media.discordapp.net/attachments/1018623841586659330/1142250313747808287/2a8e61717a2fddf8.png?width=682&height=682", 75),
                ("https://media.discordapp.net/attachments/1018623841586659330/1142250295301251132/9bc079e98e54161d.png?width=682&height=682", 11),
                ("https://media.discordapp.net/attachments/1018623841586659330/1142250272069013504/345345.png?width=682&height=682", 9),
                ("https://media.discordapp.net/attachments/1018623841586659330/1142250303660503130/3123123.png?width=682&height=682", 3),
                ("https://media.discordapp.net/attachments/1018623841586659330/1142250283448152095/312313.png?width=682&height=682", 2)
            ]
            
            random_number = random.randint(1, 100)
            cumulative_chance = 0

            for image, chance in chances:
                cumulative_chance += chance
                if random_number <= cumulative_chance:
                    result_image = image
                    break
            
            result_embed = discord.Embed(title="Вам выпало:", color=0xa33b3b)
            result_embed.set_image(url=result_image)
            
            await message.channel.send(embed=result_embed)
        else:
            await message.channel.send("Вы отказались открыть коробку.")




    if message.content == "!зайди":
        if message.author.voice:  # Check if the author is in a voice channel
            channel = message.author.voice.channel
            await channel.connect()
        else:
            await message.channel.send("не")

    if message.content == "!выйди":
        # Check if the author is in a voice channel
        if message.author.voice:
            voice_channel = message.author.voice.channel
            voice_client = message.guild.voice_client
            
            if voice_client and voice_client.channel == voice_channel:
                await voice_client.disconnect()
                await message.channel.send("Вышел из голосового канала.")
            else:
                await message.channel.send("Я не нахожусь в этом голосовом канале.")
        else:
            await message.channel.send("Вы не находитесь в голосовом канале.")





    if message.content.startswith('!баланс'):
    # Получаем список упомянутых пользователей
        mentioned_users = message.mentions
    
        if mentioned_users:
            user = mentioned_users[0]
        else:
            user = message.author
    
        user_id = str(user.id)
    
        if user_id in balances:
            await message.channel.send(f'💳 Баланс пользователя {user.mention}: {balances[user_id]}')
            #--------------------разделитель удита ----------------------
            audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
            if audit_channel_id is not None:
                audit_channel = client.get_channel(audit_channel_id)
            if audit_channel is not None:
#-----------------------------------------------------------
                    await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Проверка баланса
・Баланс : {user.mention}, {balances[user_id]}""")
#----------------------------------------------------------
        else:
            await message.channel.send(f'🍁 Пользователь {user.mention} еще не зарегистрирован. Используйте команду "!регистрация" для регистрации.')

    elif message.content.startswith('!регистрация'):
        user = str(message.author.id)
        if user not in balances:
            balances[user] = 0
            save_balances()
            await message.channel.send('✅ Вы успешно зарегистрированы! Теперь вам доступен полный функционал бота, переводы, баланс, лидеры и тд.')
            #--------------------разделитель удита ----------------------
            audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
            if audit_channel_id is not None:
                audit_channel = client.get_channel(audit_channel_id)
            if audit_channel is not None:
#-----------------------------------------------------------
                    await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Регистрация.""")
#----------------------------------------------------------
        else:
            await message.channel.send('❌ Вы уже зарегистрированы.')

    elif message.content.startswith('!перевод'):
        command_parts = message.content.split()
        if len(command_parts) != 3:
            await message.channel.send('❌ Используйте команду следующим образом: !перевод [@пользователь] [сумма]')
            return

        _, member_mention, amount_str = command_parts
        member_id = int(member_mention.strip('<@!>'))
        amount = int(amount_str)

        user = str(message.author.id)
        if user in balances and balances[user] >= amount > 0:
            if str(member_id) in balances:
                balances[user] -= amount
                balances[str(member_id)] += amount
                save_balances()
                await message.channel.send(f'🏮 Перевод на сумму {amount} рублей пользователю <@{member_id}> успешно выполнен.')
                #--------------------разделитель удита ----------------------
                audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                if audit_channel_id is not None:
                    audit_channel = client.get_channel(audit_channel_id)
                if audit_channel is not None:
#-----------------------------------------------------------
                    await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Перевод на сумму : {amount} рублей. 
・Получатель : <@{member_id}>""")
            else:
                await message.channel.send('Пользователь не зарегистрирован.')
        else:
            await message.channel.send('❌Транзакция отказана, недостаточно средств.')

    elif message.content.startswith('!лидеры'):
        sorted_balances = sorted(balances.items(), key=lambda x: x[1], reverse=True)
        leaderboard_message = "🏮 Топ пользователей по балансу:\n"

        for index, (user_id, balance) in enumerate(sorted_balances[:10], start=1):
            user = await client.fetch_user(int(user_id))
            leaderboard_message += f"{index}. {user.name}: {balance} рублей\n"

        await message.channel.send(leaderboard_message)

    elif message.content.startswith('!выдать'):
        if message.author.guild_permissions.administrator:
            command_parts = message.content.split()
            if len(command_parts) != 3:
                await message.channel.send('Используйте команду следующим образом: !выдать @пользователь сумма')
                return

            _, member_mention, amount_str = command_parts
            member_id = int(member_mention.strip('<@!>'))
            amount = int(amount_str)

            if str(member_id) in balances:
                balances[str(member_id)] += amount
                save_balances()
                await message.channel.send(f'💳 Вы успешно выдали {amount} рублей пользователю <@{member_id}>. Данная транзакция не нуждается в доп. подтверждениях')
                audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
                if audit_channel_id is not None:
                    audit_channel = client.get_channel(audit_channel_id)
                if audit_channel is not None:
            # Отправляем сообщение аудита в указанный канал
                    await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Выдача на сумму : {amount} рублей. 
・Получатель : <@{member_id}>""")
            else:
                await message.channel.send('Пользователь не зарегистрирован.')
        else:
            await message.channel.send('У вас нет прав на использование этой команды.')

    elif message.content.startswith('!убрать'):
        if message.author.guild_permissions.administrator:
            command_parts = message.content.split()
            if len(command_parts) != 3:
                await message.channel.send('Используйте команду следующим образом: !убрать @пользователь сумма')
                return

            _, member_mention, amount_str = command_parts
            member_id = int(member_mention.strip('<@!>'))
            amount = int(amount_str)

            if str(member_id) in balances:
                if balances[str(member_id)] >= amount:
                    balances[str(member_id)] -= amount
                    save_balances()
                    await message.channel.send(f'Вы успешно убрали {amount} рублей у пользователя <@{member_id}>.')
                    #--------------------разделитель удита ----------------------
                    audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                    if audit_channel_id is not None:
                        audit_channel = client.get_channel(audit_channel_id)
                    if audit_channel is not None:
#-----------------------------------------------------------
                        await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Убирание денег на сумму : {amount} рублей. 
・Получатель : <@{member_id}>""")
#----------------------------------------------------------
                else:
                    await message.channel.send('У пользователя недостаточно монет для удаления.')
            else:
                await message.channel.send('Пользователь не найден.')
        else:
            await message.channel.send('У вас нет прав на использование этой команды.')

    elif message.content.startswith('!кейс 50на50'):
        user = str(message.author.id)
        if user in balances and balances[user] >= 20:
            await message.channel.send(f"""Шансы выпадения в данном кейсе :
🟢**50%** - Пусто
🟠**50%** - 30 Рублей""")
            embed = discord.Embed(title='Покупка кейса "50на50"', description='Вы действительно хотите купить кейс "50на50"?\nС вашего баланса будет списано 20 рублей', color=discord.Color.blue())
            embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142538793400934533/f3b31387082df286.png?width=682&height=682')
            confirmation_message = await message.channel.send(embed=embed)
            await confirmation_message.add_reaction('✅')
            await confirmation_message.add_reaction('❌')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message == confirmation_message

            try:
                reaction, _ = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if str(reaction.emoji) == '✅':
                    balances[user] -= 20
                    save_balances()
                    if random.random() < 0.6:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам не повезло', color=discord.Color.green())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142538809045688390/3123133.png?width=682&height=682')
                        #--------------------разделитель удита ----------------------
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 20 рублей, 50на50. 
・Выпало : 0 рублей.""")
#----------------------------------------------------------
                    else:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам повезло!', color=discord.Color.orange())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142538801311399966/31312312.png?width=682&height=682')
                        if random.random() < 0.4:
                                                    #--------------------разделитель удита ----------------------
                            audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                            if audit_channel_id is not None:
                                audit_channel = client.get_channel(audit_channel_id)
                            if audit_channel is not None:
#-----------------------------------------------------------
                                await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 20 рублей, 50на50. 
・Выпало : 30 рублей.""")
#----------------------------------------------------------
                            balances[user] += 30
                            save_balances()
                    await message.channel.send(embed=embed)
                elif str(reaction.emoji) == '❌':
                    await message.channel.send('Покупка отменена.')
            except asyncio.TimeoutError:
                await message.channel.send('Время на подтверждение истекло.')
        else:
            await message.channel.send('У вас недостаточно рублей для покупки кейса.')

    elif message.content.startswith('!кейс 30процентов'):
        user = str(message.author.id)
        if user in balances and balances[user] >= 10:
            await message.channel.send(f"""Шансы выпадения в данном кейсе :
🟢**69%** - Пусто
🟠**30%** - 20 Рублей
🟡**1%** - **100 Рублей**""")
            embed = discord.Embed(title='Покупка кейса 30 процентов', description='Вы действительно хотите купить кейс "30 процентов"?\nС вашего баланса будет списано 10 рублей', color=0xBB4E76)
            embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142952314253086811/31231332.png?width=682&height=682')
            confirmation_message = await message.channel.send(embed=embed)
            await confirmation_message.add_reaction('✅')
            await confirmation_message.add_reaction('❌')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message == confirmation_message

            try:
                reaction, _ = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if str(reaction.emoji) == '✅':
                    balances[user] -= 10
                    save_balances()

                    if random.random() < 0.01:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вы выиграли 100 рублей!', color=discord.Color.gold())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142957438069395556/313131213.png?width=916&height=916')
                        balances[user] += 100
                        save_balances()
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 10 рублей, 30процентов. 
・Выпало : 100 рублей.""")
#----------------------------------------------------------
                    elif random.random() < 0.40:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам выпало 20 рублей', color=discord.Color.orange())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142952357932564561/43243324423.png?width=916&height=916')
                        balances[user] += 20
                        save_balances()
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 10 рублей, 30проценов. 
・Выпало : 20 рублей.""")
#----------------------------------------------------------
                    else:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам не повезло', color=discord.Color.green())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1142952369630494840/2423442342424.png?width=916&height=916')
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 10 рублей, 30процентов. 
・Выпало : 0 рублей.""")
#----------------------------------------------------------

                    await message.channel.send(embed=embed)
                elif str(reaction.emoji) == '❌':
                    await message.channel.send('⛔ Покупка отменена.')
            except asyncio.TimeoutError:
                await message.channel.send('Время на покупку истекло.')
        else:
            await message.channel.send('У вас недостаточно монет для покупки кейса.')

    elif message.content.startswith('!ресет'):
        if message.author.guild_permissions.administrator:
            command_parts = message.content.split()
            if len(command_parts) == 1:
                user = str(message.author.id)
                balances[user] = 0
                save_balances()
                await message.channel.send(f'📢 Ваш баланс сброшен до 0.')
            elif len(command_parts) == 2:
                _, member_mention = command_parts
                member_id = int(member_mention.strip('<@!>'))

                if str(member_id) in balances:
                    balances[str(member_id)] = 0
                    save_balances()
                    await message.channel.send(f'📢 Баланс пользователя <@{member_id}> сброшен до 0.')
                else:
                    await message.channel.send('Пользователь не найден.')
            else:
                await message.channel.send('Используйте команду следующим образом: !ресет [@пользователь]')

        else:
            await message.channel.send('У вас нет прав на использование этой команды.')




    elif message.content.startswith('!кейс дешовый'):
        user = str(message.author.id)
        if user in balances and balances[user] >= 5:
            await message.channel.send(f"""Шансы выпадения в данном кейсе :
🟢**65%** - Пусто
🟠**20%** - 10 Рублей
🟡**15%** - **15 Рублей**""")
            embed = discord.Embed(title='Покупка кейса "дешовый"', description='Вы действительно хотите купить кейс "дешовый"?\nС вашего баланса будет списано 5 рублей', color=0x7A3C1E)
            embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1143332636090175528/313131.png?width=916&height=916')
            confirmation_message = await message.channel.send(embed=embed)
            await confirmation_message.add_reaction('✅')
            await confirmation_message.add_reaction('❌')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message == confirmation_message

            try:
                reaction, _ = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if str(reaction.emoji) == '✅':
                    balances[user] -= 5
                    save_balances()

                    if random.random() < 0.15:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вы выиграли 15 рублей!', color=discord.Color.gold())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1143332689777266831/3123131.png?width=916&height=916')
                        balances[user] += 15
                        save_balances()
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 5 рублей, дешовый. 
・Выпало : 15 рублей.""")
#----------------------------------------------------------
                    elif random.random() < 0.20:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам выпало 10 рублей', color=discord.Color.orange())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1143332678117097562/1312132.png?width=916&height=916')
                        balances[user] += 10
                        save_balances()
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 5 рублей, дешовый. 
・Выпало : 10 рублей.""")
#----------------------------------------------------------
                    else:
                        embed = discord.Embed(title='Вы открыли кейс', description='Вам не повезло', color=discord.Color.green())
                        embed.set_image(url='https://media.discordapp.net/attachments/1018623841586659330/1143332664930222100/312313131.png?width=916&height=916')
                        audit_channel_id = 1144405401576681553  # Замените на ID вашего канала аудита
#-----------------------------------------------------------
                        if audit_channel_id is not None:
                            audit_channel = client.get_channel(audit_channel_id)
                        if audit_channel is not None:
#-----------------------------------------------------------
                            await audit_channel.send(f"""🏮 Сервер : {message.guild.name}
・Исполнитель : **<@{message.author.id}>** 
・Действие : Открытие кейсы за : 5 рублей, дешовый. 
・Выпало : 0 рублей.""")
#----------------------------------------------------------

                    await message.channel.send(embed=embed)
                elif str(reaction.emoji) == '❌':
                    await message.channel.send('⛔ Покупка отменена.')
            except asyncio.TimeoutError:
                await message.channel.send('Время на покупку истекло.')
        else:
            await message.channel.send('У вас недостаточно монет для покупки кейса.')



    if "!выдать 158 э" in message.content:
        await message.channel.send("")




















































    if message.content.startswith('!розыгрыш'):
        await message.channel.send("Введите описание розыгрыша:")
        
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            response = await client.wait_for('message', check=check, timeout=60)
            описание_розыгрыша = response.content

            await message.channel.send("Введите время длительности розыгрыша (например, 1с, 1м, 1ч, 1д):")

            response = await client.wait_for('message', check=check, timeout=2000)
            время_длительности = response.content
            await message.channel.send(f"@everyone Начинаю розыгрыш! В честь 1000 отзывов на нашем фанпей. 🏮")

            await asyncio.sleep(parse_time(время_длительности))

            сообщение_розыгрыша = await message.channel.send(f"**Розыгрыш на '{описание_розыгрыша}' начался! Нажмите на реакцию, чтобы участвовать! Всем удачи :)**")
            await сообщение_розыгрыша.add_reaction('🏮')

            участники = []

            def check_reaction(reaction, user):
                return str(reaction.emoji) == '🏮' and reaction.message.id == сообщение_розыгрыша.id

            while True:
                try:
                    reaction, user = await client.wait_for('reaction_add', check=check_reaction, timeout=2000)
                    if user not in участники:
                        участники.append(user)
                except asyncio.TimeoutError:
                    break

            if not участники:
                await message.channel.send("На реакцию '!розыгрыш' не нажал ни один участник.")
            else:
                победитель = random.choice(участники)
                await message.channel.send(f"🍁 Победитель розыгрыша на '{описание_розыгрыша}' - **{победитель.mention}**! Поздравляем 🎉")
        except asyncio.TimeoutError:
            await message.channel.send("Время ожидания истекло. Розыгрыш отменен.")

def parse_time(время):
    секунды = 0
    try:
        if время.endswith('с'):
            секунды = int(время[:-1])
        elif время.endswith('м'):
            секунды = int(время[:-1]) * 60
        elif время.endswith('ч'):
            секунды = int(время[:-1]) * 60 * 60
        elif время.endswith('д'):
            секунды = int(время[:-1]) * 60 * 60 * 24
    except ValueError:
        pass
    return секунды

# Запускаем бота
client.run(TOKEN)
