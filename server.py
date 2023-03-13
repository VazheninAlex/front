from fastapi import FastAPI
from pydantic import BaseModel
from random import randint

class Sensor(BaseModel):
    name: str
    value: int
    normalValue: int
    minValue: int
    maxValue: int
    colour: int



app = FastAPI()

@app.get('/sensor')
def info():
    pH = Sensor(name = 'pH', value = randint(1, 14), normalValue = 7, minValue = 0, maxValue = 14, colour = 0)
    sen2 = Sensor(name = 'sensor2', value = randint(1, 100), normalValue = 50, minValue = 0, maxValue = 100, colour = 0)
    sen3 = Sensor(name = 'sensor3', value = randint(1, 100), normalValue = 50, minValue = 0, maxValue = 100, colour = 0)
    pH.colour = abs((pH.normalValue - pH.value) / (pH.maxValue - pH.minValue))
    sen2.colour = abs((sen2.normalValue - sen2.value) / (sen2.maxValue - sen2.minValue))
    sen3.colour = abs((sen3.normalValue - sen3.value) / (sen3.maxValue - sen3.minValue))
    return [pH, sen2, sen3]