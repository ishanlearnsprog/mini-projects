from flask import Blueprint, render_template, request, flash, url_for, redirect, make_response
from flask_jwt_extended import set_access_cookies, create_access_token, jwt_required, unset_jwt_cookies, get_jwt_identity
from flask_bcrypt import Bcrypt
from models import db, Employee

employee = Blueprint("employee", __name__, template_folder="templates")
pwdBcrypt = Bcrypt()

@employee.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

# for testing and initializing db
@employee.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        if request.json:
            req = request.json
            pwdHash = pwdBcrypt.generate_password_hash(req["password"], 12)
            employee = Employee(
                name=req["name"],
                email=req["email"],
                password=pwdHash,
                role=req["role"],
                address=req["address"],
                panNumber=req["panNumber"],
                managerId=req["managerId"])
            db.session.add(employee)
            db.session.commit()
            return "Employee Created"

@employee.route("/login", methods=["POST"])
def login():
    error = "An Error Occurred" 
    if request.method == "POST":
        if request.form:
            form = request.form
            emp = Employee.query.filter(Employee.email == form["email"]).first()
            if emp:
                if pwdBcrypt.check_password_hash(emp.password, form["password"]): 
                    access_token = create_access_token(identity=emp.employeeId)
                    res = make_response(redirect(url_for("employee.profile")))
                    set_access_cookies(res, access_token)
                    return res
            error = "Invalid Credentials" 
    render_template("index.html", error=error)

@employee.route("/profile", methods=["GET", "POST"])
@jwt_required()
def profile():
    error = "An Error Occurred"
    if request.method == "GET":
        employeeId = get_jwt_identity()
        print(employeeId)
        return render_template("profile.html")

@employee.route("/logout", methods=["GET"])
@jwt_required()
def logout():
    res = redirect(url_for("employee.index"))
    unset_jwt_cookies(res)
    return res
