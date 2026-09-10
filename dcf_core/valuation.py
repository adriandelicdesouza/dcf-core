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