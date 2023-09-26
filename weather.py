from fastapi import FastAPI
from faker import Faker
import random

app = FastAPI()

fake = Faker()
Faker.seed(0)

@app.get("/temperature/{city}")
async def get_fake_temperature(city: str):
    temperature = round(random.uniform(10, 35), 2)

    fake_data = {
        "city": city,
        "temperature": temperature,
        "unit": "Celsius",
    }

    return fake_data