import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Roles(enum.Enum):
    EMPLOYEE = 1
    MANAGER = 2

class Employee(db.Model):
    __tablename__="employee"

    employeeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unqique=True)
    password = db.Column(db.String(100), nullable=False)
    createdOn = db.Column(db.DateTime(timezone=True), server_default=func.now())
    roleId = db.Column(db.Enum(Roles))
    address = db.Column(db.String(50), nullable=False)
    panNumber = db.Column(db,String(50), nullable=False)
    managerId = db.Column(db.Integer, ForeignKey("employees.employeeId"))
