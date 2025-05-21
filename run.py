import argparse
import os
from dotenv import load_dotenv
import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run FastAPI application with Uvicorn.")
    parser.add_argument("--prod", action="store_true", help="Run in production mode")
    parser.add_argument("--test", action="store_true", help="Run in test mode")
    parser.add_argument("--dev", action="store_true", help="Run in development mode")

    args = parser.parse_args()

    if args.prod:
        load_dotenv("app/settings/.env.prod")
    elif args.test:
        load_dotenv("app/settings/.env.test")
    else:
        load_dotenv("app/settings/.env.dev")

    uvicorn.run("app.main:app", 
                port=int(os.getenv("PORT")), 
                reload=bool(os.getenv("RELOAD")),
    )