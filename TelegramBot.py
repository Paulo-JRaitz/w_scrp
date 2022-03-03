from typing import Tuple

from Helpers import Helpers
from TelegramNotificationConfig import TelegramNotificationConfig
from ThingsInformation import ThingsInformation


class TelegramBot:
    urlSite_tagId = [
        ('https://selecao.ifmt.edu.br/', 'ctl00_ContentPlaceHolderPrincipal_grvInscricoes')
    ]

    for value in urlSite_tagId:
        concursos = ThingsInformation.getInformationOfThings(value[0], value[1])

        verify = Helpers.validation(concursos)

        if verify == 1:
            TelegramNotificationConfig.sendTelegramNotification(concursos)
