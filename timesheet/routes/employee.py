from flask import Blueprint, render_template, request

employee = Blueprint("employee", __name__, template_folder="templates")

@employee.route("/", methods=["GET"])
def dashboard():
    if request.method == "GET":
        return render_template("index.html")

@employee.route("/login", methods=["POST"])
def login():
    if request.method=="POST":
        print("Logging In")

