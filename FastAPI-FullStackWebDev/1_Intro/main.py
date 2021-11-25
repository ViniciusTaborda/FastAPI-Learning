from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World!"


# id is a path parameter
@app.get("/property/{id}")
def property(id: int):
    return f"This is a property page for property {id}"


# fastapi uses type notation to validate parameter types
@app.get("/profile/{username}")
def profile(username: str):
    return f"This is a profile page for user: {username}"


@app.get("/movies")
def movies():
    return {"movie_list": ["movie1", "movie2"]}
