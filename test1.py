from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/read_data")
def test_root():
    return {"Hello": "World"}


@app.post("/insertData")
def insert_rec(name: str):
    return{"Name": name}


if __name__ == "__main__":
    uvicorn.run(app)
