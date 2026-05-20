from backend.database import SessionLocal
from backend.models.user import User
from backend.services.security import hash_password


def create_admin_user():
    db = SessionLocal()

    try:
        email = "admin@example.com"
        password = "Admin123!"

        # check if admin already exists
        existing = db.query(User).filter(User.email == email).first()

        if existing:
            print("Admin already exists.")
            return

        admin_user = User(
            email=email,
            hashed_password=hash_password(password),
            is_admin=True
        )

        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)

        print("Admin user created successfully")
        print(f"Email: {email}")
        print(f"Password: {password}")

    finally:
        db.close()


if __name__ == "__main__":
    create_admin_user()