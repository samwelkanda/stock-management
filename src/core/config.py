import os

class Settings:
    PROJECT_NAME:str = "Stock Management"
    PROJECT_VERSION: str = "1.0.0"
    
    host_server: str = os.environ.get('HOST_SERVER', 'localhost')
    db_server_port: str = os.environ.get('DB_SERVER_PORT', '5432')
    database_name: str = os.environ.get('DB_NAME', 'stock')
    db_username: str = os.environ.get('DB_USERNAME', 'postgres')
    db_password: str = os.environ.get('DB_PASSWORD', 'postgres')


    DATABASE_URL = f'postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}'

settings = Settings()