from src.api import Server
import os
import dotenv

def main():
    dotenv.load_dotenv()

    host = 'localhost'
    port = int(os.getenv('BACKEND_PORT', 5000))

    server = Server(
        host=host,
        port=port
    )
    server.run()

if __name__ == '__main__':
    main()