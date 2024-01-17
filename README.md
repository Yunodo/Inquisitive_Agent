# Название: Inquisitive Agent

## Описание

Данная служба позволяет пользователям заполнить набор информационных полей в диалоговом режиме. Она использует API GigaChat для извлечения соответствующей информации из ответов пользователя.

## Как это работает

Запрос поля: Служба запрашивает у пользователя название поля, которое необходимо заполнить.

Ввод ответа: Пользователь вводит ответ, а служба использует API GigaChat для извлечения релевантной информации.

Сохранение данных: Извлеченная информация сохраняется в словаре.

Итерация по полям: Шаги 1-3 повторяются, пока все поля не будут заполнены.

Подтверждение: Служба запрашивает у пользователя подтверждение правильности 
введенной информации.

Вывод результата: При подтверждении, служба возвращает заполненный словарь.


## Возможные улучшения

### Улучшение диалогового интерфейса:
Использование более естественного и понятного языка при запросах.
Расширение вариантов ответов, принимаемых как верных.
Предоставление подсказок и уточнений при нечетких ответах.

### Интеграция с другими сервисами:
Сохранение заполненной информации в базу данных.
Автоматическое заполнение полей, если информация уже имеется в других сервисах.
Подключение к сторонним API для дополнительной проверки введенных данных.

### Улучшение обработки ошибок:
Более информативные сообщения об ошибках при неверных запросах или ответах.
Возможность исправления ошибок без полного перезапуска процесса.

### Расширение функциональности:
Добавление поддержки для различных типов данных (дата, адрес, номер телефона).
Разработка интерфейса для настройки списка запрашиваемых полей.
Возможность настройки уровня детализации извлекаемой информации.


### Как запускать контейнер

``docker build -t <image_name> . ``

``docker run -it <image_name>``

Также в папке с кодом нужно создать ``.env`` файл и внутри прописать ``GIGACHAT_CREDENTIALS=<>``
