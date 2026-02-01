from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/webhook")
async def receive_webhook(request: Request):
    try:
        payload = await request.json()
    except:
        payload = (await request.body()).decode(errors="ignore")

    return {
        "status": "ok",
        "received": payload
    }
