from dcf_core.forecast import forecast_ufcf
from dcf_core.valuation import calculate_dcf

def main() -> None:
    print("DCF Valuation")
    print("=============")

    starting_revenue = float(input("Starting revenue ($M): "))

    print(f"Starting revenue: ${starting_revenue:.2f}M")

    growth_rates = []
    ebit_margins = []
    tax_rates = []
    d_and_a_percents = []
    capex_percents = []
    nwc_percents = []

    for year in range(1, 6):
        print(f"\nYear {year}")
        print("-------")

        growth_rates.append(
            float(input("Revenue growth (%): ")) / 100
        )

        ebit_margins.append(
            float(input("EBIT margin (%): ")) / 100
        )

        tax_rates.append(
            float(input("Tax rate (%): ")) / 100
        )

        d_and_a_percents.append(
            float(input("D&A as % of revenue (%): ")) / 100
        )

        capex_percents.append(
            float(input("CapEx as % of revenue (%): ")) / 100
        )

        nwc_percents.append(
            float(input("Change in NWC as % of revenue (%): ")) / 100
        )

    ufcfs = forecast_ufcf(
        starting_revenue=starting_revenue,
        growth_rates=growth_rates,
        ebit_margins=ebit_margins,
        tax_rates=tax_rates,
        d_and_a_percents=d_and_a_percents,
        capex_percents=capex_percents,
        nwc_percents=nwc_percents,
    )

    print("\nForecast UFCF")
    print("=============")

    for year, ufcf in enumerate(ufcfs, start=1):
        print(f"Year {year}: ${ufcf:.2f}M")

    wacc = float(input("WACC (%): ")) / 100

    print(f"WACC: {wacc}")

    terminal_growth = float(input("Terminal growth (%): ")) / 100

    print(f"Terminal growth: {terminal_growth}")

    debt = float(input("Debt ($M): "))
    print(f"Debt: ${debt:.2f}M")

    cash = float(input("Cash ($M): "))
    print(f"Cash: ${cash:.2f}M")

    shares_outstanding = float(input("Shares outstanding (M): "))
    print(f"Shares outstanding: {shares_outstanding:.2f}M")

    result = calculate_dcf(
        ufcfs=ufcfs,
        wacc=wacc,
        terminal_growth=terminal_growth,
        debt=debt,
        cash=cash,
        shares_outstanding=shares_outstanding,
    )

    print("\nDCF Valuation")
    print("=============")

    print(f"PV of UFCF: ${result['present_value_of_ufcf']:.2f}M")
    print(f"Terminal Value: ${result['terminal_value']:.2f}M")
    print(f"PV of Terminal Value: ${result['present_value_of_terminal_value']:.2f}M")
    print(f"Enterprise Value: ${result['enterprise_value']:.2f}M")
    print(f"Equity Value: ${result['equity_value']:.2f}M")
    print(f"Implied Share Price: ${result['implied_share_price']:.2f}")

if __name__ == "__main__":
    main()