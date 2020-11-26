#!/usr/bin/env python
# coding=utf-8

'''
Version: 0.1
Autor: zmf96
Email: zmf96@qq.com
Date: 2020-11-19 14:29:06
LastEditors: zmf96
LastEditTime: 2020-11-19 14:29:17
FilePath: \main.py
Description: 
'''

import os
import secrets
import sys
import threading
import time
from datetime import timedelta, timezone
from PIL import Image,ImageDraw, ImageFont

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status,Form
from fastapi.responses import RedirectResponse,FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from loguru import logger

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static/"), name="static")
app.mount("/dist", StaticFiles(directory="./static/dist"), name="dist")
app.mount("/data",StaticFiles(directory="./data"),name="data")
templates = Jinja2Templates(directory="templates")

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "hot")
    correct_password = secrets.compare_digest(credentials.password, "invitation")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html",{"request": request}
    )


@app.get("/2020/")
async def portrait(request: Request, username: str = Depends(get_current_username)):
    _pngname = "base"
    return templates.TemplateResponse(
        "2020.html", {"request": request,         
        'pngname':_pngname}
    )

# 思源黑体
def draw_image(text,x=0,y=60):
    new_image = Image.open("./data/base.png")
    draw = ImageDraw.Draw(new_image)
    img_size = new_image.size
    try:
        fnt = ImageFont.truetype("./data/base.ttf",80)
        fnt_size = fnt.getsize(text)
        x1 = (img_size[0]-fnt_size[0])/2+x
        y1 = (img_size[1]-fnt_size[1])/2+y
        draw.text((x1,y1),text,font=fnt,fill="#000000")
        new_image.save("./data/%s.png"%text)
    except Exception as e:
        print(e)

@app.post("/2020/produce/")
async def produce(request: Request, pngname:str=Form(...), username: str = Depends(get_current_username)):
    logger.info(pngname)
    draw_image(pngname,0,60) # 修改x,y的值调整字体的位置

    _pngname = pngname
    logger.info(_pngname)
    return templates.TemplateResponse("2020.html", {
         'request':request,
         'pngname':_pngname
    })

@app.get("/2020/download/{name}")
async def download(request: Request, pngname:str, username: str = Depends(get_current_username)):
    return FileResponse(f"./data/{pngname}.png",media_type="image/png")

def main():
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    uvicorn.run("main:app", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
