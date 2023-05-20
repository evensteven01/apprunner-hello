from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "AppRunner world!"}


if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8081)),
        log_level=os.getenv('LOG_LEVEL', "info"),
        proxy_headers=True
    )
