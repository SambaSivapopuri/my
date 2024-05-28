from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from Views.user import app as user
app = FastAPI(
    title='PPA API',
	docs_url='/ppa/docs',
	openapi_url='/ppa/openapi.json'
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True,
)
app.include_router(user)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
