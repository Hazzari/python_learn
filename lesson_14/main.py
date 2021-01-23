from instabot import Bot

bot = Bot()
bot.login(username='Haz.zari', password='Qazxcde321')

user_followers = bot.get_user_followers('Haz.zari')  # Список подписчиков
user_following = bot.get_user_following('Haz.zari')  # Список подписок

print(user_followers)
print(user_following)
