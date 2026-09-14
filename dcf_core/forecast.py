def project_revenue(previous_revenue: float, growth_rate: float) -> float:
    return previous_revenue * (1 + growth_rate)


def calculate_ebit(revenue: float, ebit_margin: float) -> float:
    return revenue * ebit_margin


def calculate_taxes(ebit: float, tax_rate: float) -> float:
    return ebit * tax_rate


def calculate_nopat(ebit: float, tax_rate: float) -> float:
    return ebit * (1 - tax_rate)


def calculate_d_and_a(revenue: float, d_and_a_percent: float) -> float:
    return revenue * d_and_a_percent


def calculate_capex(revenue: float, capex_percent: float) -> float:
    return revenue * capex_percent


def calculate_nwc(revenue: float, nwc_percent: float) -> float:
    return revenue * nwc_percent


def calculate_change_in_nwc(
    current_nwc: float,
    previous_nwc: float,
) -> float:
    return current_nwc - previous_nwc


def calculate_ufcf(
    nopat: float,
    d_and_a: float,
    capex: float,
    change_in_nwc: float,
) -> float:
    return nopat + d_and_a - capex - change_in_nwc

def forecast_ufcf(
    starting_revenue: float,
    growth_rates: list[float],
    ebit_margins: list[float],
    tax_rates: list[float],
    d_and_a_percents: list[float],
    capex_percents: list[float],
    nwc_percents: list[float],
) -> list[float]:
    if not (
        len(growth_rates)
        == len(ebit_margins)
        == len(tax_rates)
        == len(d_and_a_percents)
        == len(capex_percents)
        == len(nwc_percents)
    ):
        raise ValueError("All forecast assumptions must have the same length.")

    ufcfs = []
    previous_revenue = starting_revenue
    previous_nwc = 0.0

    for year in range(len(growth_rates)):
        revenue = project_revenue(
            previous_revenue,
            growth_rates[year],
        )

        ebit = calculate_ebit(
            revenue,
            ebit_margins[year],
        )

        nopat = calculate_nopat(
            ebit,
            tax_rates[year],
        )

        d_and_a = calculate_d_and_a(
            revenue,
            d_and_a_percents[year],
        )

        capex = calculate_capex(
            revenue,
            capex_percents[year],
        )

        current_nwc = calculate_nwc(
            revenue,
            nwc_percents[year],
        )

        change_in_nwc = calculate_change_in_nwc(
            current_nwc,
            previous_nwc,
        )

        ufcf = calculate_ufcf(
            nopat,
            d_and_a,
            capex,
            change_in_nwc,
        )

        ufcfs.append(ufcf)

        previous_revenue = revenue
        previous_nwc = current_nwc

    return ufcfs