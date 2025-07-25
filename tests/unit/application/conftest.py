from collections.abc import Callable
from datetime import UTC, datetime
from uuid import UUID

import pytest

from src.adapter.v1.header.receivables_advance_header import ReceivablesAdvanceHeader
from src.external.model.receivables_advance.base.account import (
    ReceivablesAdvanceAccount,
)
from src.external.model.receivables_advance.base.bank import (
    ReceivablesAdvanceBank,
)
from src.external.model.receivables_advance.proposal.base.amount import ProposalAmount
from src.external.model.receivables_advance.proposal.base.bank_info import (
    ProposalBankInformation,
)
from src.external.model.receivables_advance.proposal.base.discount import (
    ProposalDiscount,
)
from src.external.model.receivables_advance.proposal.base.status import ProposalStatus
from src.external.model.receivables_advance.proposal.base.type import ProposalType
from src.external.model.receivables_advance.proposal.get.response.response import (
    ReceivablesAdvanceProposalDetailResponse,
)
from src.external.model.receivables_advance.proposal.spot.submit.response.response import (
    ReceivablesAdvanceSpotResponse,
)
from src.external.model.sql.proposal.model import ReceivablesAdvanceProposal


@pytest.fixture
def spot_submit_response() -> Callable:
    def closure(status: str = "created") -> dict:
        return ReceivablesAdvanceSpotResponse(
            status=status,
        )

    return closure


@pytest.fixture
def proposal_factory(
    receivables_advance_header_dto: ReceivablesAdvanceHeader,
) -> Callable:
    def closure(
        proposal_id: UUID,
        status: str = "created",
        submitted_at: datetime | None = None,
        type: str = "spot",
        amount_requested: float = 1000.00,
        amount_gross: float = 1000.00,
        amount_net: float = 950.00,
        discount_rate: float = 5.00,
        discount_amount: float = 50.00,
        settle_date: str = str(datetime.now(UTC)),
        expires_at: str = str(datetime.now(UTC)),
    ):
        return ReceivablesAdvanceProposal(
            id=proposal_id,
            status=status,
            type=type,
            amount_requested=amount_requested,
            amount_gross=amount_gross,
            amount_net=amount_net,
            discount_rate=discount_rate,
            discount_amount=discount_amount,
            settle_date=settle_date,
            expires_at=expires_at,
            updated_at=datetime.now(UTC),
            created_at=datetime.now(UTC),
            submitted_at=submitted_at,
            merchant_id=receivables_advance_header_dto.merchant_id,
        )

    return closure


@pytest.fixture
def get_proposal_details_response() -> ReceivablesAdvanceProposalDetailResponse:
    def closure(
        id: str = "1238ecf4-d52e-4cfb-83c6-68906d0de9af",
        type: str = "spot",
        status: str = "created",
        amount_requested: float = 10000.00,
        amount_gross: float = 10000.00,
        amount_net: float = 8000.00,
        discount_rate: float = 0.2,
        discount_amount: float = 2000.00,
        settle_date: str = "2025-06-12T14:35:21.123456",
        expires_at: str = "2025-06-19T14:35:21.654321",
        updated_at: str = "2025-06-19T14:35:21.654321",
        created_at: str = "2025-06-12T14:35:21.123456",
    ) -> ReceivablesAdvanceProposalDetailResponse:
        return ReceivablesAdvanceProposalDetailResponse(
            id=UUID(id),
            type=ProposalType(type),
            status=ProposalStatus(status),
            amount=ProposalAmount(
                requested=amount_requested,
                gross=amount_gross,
                net=amount_net,
            ),
            discount=ProposalDiscount(
                rate=discount_rate,
                amount=discount_amount,
            ),
            bank_info=ProposalBankInformation(
                bank=ReceivablesAdvanceBank(
                    code="0001",
                    name="Any Bank",
                ),
                account=ReceivablesAdvanceAccount(
                    branch="0001",
                    number="123456789",
                    type="corrente",
                ),
            ),
            settle_date=datetime.fromisoformat(settle_date),
            expires_at=datetime.fromisoformat(expires_at),
            updated_at=datetime.fromisoformat(updated_at),
            created_at=datetime.fromisoformat(created_at),
        )

    return closure
