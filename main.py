from src.api import Server
import os
import dotenv

def main():
    dotenv.load_dotenv()

    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('BACKEND_PORT', 5000))

    Server.init(host, port)
    Server.run()

if __name__ == '__main__':
    main()