from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
  return {"res":"Hello 1-1 World"}