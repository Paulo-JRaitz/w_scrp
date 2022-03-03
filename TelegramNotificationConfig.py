import requests


class TelegramNotificationConfig:
    def sendTelegramNotification(self):
        telegramBotUrl = 'https://api.telegram.org/bot'
        chatId = '123'
        messageToSend = f'{telegramBotUrl}sendMessage?chat_id={chatId}&text={self}'
        requests.get(messageToSend)