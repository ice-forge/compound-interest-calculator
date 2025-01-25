PRINCIPAL = 1000000  # current holdings
MONTHLY_MONEY_DEPOSIT = 0  # deposit
RATE_OF_RETURN = 0.25  # yearly rate of return
YEARS_SPENT_COMPOUNDING = 10  # years invested

DIVIDEND_YIELD = 0.00316 # annual dividend yield
REINVEST_DIVIDENDS = True  # option to reinvest dividends anually

GOAL = 8640800

def calculate_compound_interest(principal, money_deposit, rate_of_return, year_span):
    total_periods = 12 * year_span # 12 = months in a year
    interest_rate_per_period = (1 + rate_of_return)**(1/12) - 1 # 12 = months in a year

    future_value = principal * (1 + (interest_rate_per_period)) ** total_periods
    future_value += money_deposit * (((1 + interest_rate_per_period) ** total_periods - 1) / interest_rate_per_period)

    return future_value

def reinvest_dividends(principal, money_deposit, rate_of_return, year_span, dividend_yield):
    total_years = int(year_span)
    remaining_months = round((year_span - total_years) * 12)
    final_year_dividend = 0
    monthly_interest = (1 + rate_of_return)**(1/12) - 1

    for year in range(total_years):
        for m in range(12):
            principal += money_deposit
            principal += principal * monthly_interest
        annual_dividend = principal * dividend_yield
        principal += annual_dividend
        final_year_dividend = annual_dividend

    interest_rate_per_period = (1 + rate_of_return)**(1/12) - 1
    for month in range(remaining_months):
        principal += money_deposit
        principal *= (1 + interest_rate_per_period)
        monthly_dividend = principal * dividend_yield / 12
        principal += monthly_dividend
        final_year_dividend += monthly_dividend

    return principal, final_year_dividend

def estimate_time_to_reach_goal(principal, money_deposit, rate_of_return, goal, dividend_yield=0, parameter_reinvest_dividends=False):
    years = 0

    while principal < goal:
        if parameter_reinvest_dividends:
            principal, _ = reinvest_dividends(principal, money_deposit, rate_of_return, 1, dividend_yield)
        else:
            principal = calculate_compound_interest(principal, money_deposit, rate_of_return, 1)
        years += 1
    return years

future_value, total_dividends = reinvest_dividends(PRINCIPAL, MONTHLY_MONEY_DEPOSIT, RATE_OF_RETURN, YEARS_SPENT_COMPOUNDING, DIVIDEND_YIELD)

if not REINVEST_DIVIDENDS:
    future_value = calculate_compound_interest(PRINCIPAL, MONTHLY_MONEY_DEPOSIT, RATE_OF_RETURN, YEARS_SPENT_COMPOUNDING)

estimated_time = estimate_time_to_reach_goal(future_value, MONTHLY_MONEY_DEPOSIT, RATE_OF_RETURN, GOAL, DIVIDEND_YIELD, REINVEST_DIVIDENDS)

string_future_value = f"${future_value:,.2f}"
string_total_dividends = f"${total_dividends:,.2f}"
string_total = f"${(future_value + total_dividends):,.2f}"

string_goal = f"${GOAL:,.2f}"
string_estimated_time = "" if estimated_time <= 0 else f"~ {estimated_time} Years"

# Define a width for alignment
width = 35

print(f"\n{'Predicted Outcome:':<{width}}" + string_future_value)
print(f"{'Annual Dividend Payouts:':<{width}}" + string_total_dividends)

print("-" * (width + len(string_total)))

print(f"{'Goal:':<{width}}" + string_goal)

if estimated_time <= 0:
    print (f"{'Overbalance:':<{width}}" + f"${future_value - GOAL:,.2f}\n")
else:
    print(f"{'Estimated Time:':<{width}}" + string_estimated_time)
