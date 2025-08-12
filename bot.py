import discord
import random
import datetime
from bot_mantik import gen_pass


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$merhaba'):
        await message.channel.send("Merhaba!")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$nasılsın'):
        await message.channel.send("Ben bir botum, duygularım yok ama sen nasılsın?")

    elif message.content.startswith('$saat kaç'):
        now = datetime.datetime.now()
        await message.channel.send(f"Şu an saat: {now.strftime('%H:%M:%S')}")

    elif message.content.startswith('$bilmece sor'):
        await message.channel.send("tamam. İşte bir bilmece: 'Bütün gün çalışır, ama hiç yorulmaz. O nedir?'")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            cevap = await client.wait_for('message', check=check, timeout=10.0)
            if cevap.content.lower() == 'saat':
                await message.channel.send("Doğru cevap! Tebrikler!")
            else:
                await message.channel.send("Yanlış cevap! Doğru cevap 'saat' olacaktı.")
        except Exception:
            await message.channel.send("Süre doldu! Doğru cevap 'saat' olacaktı.")

    elif message.content.startswith('$oyun oynayalım'):
        await message.channel.send("tamam, sayı tahmin etme oyunu oynayabiliriz. 1 ile 10 arasında bir sayı söyle, süren başladı!")
        answer = random.randint(1, 10)

        def is_correct(m):
            return m.author == message.author and m.channel == message.channel and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
            if int(guess.content) == answer:
                await message.channel.send('Doğru bildin!')
            else:
                await message.channel.send(f'Yanlış! Doğru cevap {answer} olacaktı.')
        except Exception:
            await message.channel.send(f'Süre doldu! Doğru cevap {answer} olacaktı.')

    else:
        await message.channel.send("Şifreniz: " + gen_pass(10))


client.run("token yazınız")