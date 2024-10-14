from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/hello-world/")                                     #A
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}