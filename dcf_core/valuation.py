def discount_factor(wacc: float, period: int) -> float:
    return 1 / (1 + wacc) ** period


def present_value(cash_flow: float, wacc: float, period: int) -> float:
    return cash_flow * discount_factor(wacc, period)

def terminal_value(
    final_ufcf: float,
    terminal_growth: float,
    wacc: float,
) -> float:
    if wacc <= terminal_growth:
        raise ValueError("WACC must be greater than terminal growth.")

    next_year_ufcf = final_ufcf * (1 + terminal_growth)
    return next_year_ufcf / (wacc - terminal_growth)


def present_value_terminal_value(
    terminal_value: float,
    wacc: float,
    final_period: int,
) -> float:
    return terminal_value * discount_factor(wacc, final_period)

def enterprise_value(
    present_values_of_ufcf: list[float],
    present_value_of_terminal_value: float,
) -> float:
    return sum(present_values_of_ufcf) + present_value_of_terminal_value


def equity_value(
    enterprise_value: float,
    debt: float,
    cash: float,
) -> float:
    return enterprise_value - debt + cash


def implied_share_price(
    equity_value: float,
    shares_outstanding: float,
) -> float:
    if shares_outstanding <= 0:
        raise ValueError("Shares outstanding must be greater than zero.")

    return equity_value / shares_outstanding

def present_value_of_ufcf(
    ufcfs: list[float],
    wacc: float,
) -> list[float]:
    return [
        present_value(ufcf, wacc, period)
        for period, ufcf in enumerate(ufcfs, start=1)
    ]

def present_value_of_forecast(
    ufcfs: list[float],
    wacc: float,
) -> float:
    return sum(present_value_of_ufcf(ufcfs, wacc))

def calculate_dcf(
    ufcfs: list[float],
    wacc: float,
    terminal_growth: float,
    debt: float,
    cash: float,
    shares_outstanding: float,
) -> dict:
    present_values_of_ufcf = present_value_of_ufcf(
        ufcfs=ufcfs,
        wacc=wacc,
    )

    terminal_value_amount = terminal_value(
        final_ufcf=ufcfs[-1],
        terminal_growth=terminal_growth,
        wacc=wacc,
    )

    present_value_of_terminal = present_value_terminal_value(
        terminal_value=terminal_value_amount,
        wacc=wacc,
        final_period=len(ufcfs),
    )

    ev = enterprise_value(
        present_values_of_ufcf=present_values_of_ufcf,
        present_value_of_terminal_value=present_value_of_terminal,
    )

    equity = equity_value(
        enterprise_value=ev,
        debt=debt,
        cash=cash,
    )

    share_price = implied_share_price(
        equity_value=equity,
        shares_outstanding=shares_outstanding,
    )

    return {
        "present_value_of_ufcf": sum(present_values_of_ufcf),
        "terminal_value": terminal_value_amount,
        "present_value_of_terminal_value": present_value_of_terminal,
        "enterprise_value": ev,
        "equity_value": equity,
        "implied_share_price": share_price,
    }