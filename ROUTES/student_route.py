from bson import ObjectId
from fastapi import APIRouter
from CONFIG.db import conn
from SCHEMAS.student_entity import studentEntity, studentsEntity
from MODELS.student import Students

student = APIRouter()

@student.get('/students')
def get_all_student():
    return studentsEntity(conn.mintic.users.find())

@student.post('/students')
def create_student(estudiante:Students):
    new_student = dict(estudiante)
    id = conn.mintic.users.insert_one(new_student).inserted_id
    return f"El estudiante se ha creado {id}"

@student.get('/students/{id}')
def get_student(id:str):
    return studentEntity(conn.mintic.users.find_one({"_id":ObjectId(id)}))

@student.delete('/students/{id}')
def delete_student(id:str):
    conn.mintic.users.find_one_and_delete({"_id":ObjectId(id)})
    return "Estudiante eliminado"

@student.put('/students/{id}')
def update_student(id:str, stu:Students):
    conn.mintic.users.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(stu)})
    return studentEntity(conn.mintic.users.find_one({"_id":ObjectId(id)}))