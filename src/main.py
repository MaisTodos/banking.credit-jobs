from pathlib import Path

from typer import Typer, run

from src.adapters.controllers.credit.business_credit import BusinessCreditController
from src.external.infrastructure.container import init_ioc_container
from src.external.infrastructure.i18n import init_i18n_translator
from src.external.infrastructure.logger import init_json_logger
from src.external.setting.environment import env

path = Path(__file__).parent
PATH_TRANSLATOR = Path(path) / "external" / "translator"

init_ioc_container()
init_i18n_translator(path_translator=PATH_TRANSLATOR)
init_json_logger(log_level=env.LOG_LEVEL.value)
app = Typer()


@app.command()
def run_update_business_credit_limits():
    business_credit_controller = BusinessCreditController()
    business_credit_controller.update_credit_info()


if __name__ == "__main__":
    run(app())
