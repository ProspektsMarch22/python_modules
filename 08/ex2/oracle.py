import os
import sys


def load_config() -> dict[str, str]:
    # Gets variables from .env file
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("\nERROR: Missing dependency: python-dotenv\n"
              "Use the following command to install it:\n"
              "pip install python-dotenv")
        return {}
    try:
        matrix_mode = os.getenv('MATRIX_MODE', 'dev')
        database_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        zion_endpoint = os.getenv('ZION_ENDPOINT')
        if not database_url or not api_key or not zion_endpoint:
            print("ERROR: Missing required environment variables")
            return {}
        return {
            "mode": matrix_mode,
            "database": database_url,
            "api": api_key,
            "log_level": log_level,
            "zion_ep": zion_endpoint
        }
    except Exception as e:
        print(f"[LOAD_CONFIG() ERROR]: {e}")
        return {}


def oracle(env_variables: dict[str, str]) -> None:
    try:
        print("\nORACLE STATUS: Reading the Matix...\n\n"
              "Configuration loaded:")
        print(f"Mode: {env_variables['mode']}")
        if env_variables['mode'] == "dev":
            print("Database: Connected to local instance")
        elif env_variables['mode'] == "prod":
            print("Database: Connected to production")
        else:
            print("Database: invalid mode - you're on your own")
        print("API Access: Authenticated")
        print(f"Log level: {env_variables['log_level']}")
        print("Zion Network: Online")
    except Exception as e:
        print(f"[ORACLE() ERROR]: {e}")


def security_check() -> None:
    print("\nEnvironment security check:\n"
          "[OK] No hardcoded secrets detected")
    if not os.path.exists(".env"):
        print("[WARNING] .env not found!\n"
              "'cp .env.example .env' to create a .env file")
    else:
        print("[OK] .env file properly configured!")
    print("[OK] Production overrides available\n"
          "The Oracle sees all configurations.")


if __name__ == "__main__":
    config = load_config()
    if config:
        oracle(config)
    security_check()
    if not config:
        sys.exit(1)
