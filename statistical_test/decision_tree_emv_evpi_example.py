
#!/usr/bin/env python3
# decision_tree_emv_evpi_example.py
# Small synthetic example of a decision tree with EMV and EVPI.
# Scenario:
# A company must choose a batch size (Large vs Small) under uncertain demand.
# - Demand can be High (prob p_high) or Low (prob 1 - p_high).
# - Each combination of decision + demand state has an associated profit.
# We compute:
# - EMV for each decision
# - Best decision by EMV
# - Expected value with perfect information (EV with PI)
# - Expected value of perfect information (EVPI)

from matplotlib import pyplot as plt

# Probabilities
p_high = 0.4
p_low = 1 - p_high

# Payoff table (profits)
payoffs = {
    "Large": {"High": 100, "Low": -20},
    "Small": {"High": 60, "Low": 30},
}


def emv(option: str) -> float:
    """Expected monetary value for a given decision option."""
    return (
        p_high * payoffs[option]["High"]
        + p_low * payoffs[option]["Low"]
    )


# EMVs
emv_large = emv("Large")
emv_small = emv("Small")
best_decision = "Large" if emv_large > emv_small else "Small"
best_emv = max(emv_large, emv_small)

# Expected value with perfect information:
# For each state of demand, we would choose the better option.
ev_perfect = (
    p_high * max(payoffs["Large"]["High"], payoffs["Small"]["High"])
    + p_low * max(payoffs["Large"]["Low"], payoffs["Small"]["Low"])
)
evpi = ev_perfect - best_emv


def print_summary() -> None:
    print("=== Decision Tree EMV / EVPI Example ===")
    print(f"p(High demand) = {p_high:.2f}, p(Low demand) = {p_low:.2f}\n")

    print("Payoff table (profit):")
    for opt in payoffs:
        print(
            f"  {opt:>5}  |  High: {payoffs[opt]['High']:>4}  "
            f"Low: {payoffs[opt]['Low']:>4}"
        )

    print("\nExpected Monetary Values (EMV):")
    print(f"  EMV(Large) = {emv_large:.2f}")
    print(f"  EMV(Small) = {emv_small:.2f}")
    print(f"\n→ Optimal decision by EMV: {best_decision} (EMV = {best_emv:.2f})")

    print("\nPerfect information:")
    print(f"  EV with perfect information = {ev_perfect:.2f}")
    print(f"  EVPI = {evpi:.2f}")


def plot_tree(output_path: str = "emv_evpi_decision_tree.png") -> None:
    """Draw a simple decision tree diagram with EMVs and EVPI."""

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")

    # Node positions
    root = (0.1, 0.5)
    large = (0.4, 0.75)
    small = (0.4, 0.25)

    large_high = (0.8, 0.95)
    large_low = (0.8, 0.55)
    small_high = (0.8, 0.35)
    small_low = (0.8, 0.05)

    def connect(a, b):
        ax.plot([a[0], b[0]], [a[1], b[1]])

    # Root node (decision)
    ax.text(
        root[0],
        root[1],
        "Decision:\nBatch size",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round", alpha=0.2),
    )

    # Decision branches
    connect(root, large)
    connect(root, small)
    ax.text((root[0] + large[0]) / 2, (root[1] + large[1]) / 2 + 0.03, "Large", ha="center")
    ax.text((root[0] + small[0]) / 2, (root[1] + small[1]) / 2 - 0.03, "Small", ha="center")

    # Chance nodes
    ax.text(
        large[0],
        large[1],
        "Demand\n(H/L)",
        ha="center",
        va="center",
        bbox=dict(boxstyle="circle", alpha=0.2),
    )
    ax.text(
        small[0],
        small[1],
        "Demand\n(H/L)",
        ha="center",
        va="center",
        bbox=dict(boxstyle="circle", alpha=0.2),
    )

    # Large → outcomes
    connect(large, large_high)
    connect(large, large_low)
    ax.text(
        (large[0] + large_high[0]) / 2,
        (large[1] + large_high[1]) / 2 + 0.03,
        f"High ({p_high:.1f})",
        ha="center",
    )
    ax.text(
        (large[0] + large_low[0]) / 2,
        (large[1] + large_low[1]) / 2 - 0.03,
        f"Low ({p_low:.1f})",
        ha="center",
    )

    # Small → outcomes
    connect(small, small_high)
    connect(small, small_low)
    ax.text(
        (small[0] + small_high[0]) / 2,
        (small[1] + small_high[1]) / 2 + 0.03,
        f"High ({p_high:.1f})",
        ha="center",
    )
    ax.text(
        (small[0] + small_low[0]) / 2,
        (small[1] + small_low[1]) / 2 - 0.03,
        f"Low ({p_low:.1f})",
        ha="center",
    )

    # Outcome payoffs
    ax.text(large_high[0], large_high[1], "Profit = 100", ha="center", va="center")
    ax.text(large_low[0], large_low[1], "Profit = -20", ha="center", va="center")
    ax.text(small_high[0], small_high[1], "Profit = 60", ha="center", va="center")
    ax.text(small_low[0], small_low[1], "Profit = 30", ha="center", va="center")

    # EMV + EVPI summary
    ax.text(
        0.5,
        0.02,
        (
            f"EMV(Large) = {emv_large:.1f}, EMV(Small) = {emv_small:.1f} → choose {best_decision}\n"
            f"EV with perfect info = {ev_perfect:.1f}, EVPI = {evpi:.1f}"
        ),
        ha="center",
        va="bottom",
    )

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    print(f"Saved decision tree diagram to {output_path}")


if __name__ == "__main__":
    print_summary()
    plot_tree()