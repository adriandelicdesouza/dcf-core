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
    present_value_of_ufcf,
    present_value_of_forecast,
    calculate_dcf,
)


def test_terminal_value():
    tv = terminal_value(
        final_ufcf=140,
        terminal_growth=0.03,
        wacc=0.10,
    )

    assert round(tv, 2) == 2060.00


def test_terminal_value_rejects_invalid_growth():
    with pytest.raises(ValueError):
        terminal_value(
            final_ufcf=100,
            terminal_growth=0.10,
            wacc=0.10,
        )


def test_discount_factor():
    assert round(discount_factor(0.10, 1), 4) == 0.9091


def test_present_value():
    assert round(present_value(100, 0.10, 1), 2) == 90.91


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


def test_present_value_of_forecast():
    ufcfs = [100, 120, 130]

    pv = present_value_of_forecast(
        ufcfs=ufcfs,
        wacc=0.10,
    )

    assert round(pv, 2) == 287.75


def test_present_value_terminal_value():
    tv = 2060.00

    pv = present_value_terminal_value(
        terminal_value=tv,
        wacc=0.10,
        final_period=5,
    )

    assert round(pv, 2) == 1279.10


def test_enterprise_value():
    present_values = [90.91, 99.17, 97.67]
    pv_terminal = 1279.10

    ev = enterprise_value(
        present_values_of_ufcf=present_values,
        present_value_of_terminal_value=pv_terminal,
    )

    assert round(ev, 2) == 1566.85


def test_equity_value():
    equity = equity_value(
        enterprise_value=1566.85,
        debt=300,
        cash=100,
    )

    assert round(equity, 2) == 1366.85


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

def test_full_dcf_output():
    ufcfs = [100, 120, 130]
    wacc = 0.10

    pv_forecast = present_value_of_forecast(
        ufcfs=ufcfs,
        wacc=wacc,
    )

    tv = terminal_value(
        final_ufcf=130,
        terminal_growth=0.03,
        wacc=wacc,
    )

    pv_tv = present_value_terminal_value(
        terminal_value=tv,
        wacc=wacc,
        final_period=3,
    )

    ev = enterprise_value(
        present_values_of_ufcf=present_value_of_ufcf(ufcfs, wacc),
        present_value_of_terminal_value=pv_tv,
    )

    equity = equity_value(
        enterprise_value=ev,
        debt=200,
        cash=50,
    )

    share_price = implied_share_price(
        equity_value=equity,
        shares_outstanding=100,
    )

    assert round(pv_forecast, 2) == 287.75
    assert round(tv, 2) == 1912.86
    assert round(pv_tv, 2) == 1437.16
    assert round(ev, 2) == 1724.91
    assert round(equity, 2) == 1574.91
    assert round(share_price, 2) == 15.75

def test_calculate_dcf():
    result = calculate_dcf(
        ufcfs=[100, 120, 130],
        wacc=0.10,
        terminal_growth=0.03,
        debt=200,
        cash=50,
        shares_outstanding=100,
    )

    assert round(result["present_value_of_ufcf"], 2) == 287.75
    assert round(result["terminal_value"], 2) == 1912.86
    assert round(result["present_value_of_terminal_value"], 2) == 1437.16
    assert round(result["enterprise_value"], 2) == 1724.91
    assert round(result["equity_value"], 2) == 1574.91
    assert round(result["implied_share_price"], 2) == 15.75

