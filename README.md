# my-fastapi-server

## Installation

1. Create a virtual environment:
   ```shell
   python -m venv .venv
   ```

2. Activate the virtual environment:
- Windows (PowerShell):
   ```shell
   .\.venv\Scripts\Activate.ps1
   ```
- Windows (Command Prompt):
   ```shell
   .\.venv\Scripts\activate.bat
   ```
- Linux/Mac:
   ```shell
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create environment configuration files in the `app/settings/` directory based on your running environment:
   
   - Development environment: `.env.dev`
   - Test environment: `.env.test`
   - Production environment: `.env.prod`
   
   You can refer to the `app/settings/.env.example` file to create your configuration:
   ```shell
   # Copy the example file and modify it
   copy app\settings\.env.example app\settings\.env.dev
   ```
   
   Then edit the `.env.dev` file and set the following environment variables:
   ```
   APP_MOD=dev
   PORT=8000
   RELOAD=True
   HTTP_PROXY=http://your-proxy.com
   HTTPS_PROXY=https://your-proxy.com
   DATABASE_URL=your_database_url
   ```

5. Run the project:
   Use the `run.py` script to run the project:
   ```shell
   # Run in development mode (default)
   python run.py --dev
   
   # Run in test mode
   python run.py --test
   
   # Run in production mode
   python run.py --prod
   ```
   
   If no parameters are specified, it will run in development mode by default:
   ```shell
   python run.py
   ```

## Usage

After running successfully, your FastAPI application will provide the following endpoints:

- `GET /` - Returns a welcome message
- `GET /env` - Returns current environment configuration information
- `POST /remoteRequest` - Proxy endpoint for sending remote requests

The server will run on the port specified in your environment configuration file and will enable hot reload based on the `RELOAD` setting.

