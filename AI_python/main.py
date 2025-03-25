from http.client import responses

# from binstar_client import STATUS_CODES
from fastapi import FastAPI, HTTPException # FastAPI 임포트 -> http에 대한 비동기 방식을 처리하는 서버
from pydantic import BaseModel # 데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링이 쉽고 강력함)
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
# 요청과 응답사이에 특정 작업 수행

# 미들웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특정 작업을 수행할 수 있음
# 예를 들어 로깅, 인증, cors처리, 압축등...
import logging

from starlette.requests import Request  # 요청에 대한 내용
from starlette.responses import Response    # 응답에 대한 내용

app = FastAPI(
    title="My API",                         # 앱의 제목
    description = "This is a sample API",   # 앱의 주석(설명)
    version="1.0.0",                         # 앱의 버전
    docs_url=None, # http://localhost:8001/docs # 보안상 None 처리로
    redoc_url=None # http://localhost:8001/redoc
) # FastAPI 객체 생성후 app 변수에 넣음

@app.get("/") # http://localhost/ 의 라우트
async def read_root():
    return {"Hello" : "World"}
# 서버 실행 -> cd AI_python -> uvicorn main:app --reload --port 8001
# 크롬 -> 주소 : http://localhost:8001/ 확인가능
# 크롬 -> 주소 : http://127.0.0.1:8001/ 확인가능


class LoggingMiddleware(BaseHTTPMiddleware): # 로그를 콘솔에 출력하는 용도
    logging.basicConfig(level=logging.INFO) # 로그 출력 추가
    async def dispatch(self, request, call_next) :
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response
app.add_middleware(LoggingMiddleware) # 모든 요청에 대해 로그를 남기는 미들웨어 클래스를 사용함

class Item(BaseModel):  # 아이템 객체 생성(BaseModel : 객체 연결 -> 상속)
    name : str                  # 상품명 : 문자열
    description : str = None    # 상품설명 : 문자열(null)
    price : float               # 가격 : 실수형
    tax : float = None          # 세금 : 실수형(null)

@app.get("/items/{item_id}")    # http://ip주소:포트/items/1
async def read_item(item_id: int, q: str = None):
    return {"item_id" : item_id, "q" : q}
    # item_id : 상품의 번호 -> 경로 매개변수
    # q : 쿼리 매개변수 (기본값 none)

@app.post("/items/")    # post메서드용 응답
async def create_item(item: Item): # BaseModel은 데이터 모델링을 쉽게 도와주고 유효성검사도 수행
    # 잘못된 데이터가 들어오면 422 오류코드를 반환
    return item