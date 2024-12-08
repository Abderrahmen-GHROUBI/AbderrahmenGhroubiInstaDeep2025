from app.Database import engine,Base

try:
    Base.metadata.create_all(bind=engine)
    print(f"Suc ")
except Exception as e:
    print(f"error creating in database:{e}")