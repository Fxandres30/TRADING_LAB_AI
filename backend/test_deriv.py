import json
import websocket

TOKEN = "pat_7c5ba7e81bb78a8cceffee7f3e3ed561bfe15eadfdc6bdaeb47d89cd019dc556"

ws = websocket.create_connection(
    "wss://ws.derivws.com/websockets/v3?app_id=1089"
)

ws.send(json.dumps({
    "authorize": TOKEN
}))

print(ws.recv())