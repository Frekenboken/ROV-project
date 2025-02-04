import asyncio
import cv2
import numpy as np
import websockets
import json

camera = cv2.VideoCapture(0)
clients = set()

async def send_data(websocket):
    """ Отправка изображения и данных клиенту """
    while True:
        ret, frame = camera.read()
        if not ret:
            continue

        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        img_bytes = buffer.tobytes()

        data = {
            "info": {"temp": 22.5, "status": "active"},
            "image": img_bytes.hex()
        }

        try:
            await websocket.send(json.dumps(data))
        except:
            break  # Клиент отключился
        await asyncio.sleep(0.033)  # ~30 FPS

async def handle_client(websocket, path):
    """ Обработка соединения с клиентом """
    clients.add(websocket)
    print(f"Клиент подключен: {len(clients)}")

    try:
        send_task = asyncio.create_task(send_data(websocket))
        async for message in websocket:
            command = json.loads(message).get("command", "noop")
            print(f"Получена команда: {command}")
    except:
        pass
    finally:
        send_task.cancel()
        clients.remove(websocket)
        print(f"Клиент отключен: {len(clients)}")

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 8080)
    print("Сервер запущен на порту 8080")
    await server.wait_closed()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Сервер остановлен")
finally:
    camera.release()
