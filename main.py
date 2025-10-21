from src.api import Server
from src.database.connection import create_database
import os
import dotenv

def main():
    dotenv.load_dotenv()

    # Cria as tabelas no banco de dados (se não existirem)
    create_database()

    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('BACKEND_PORT', 5000))

    Server.init(host, port)
    Server.run()

if __name__ == '__main__':
    main()