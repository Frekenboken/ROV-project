import asyncio
import json
import cv2
import numpy as np
import aiohttp
from aiohttp import web

# Глобальные переменные
camera = cv2.VideoCapture(0)  # Камера
clients = set()  # Подключенные клиенты

async def handle_request(request):
    """ Обработчик запросов от клиента """
    try:
        data = await request.json()
        command = data.get("command", "noop")  # Получаем команду
        response_data = {"status": "ok", "received_command": command}

        # Захватываем кадр с камеры
        ret, frame = camera.read()
        if not ret:
            response_data["error"] = "Failed to capture frame"
        else:
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            response_data["image"] = buffer.tobytes().hex()  # Отправляем кадр в hex-формате

        response_data["info"] = {"temp": 22.5, "status": "active"}  # Пример данных

        return web.json_response(response_data)
    except Exception as e:
        return web.json_response({"error": str(e)})

async def start_server():
    """ Запуск сервера """
    app = web.Application()
    app.router.add_post("/control", handle_request)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("Сервер запущен на порту 8080")

async def main():
    await start_server()
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Сервер остановлен")
finally:
    camera.release()
