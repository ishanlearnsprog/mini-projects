import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Roles(enum.Enum):
    EMPLOYEE = 1
    MANAGER = 2

class Status(enum.Enum):
    IN_PROCESS = 1,
    APPROVED = 2,
    REJECTED = 3

class Employee(db.Model):
    __tablename__="employees"

    employeeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    createdOn = db.Column(db.DateTime(timezone=True), server_default=func.now())
    role = db.Column(db.Enum(Roles))
    address = db.Column(db.String(50), nullable=False)
    panNumber = db.Column(db.String(50), nullable=False)
    managerId = db.Column(db.Integer, db.ForeignKey("employees.employeeId"))
    manager = db.relationship("Employee", back_populates="employee", remote_side=[employeeId])
    employee = db.relationship("Employee", back_populates="manager")

    def __repr__(self):
        return "Employee Details: Name: {} | Id: {} | Email: {} | Role: {}".format(self.name, self.employeeId, self.email, self.role)
