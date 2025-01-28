from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Get_Main_Page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def Get_Admin_Page() -> str:
    return "Вы вошли как администратор"

@app.get("/users/{user_id}")
async def Get_User_id(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def Get_User_Info(username: str = 'Olga', age: int= 23) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
