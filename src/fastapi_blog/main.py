from fastapi_blog import snippets
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{snippets.posts[0]["title"]}</h1>"

@app.get("/api/post")
def get_post():
    return snippets.posts