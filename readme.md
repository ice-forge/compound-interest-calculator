# Compound Interest Calculator

A Python script that calculates compound interest with options for monthly deposits, dividend reinvestment, and goal-based projections.

## Features

- Calculate compound interest with or without monthly deposits
- Support for dividend yield calculations
- Option to reinvest dividends
- Goal-based time estimation
- Detailed financial projections output

## Configuration

The script uses the following constants that can be modified:

```python
PRINCIPAL = 1000000              # Initial investment
MONTHLY_MONEY_DEPOSIT = 0        # Monthly contribution
RATE_OF_RETURN = 0.25           # Annual rate of return (25%)
YEARS_SPENT_COMPOUNDING = 10     # Investment timeframe
DIVIDEND_YIELD = 0.00316        # Annual dividend yield (0.316%)
REINVEST_DIVIDENDS = True       # Toggle dividend reinvestment
GOAL = 8640800                  # Target amount
```

## Output

The script provides:
- Predicted investment outcome
- Annual dividend payouts
- Goal comparison
- Estimated time to reach goal (if applicable)

## Example Output

```
Predicted Outcome:                  $9,611,744.06
Annual Dividend Payouts:            $30,277.43
-------------------------------------------------
Goal:                               $8,640,800.00
Overbalance:                        $970,944.06
```

## Functions

- `calculate_compound_interest`: Basic compound interest calculation
- `reinvest_dividends`: Handles compound interest with dividend reinvestment
- `estimate_time_to_reach_goal`: Projects years needed to reach financial goal

## Usage
To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ice-forge/compound-interest-calculator.git
    ```
    Run the application:
    ```bash
    python app.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
