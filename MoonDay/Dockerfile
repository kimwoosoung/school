# Python 3.10 이미지를 기반으로 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사
COPY requirements.txt /app/

# dependencies 설치
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 애플리케이션 파일 복사
COPY . /app/

# 8000번 포트 열기
EXPOSE 8000

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]