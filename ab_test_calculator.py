import math

def sample_size_proportions(baseline_ctr=0.10, mde=0.02, alpha=0.05, power=0.8):
    """
    Approximate sample size per variant for a two-proportion Z-test.

    baseline_ctr: baseline conversion rate (e.g., 0.10)
    mde: minimum detectable effect (absolute delta, e.g., 0.02)
    alpha: false positive rate
    power: 1 - false negative rate
    """
    from scipy.stats import norm
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)

    p1 = baseline_ctr
    p2 = baseline_ctr + mde
    p_bar = (p1 + p2) / 2.0

    sd1 = math.sqrt(2 * p_bar * (1 - p_bar))
    sd2 = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    n = ((z_alpha * sd1 + z_beta * sd2) ** 2) / (mde ** 2)
    return math.ceil(n)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="A/B Test Sample Size Calculator (proportions)")
    parser.add_argument("--baseline_ctr", type=float, default=0.10, help="Baseline conversion rate, e.g., 0.10")
    parser.add_argument("--mde", type=float, default=0.02, help="Minimum detectable effect (absolute), e.g., 0.02")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level")
    parser.add_argument("--power", type=float, default=0.8, help="Statistical power")
    args = parser.parse_args()

    n = sample_size_proportions(
        baseline_ctr=args.baseline_ctr,
        mde=args.mde,
        alpha=args.alpha,
        power=args.power
    )
    print(f"Required sample size per variant: {n}")
