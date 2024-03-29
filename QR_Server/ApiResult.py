# Результаты выполнения запроса к сервису работы с сообщениями
class ApiResult:
    Ok = 0  # Запрос выполнен успешно
    JsonFieldMissing = 100  # Не переданы все обязательные поля
    ParsePacketError = 101  # Некорректный пакет
    JsonSyntaxError = 102  # Ошибка парсинга. Не хватает закрывающей скобки или запятой
    SenderNotReady = 103  # Сервис отправки сообщений не может обработать сообщение в данный момент
    FileNotExist = 104  # Файл с контентом не существует. Возможно не было передано изображение
    BadReceiver = 105  # Некорректный получатель сообщения
    Timeout = 106  # Сервер не дождался всех фрагментов команды
    Unauthorized = 107  # Не совпал token аутентификации