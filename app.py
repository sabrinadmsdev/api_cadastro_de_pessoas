#camada principal que vai rodar a aplicação.
from fastapi import FastAPI #framework web para construção de APIs
import uvicorn
from router import route

app = FastAPI()
app.include_router(router= route) #método para inclusão de rota FastAPI

#rota GET para checar se a aplicação está funcionando.
@app.get("/")
def health_check():
    return {"response": "a aplicação está funcionando."}


#script para rodar a aplicação
if __name__ == "__main__":
    uvicorn.run("app:app", port=8000)