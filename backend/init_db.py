from backend.database import engine
from backend.models.audit_log import AuditLog
from backend.database import Base


def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")


if __name__ == "__main__":
    initialize_database()