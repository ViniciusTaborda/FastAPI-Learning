from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World!"


@app.get("/property")
def property():
    return "This is a property page."


@app.get("/movies")
def movies():
    return {"movie_list": ["movie1", "movie2"]}
