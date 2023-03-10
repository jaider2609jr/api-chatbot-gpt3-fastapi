from fastapi import FastAPI
from schemas import prompt_schema, res_schema
from controllers.openaiController import response_prompt

#en el archivo de openaiConroller de la carpeta controllers configura tu apikey para pueda funcionar a api

app = FastAPI()

@app.get("/")
async def index():
    return {"mensaje": "Bienvenido a PyGpt por JaiderBy10"}

@app.post("/prompt", response_model=res_schema.resSchema)
async def create(prompt:prompt_schema.PromptSchema):
    return response_prompt(prompt.prompt)