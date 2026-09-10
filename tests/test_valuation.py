import pytest
from pytest import approx
from dcf_core.valuation import (
    discount_factor,
    present_value,
    terminal_value,
    present_value_terminal_value,
    enterprise_value,
    equity_value,
    implied_share_price,
    present_value_of_ufcf
)

def test_terminal_value():
    assert terminal_value(
        final_ufcf=100,
        terminal_growth=0.03,
        wacc=0.10,
    ) == approx(1471.43)


def test_terminal_value_rejects_invalid_growth():
    with pytest.raises(ValueError):
        terminal_value(
            final_ufcf=100,
            terminal_growth=0.10,
            wacc=0.10,
        )


def test_present_value_terminal_value():
    assert present_value_terminal_value(
        terminal_value=1471.43,
        wacc=0.10,
        final_period=5,
    ) == approx(913.64, abs=0.01)

def test_discount_factor():
    assert round(discount_factor(0.10, 1), 4) == 0.9091


def test_present_value():
    assert round(present_value(100, 0.10, 1), 2) == 90.91

def test_enterprise_value():
    assert enterprise_value(
        present_values_of_ufcf=[100, 110, 120],
        present_value_of_terminal_value=1000,
    ) == 1330


def test_equity_value():
    assert equity_value(
        enterprise_value=1330,
        debt=200,
        cash=50,
    ) == 1180


def test_implied_share_price():
    assert implied_share_price(
        equity_value=1180,
        shares_outstanding=100,
    ) == 11.80


def test_implied_share_price_rejects_zero_shares():
    with pytest.raises(ValueError):
        implied_share_price(
            equity_value=1180,
            shares_outstanding=0,
        )

def test_present_value_of_ufcf():
    ufcfs = [100, 120, 130]

    pv = present_value_of_ufcf(
        ufcfs=ufcfs,
        wacc=0.10,
    )

    assert len(pv) == 3
    assert round(pv[0], 2) == 90.91
    assert round(pv[1], 2) == 99.17
    assert round(pv[2], 2) == 97.67