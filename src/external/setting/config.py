from pathlib import Path

from src.external.setting.environment import env

path = Path(__file__).parent
CERT_PATH = Path(path) / "postgres.pem"
ECHO = env.ENV == "local"
SSL_MODE = "allow" if env.ENV == "local" else "verify-ca"
