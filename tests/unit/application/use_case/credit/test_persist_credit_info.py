from src.application.use_cases.credit.persist_credit_info import (
    PersistCreditInfoUseCase,
)


def test_convert_entities_to_models(list_credit_limit_business_entities):
    models = PersistCreditInfoUseCase().convert_to_database_model(
        list_credit_limit_business_entities
    )
    assert len(models) == 5
    assert all(
        [
            models[i].document == list_credit_limit_business_entities[i].document
            for i in range(5)
        ]
    )
    assert all(
        [models[i].qia == list_credit_limit_business_entities[i].qia for i in range(5)]
    )
    assert all(
        [models[i].cgr == list_credit_limit_business_entities[i].cgr for i in range(5)]
    )
