# -*- coding: utf-8 -*-
import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import BaseModel
from typing import Optional
import json


try:
    import RPi.GPIO as GPIO
    from util.controller import Controller
    TEST = False
except:
    print("module RPi.GPIO can't import")
    from util.controller import TestController as Controller
    TEST = True


class ControlRequest(BaseModel):
    movement: Optional[int] # 0: stop, 1: forward, 2: backward, 3: rotate_right, 4: rotate_left
    action: Optional[int]  # TBD


class ControlResponse(BaseModel):
    message: str


class App(FastAPI):
    def __init__(self):
        super().__init__()
        self.ctl = Controller()
        self.prepare_resources()
        return None
    
    def prepare_resources(self):
        @self.get('/')
        def index():
            return JSONResponse(content={'msg': 'ok'}, status_code=status.HTTP_200_OK)
        
        @self.post('/control', response_model=ControlResponse)
        def control(request: ControlRequest):
            try:
                if hasattr(request, "movement"):
                    mov = request.movement
                    if mov == 0:
                        self.ctl.stop()
                    elif mov == 1:
                        self.ctl.forward()
                    elif mov == 2:
                        self.ctl.backward()
                    elif mov == 3:
                        self.ctl.rotate_right()
                    elif mov == 4:
                        self.ctl.rotate_left()
                if hasattr(request, "ation"):
                    act = request.action
                    # TBD
            except Exception as e:
                print(e)
            return JSONResponse(content={'msg': 'ok'}, status_code=status.HTTP_200_OK)

        @self.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc):
            logger.error(exc.errors())
            return JSONResponse(
                content={'msg': 'Invalid request.'},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        @self.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc):
            logger.error(exc.detail)
            return JSONResponse(
                content={'msg': 'Internal server error.'},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return None


if __name__ == '__main__':
    import uvicorn
    if TEST:
        host = "0.0.0.0"
    else:
        host = "192.168.0.56"
    try:
        app=App()
        uvicorn.run(
            app=app, 
            host=host, 
            port=8000, 
#            log_config='log_config.json', 
#            access_log=False
        )
    except Exception as e:
        print(e)
    finally:
        print("close app")
        del app
