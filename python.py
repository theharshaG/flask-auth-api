from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'secret123'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Auth API Running"


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"})
      
    hashed_password = generate_password_hash(data['password'])

    user = User(
        username=data['username'],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

# LOGIN API
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Find user
    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return jsonify({"error": "User not found"})

    # Check password
    if check_password_hash(user.password, data['password']):
        
        # Create JWT token
        token = create_access_token(identity=user.username)

        return jsonify({"message": "Login successful", "token": token})

    return jsonify({"error": "Invalid password"})


# PROTECTED ROUTE
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()

    return jsonify({
        "message": f"Welcome {current_user}",
        "status": "Access granted"
    })

if __name__ == '__main__':
    app.run(debug=True)
