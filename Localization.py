﻿# -*- coding: utf-8 -*-
'''
    Torrenter plugin for XBMC
    Copyright (C) 2012 Vadim Skorba
    vadim.skorba@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
try:
    import xbmcaddon

    __settings__ = xbmcaddon.Addon(id='plugin.video.torrenter')

    language = ('en', 'ru')[int(__settings__.getSetting("language"))]
except:
    language = 'ru'

dictionary = {
    'ru': {
        'Seeds searching.': 'Идёт поиск сидов.',
        'Please Wait': 'Подождите',
        'Information': 'Информация',
        'Torrent downloading is stopped.': 'Загрузка торрента прекращена.',
        'Search': 'Поиск',
        'Seeds': 'Сиды',
        'Peers': 'Пиры',
        'Materials are loading now.': 'Идёт загрузка материалов.',
        'Search Phrase': 'Фраза для поиска',
        'Magnet-link is converting.': 'Идёт преобразование magnet-ссылки.',
        'Error': 'Ошибка',
        'Your library out of date and can\'t save magnet-links.': 'Ваша библиотека устарела и не может сохранять магнет-ссылки.',
        'Bookmarks': 'Закладки',
        'Logout': 'Выход',
        'Login': 'Вход',
        'Recent Materials': 'Свежие Материалы ',
        'Register': 'Регистрация',
        'Bookmark': 'Закладка',
        'Item successfully added to Bookmarks': 'Элемент удачно добавлен в закладки',
        'Item successfully removed from Bookmarks': 'Элемент удачно удалён из закладок',
        'Bookmark not added': 'Закладка не добавлена',
        'Bookmark not removed': 'Закладка не удалена',
        'Add To Bookmarks': 'Добавить в закладки',
        'Remove From Bookmarks': 'Удалить из Закладок',
        'Auth': 'Авторизация',
        'Already logged in': 'Пользователь уже в системе',
        'Input Email (for password recovery):': 'Введите E-mail (для восстановления пароля):',
        'Input Email:': 'Введите E-mail:',
        'Input Password (6+ symbols):': 'Введите пароль (6+ символов):',
        'Input Password:': 'Введите пароль:',
        'Login successfull': 'Вход выполнен успешно',
        'Login failed': 'Вход не выполнен',
        'User not logged in': 'Пользователь не в системе',
        'User successfully logged out': 'Пользователь успешно покинул систему',
        'Preloaded: ': 'Предзагружено: ',
        'Do you want to STOP torrent downloading and seeding?': 'Вы хотите остановить загрузку и раздачу торрента?',
        'Torrent Downloading': 'Загрузка торрента',
        'Auth expired, please relogin': 'Авторизация истекла, пожалуйста войдите снова',
        'Storage': 'Хранилище',
        'Storage was cleared': 'Хранилище очищено',
        'Clear Storage': 'Очистить хранилище',
        'Popular': 'Популярное',
        'Views': 'Просмотров',
        'Uploading': 'Раздача',
        'Download': 'Скачать',
        'Input symbols from CAPTCHA image:': 'Введите символы с картинки CAPTCHA:',
        'Please, rate watched video:': 'Пожалуйста, оцените просмотренное видео:',
        'Bad': 'Плохо',
        'So-So': 'Такое...',
        'Good': 'Отлично',
        'Ratings': 'Оценки',
        'Rating': 'Оценка',
        'Retry': 'Повторная попытка',
        '%ds has left': 'Осталось %d попыток',
        'File failed to play! Do you want to RETRY and buffer more?': 'Ошибка проигрывания файла! Хотите предзагрузить больше и повторить?',
        'High Priority All Files': 'Высокий Приоритет Всем Файлам',
        'Skip All Files': 'Пропустить Все Файлы',
        'Start': 'Пуск',
        'Stop': 'Стоп',
        'High Priority': 'Высокий Приоритет',
        'Skip File': 'Пропустить Файл',
        'Remove': 'Удалить',
        'Remove with files': 'Удалить с файлами',
        'Play File': 'Проиграть файл',
        'Start All Files': 'Пуск Всем Файлам',
        'Stop All Files': 'Стоп Всем Файлам',
        'Torrent-client Browser': 'Браузер Торрент-клиента',
        'Remote Torrent-client': 'Удаленный торрент-клиент',
        'You didn\'t set up replacement path in setting.': 'Вы не настроили замены путей.',
        'For example /media/dl_torr/ to smb://SERVER/dl_torr/. Setup now?': 'Например /media/dl_torr/ на smb://SERVER/dl_torr/. Настроить?',
        'Manual Torrent-client Path Edit': 'Вручную изменить папку торрент-клиента по-умолчанию',
        'Choose .torrent in video library': 'Выберите .torrent в видеобиблиотеке',
        '.torrent Player': '.torrent Проигрыватель',
        'Choose directory:': 'Выберите папку:',
        'Starting download next episode!': 'Начинаю скачку следующего эпизода!',
        'Choose in torrent-client:': 'Выберите раздачу:',
        'Search Control Window': 'Окно Управления Поиском',
        'Magnet-link (magnet:...)': 'Magnet-ссылка (magnet:...)',
        'Not a magnet-link!': 'Не является magnet-ссылкой',
        'Magnet-link Player': 'Проигрыватель Magnet-Ссылок',
        'UNKNOWN STATUS': 'Неизвестное состояние',
        'Checking preloaded files...': 'Проверка файлов...',
        'Waiting for website response...': 'Ожидание ответа сайта...',
        'Search and cache information for:': 'Поиск и кэширование информации для:',
        'Open Torrent': 'Открыть Список файлов',
        'Torrent list is empty.': 'Список раздач пуст.',
        'Content Lists': 'Списки Медиа',
        'Canceled by User': 'Отменено пользователем',
        'Do you want to search and cache full metadata + arts?': 'Хотите автоматически получать мета-данные и арты?',
        'This vastly decreases load speed, but you will be asked to download premade bases!': 'Это существенно снижает скорость загрузки, но Вам предложат скачать готовые базы!',
        'Do you want to preload full metadata?': 'Хотите готовую загрузить базу данных?',
        'It is highly recommended!': 'Настоятельно рекомендовано согласиться!',
        'TV Shows': 'Сериалы',
        'Cartoons': 'Мультфильмы',
        'Anime': 'Аниме',
        'Hot & New': 'Горячие Новинки',
        'Top 250 Movies': 'Лучшие 250 фильмов',
        'Top All Time': 'Лучшее за ВСЕ ВРЕМЯ',
        'by Genre': 'по Жанру',
        'by Year': 'по Году',
        'Action': 'Боевики',
        'Adventure': 'Приключения',
        'Animation': 'Анимация',
        'Biography': 'Биография',
        'Comedy': 'Комедии',
        'Crime': 'Детектив',
        'Documentary': 'Документальное',
        'Drama': 'Драмы',
        'Family': 'Семейное',
        'Fantasy': 'Фэнтази',
        'Film-Noir': 'Нуар',
        'History': 'Историчекие',
        'Horror': 'Ужасы',
        'Music': 'Музыкальные',
        'Musical': 'Мьюзиклы',
        'Mystery': 'Мистика',
        'Romance': 'Мелодрамы',
        'Sci-Fi': 'Фантастика',
        'Short': 'Короткометражки',
        'Sport': 'Спортивные',
        'Thriller': 'Триллеры',
        'War': 'Военные',
        'Western': 'Вестерны',
        '[B]by Site[/B]': '[B]по Сайту[/B]',
        'Movies': 'Фильмы',
        'Cartoons Series': 'Мультсериалы',
        'Cartoons Short': 'Мультфильмы (короткометражки)',
        'Male': 'Мужские',
        'Female': 'Женские',
        'Russia & USSR': 'Россия + СССР',
        'Next Page': 'Следующая Страница',
        'Previous Page': 'Предыдущая Страница',
        'Russian Movies': 'Отечественные Фильмы',
        'Forieng Movies': 'Зарубежные Фильмы',
        'Anime Film': 'Полнометражное Аниме',
        'Anime Series': 'Аниме Сериалы',
        'Can\'t download torrent, probably no seeds available.': 'Не могу скачать торрент, скорее всего нет доступных сидов.',
        'Personal List': 'Личный Список',
        'Add to %s': 'Добавить в %s',
        'Delete from %s': 'Удалить из %s',
        'Added!': 'Добавлено',
        'Deleted!': 'Удалено!',
        'Search History': 'История Поиска',
        'Favourites': 'Избранное',
        'Favourites SH': 'Избранное ИП',
        'Clear Search History': 'Очистить Историю Поиска',
        'Clear!': 'Очищено!',
        'kb/s': 'Кб/с',
        'Queued': 'В очереди',
        'Checking': 'Проверка',
        'Downloading metadata': 'Скачивание мета-данных',
        'Downloading': 'Скачивание',
        'Finished': 'Окончено',
        'Seeding': 'Раздача (сидирование)',
        'Allocating': 'Allocating',
        'Allocating file & Checking resume': 'Allocating file & Checking resume',
        'For Kids': 'Детское',
        'Adult': 'Эротика',
        'Does not support magnet links!': 'Не поддерживает магнит-ссылки!',
        'Reset All Cache DBs': 'Сбросить Базы Данных',
        '[B]Search[/B]': '[B]Поиск[/B]',
        'You can always restart this by deleting DBs via Context Menu': 'Вы всегда можете перезапустить этот процесс через Контекстное Меню',
        'Your preloaded databases are outdated!': 'Ваши предзакаченные базы метаданных устарели!',
        'Do you want to download new ones right now?': 'Хотите прямо сейчас скачать новые?',
        'Individual Tracker Options':'Выбор Трекеров',
        'Downloading and copy subtitles. Please wait.':'Скачиваю и копирую субтитры. Пожалуйста подождите.',
        'International Check - First Run':'International Check - Первый запуск',
        'Delete Russian stuff?':'Удалить русские трекеры?',
        'Save to path':'Сохранить в папку',
    }
}


def localize(text):
    try:
        return dictionary[language][text]
    except:
        return text
