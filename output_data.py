import dictionary as d
from aiogram.types import Message, CallbackQuery
import keyboards as kb
import datetime
from aiogram import html

"""Вывод полученной информации о погоде"""
async def output_weather(message: Message, data, city):
    weather_description = data['weather'][0]['main']
            
    if weather_description in d.code_to_smile:
        wd = d.code_to_smile[weather_description]
    else:
        wd = ''
    
    cur_weather = round(data['main']['temp'], 1); prefix = '+' if cur_weather >= 1.0 else ''
    humidity = data['main']['humidity']
    pressure = round(data['main']['pressure'] / 1.33322)
    wind = data['wind']['speed']

    sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone'], tz=datetime.timezone.utc)
    sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'], tz=datetime.timezone.utc)
    length_day = sunset_timestamp - sunrise_timestamp
    
    await message.answer(
        f"🗓 {html.bold(d.weather_indicators[8])} {html.italic(datetime.datetime.now().strftime('%d.%m.%Y %H:%M'))} 🗓\n\n\n"
        f"🌍 {html.bold(d.weather_indicators[0])} {html.italic(city.title())}\n\n"
        f"🌡 {html.bold(d.weather_indicators[1])} {prefix}{cur_weather}°C {html.bold(wd)}\n\n"
        f"💧 {html.bold(d.weather_indicators[2])} {humidity}%\n\n"
        f"🗿 {html.bold(d.weather_indicators[3])} {pressure} мм.рт.ст\n\n"
        f"🍃 {html.bold(d.weather_indicators[4])} {wind} м/с\n\n"
        f"🌅 {html.bold(d.weather_indicators[5])} {sunrise_timestamp.strftime('%H:%M')}\n\n"
        f"🌇 {html.bold(d.weather_indicators[6])} {sunset_timestamp.strftime('%H:%M')}\n\n"
        f"☀ {html.bold(d.weather_indicators[7])} {str(length_day)[:2]} ч. {str(length_day)[3:5]} м."
    )
    
"""Вывод информации о профиле пользователя"""
async def output_profil_data(message: Message, city_name):
    await message.answer(
        f"ℹ️ {html.italic(d.profil_settings[0])}\n\n"
        f"🏙️ {d.profil_settings[1]} {html.bold(city_name)}",
        
        reply_markup=kb.profile_settings
    )
