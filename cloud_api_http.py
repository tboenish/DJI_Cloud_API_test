#!/usr/bin/env python3
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

host_addr = "192.168.88.14"
username = ""
password = ""

app = FastAPI()


@app.get("/login")
async def pilot_login():
    file_path = "./couldhtml/login.html"
    with open(file_path, 'r',encoding="UTF-8") as file:
        file_content = file.read()
    file_content = file_content.replace("hostnamehere", host_addr)
    file_content = file_content.replace("userloginhere", username)
    file_content = file_content.replace("userpasswordhere", password)
    #print(file_content)
    return HTMLResponse(file_content)


if __name__ == "__main__":
    uvicorn.run(app, host=host_addr, port=5000)
