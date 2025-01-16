import uvicorn

if __name__ == "__main__":
    uvicorn.run("lajeh_api.main:app", reload=True)