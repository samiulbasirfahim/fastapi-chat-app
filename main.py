from fastapi import FastAPI
from socketio import AsyncServer, ASGIApp


app = FastAPI(
    title="CHAT backend",
    version="1.0.0"
)

sio = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=['*']
)

sio_app = ASGIApp(sio)


app.mount('/socket.io', sio_app)
