from fastapi import Form
from typing import Annotated

def get(txt: str):
  return {"result": txt}

def post(txt: Annotated[str, Form(...)]):
  return {"result": txt}


study03 = {
  "prefix":"/s3", 
  "tags":["CRUD 연습"],
  "urls" : [
    {
      "methods":["GET"], 
      "path":"/",
      "endpoint": get,
    },
    {
      "methods":["POST"], 
      "path":"/",
      "endpoint": post,
    }
  ]
}
