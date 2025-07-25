from collections.abc import Callable

import pytest

from src.external.model.sql.account_merchant.model import AccountMerchant
from src.external.model.sql.membership_proposal.model import (
    MembershipReceivablesAdvanceProposal,
)
from src.external.model.sql.merchant.model import Merchant
from src.external.model.sql.proposal.model import ReceivablesAdvanceProposal


@pytest.fixture
def merchant_factory() -> Callable:
    def closure(
        external_id: str = "104512",
        name: str = "Any merchant",
        trading_name: str = "Any trading name",
        status: str = "active",
    ) -> Merchant:
        raw_data = {
            "external_id": external_id,
            "trading_name": trading_name,
            "name": name,
            "status": status,
        }

        merchant = Merchant(**raw_data)
        return merchant

    return closure


@pytest.fixture
def account_merchant_factory() -> Callable:
    def closure(
        linked: bool = True,
        account_id: str = "a6176a71-c1ad-4be5-93bc-178e604a3bc8",
        merchant_id: str = "ba7c50ad-a938-4947-8101-b3ad1b630e93",
    ) -> AccountMerchant:
        raw_data = {
            "linked": linked,
            "account_id": account_id,
            "merchant_id": merchant_id,
        }

        account_merchant = AccountMerchant(**raw_data)
        return account_merchant

    return closure


@pytest.fixture
def proposal_factory() -> Callable:
    def closure(
        merchant_id: str = "ba7c50ad-a938-4947-8101-b3ad1b630e93",
        type: str = "spot",
        status: str = "created",
        amount_requested: float = 1000.00,
        amount_gross: float = 1000.00,
        amount_net: float = 950.00,
        discount_rate: float = 5.00,
        discount_amount: float = 50.00,
        settle_date: str = "2025-10-01T00:00:00",
        expires_at: str = "2025-10-15T00:00:00",
    ) -> ReceivablesAdvanceProposal:
        raw_data = {
            "type": type,
            "status": status,
            "amount_requested": amount_requested,
            "amount_gross": amount_gross,
            "amount_net": amount_net,
            "discount_rate": discount_rate,
            "discount_amount": discount_amount,
            "settle_date": settle_date,
            "expires_at": expires_at,
            "merchant_id": merchant_id,  # Example merchant ID
        }

        proposal = ReceivablesAdvanceProposal(**raw_data)
        return proposal

    return closure


@pytest.fixture
def membership_proposal_factory() -> Callable:
    def closure(
        action: str = "created",
        membership_id: str = "a6176a71-c1ad-4be5-93bc-178e604a3bc8",
        proposal_id: str = "ba7c50ad-a938-4947-8101-b3ad1b630e93",
    ) -> MembershipReceivablesAdvanceProposal:
        raw_data = {
            "action": action,
            "membership_id": membership_id,
            "receivables_advance_proposal_id": proposal_id,
        }

        membership_proposal = MembershipReceivablesAdvanceProposal(**raw_data)
        return membership_proposal

    return closure
