# Movie Recommendation System

## Описание

Система рекомендаций фильмов, которая анализирует последние оценки пользователя и предлагает фильмы на основе
совпадающих тегов и других критериев.

### Работа системы:

1. Анализируются пять последних оценок пользователя. Если их менее 10, используются все доступные оценки.
2. Из этих оценок извлекаются теги фильмов.
3. Подбираются фильмы, содержащие хотя бы один из этих тегов.
4. Если у пользователя есть любимые фильмы, учитываются только те фильмы, что содержат теги из этого списка.
5. Из списка выбираются фильмы, выпущенные за последние 6 месяцев.
6. Если фильмов менее 10, возвращаются все найденные.
7. Фильмы сортируются по количеству совпадающих тегов и возвращается 10 наиболее релевантных.

## Установка и настройка

1. **Клонирование репозитория**:
   -     git clone https://github.com/sntx10/System-Recommendation.git
2. **Создание виртуального окружения**:
   -     python3 -m venv <название окружение>
3. **Активация виртуального окружения**:
   -     source <название окружение>/bin/activate
4. **Установка зависимостей**:
   -     pip3 install -r requirements.txt
5. **Настройка конфигурации**:
- Переименуйте файл `env_example` в `.env`.
- Обновите значения в файле `.env` соответствующим образом.
6. **Миграция базы данных**:
   -     python3 manage.py migrate
7. **Запуск сервера**:
   -     python3 manage.py runserver
