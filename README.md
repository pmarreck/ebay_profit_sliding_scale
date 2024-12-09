# eBay Profit Sliding Scale Model

This project demonstrates a novel approach to eBay reselling that better aligns incentives between sellers and item owners. Instead of using a fixed commission percentage, it implements a sliding scale where the seller's cut adjusts based on the item's value.

## The Model

The model uses a logistic-like curve to determine the seller's percentage based on the item's value:
- For lower-value items, the seller receives a higher percentage to make it worth their time and effort
- For higher-value items, the percentage gradually decreases to a minimum floor
- The transition between these extremes is smooth and configurable

### Key Features

- Minimum seller percentage (floor) for high-value items
- Additional percentage for lower-value items
- Configurable inflection point where the curve begins to decline
- Adjustable curve steepness
- Visual representation through two charts:
  1. Seller's percentage vs. item value
  2. Seller's profit vs. item value

## Running the Project

This project uses Nix for dependency management. To run it:

1. Ensure you have Nix installed:
   ```bash
   # On macOS/Linux
   sh <(curl -L https://nixos.org/nix/install)
   ```

2. Clone this repository and navigate to it

3. Enter the Nix development shell:
   ```bash
   nix develop
   ```

4. Run the script:
   ```bash
   python chart.py
   ```

## Running Tests

The project includes unit tests to verify the behavior of the profit model. To run the tests:

1. Enter the Nix development shell if you haven't already:
   ```bash
   nix develop
   ```

2. Run the tests:
   ```bash
   python -m unittest test_chart.py
   ```

The tests verify:
- Minimum percentage floor is maintained for high-value items
- Maximum percentage ceiling is respected for low-value items
- Behavior around the inflection point
- Monotonic decrease of percentage as value increases

## Customizing the Model

You can adjust the model's behavior by modifying these variables in `chart.py`:

- `MIN_SELLER_PERCENTAGE`: The minimum percentage the seller gets (floor)
- `ADDITIONAL_PERCENTAGE`: Extra percentage available for lower-value items
- `PRICE_INFLECTION`: Price point where the curve starts to significantly decline
- `CURVE_STEEPNESS`: Controls how abruptly the percentage changes

### Example Configurations

For a more aggressive curve (higher percentages for low-value items):
```python
MIN_SELLER_PERCENTAGE = 0.30  # 30%
ADDITIONAL_PERCENTAGE = 0.40  # 40%
PRICE_INFLECTION = 800.0     # Curve drops earlier
CURVE_STEEPNESS = 1.3        # Steeper transition
```

For a gentler curve:
```python
MIN_SELLER_PERCENTAGE = 0.25  # 25%
ADDITIONAL_PERCENTAGE = 0.30  # 30%
PRICE_INFLECTION = 1200.0    # Curve drops later
CURVE_STEEPNESS = 0.9        # More gradual transition
```

## Business Model Benefits

This sliding scale model offers several advantages:

1. **Better Incentive Alignment**: 
   - Sellers are motivated to handle low-value items (higher percentage)
   - Item owners get a larger share of high-value items
   - Fair compensation for seller effort regardless of item value

2. **Market Efficiency**:
   - Encourages processing of items that might otherwise be ignored
   - Natural price-based optimization of effort allocation

3. **Transparency**:
   - Clear, mathematical model for all parties
   - Predictable earnings based on item value
   - No hidden fees or complicated structures

## Dependencies

The project uses these Python packages (managed via Nix):
- numpy
- matplotlib

These dependencies are automatically managed through the `flake.nix` configuration.
