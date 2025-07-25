from witch_doctor import WitchDoctor

from src.external.infrastructure.container.default import ContainerDefault


def init_ioc_container():
    ContainerDefault.create_ioc_container()
    WitchDoctor.load_container("prod")
