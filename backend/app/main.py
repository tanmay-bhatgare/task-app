from fastapi import FastAPI, status
from .db.database import engine
from .models import taskModel, userModel
from .routes import taskRoutes, authRoutes, userRoutes

taskModel.Base.metadata.create_all(bind=engine)
userModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(taskRoutes.router)
app.include_router(authRoutes.router)
app.include_router(userRoutes.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Root"}
