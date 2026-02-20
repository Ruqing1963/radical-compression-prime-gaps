#!/usr/bin/env python3
"""
cramer_wronskian_scanner.py
===========================
Scan for maximal (record-breaking) prime gaps up to a given limit
and compute the Discrete Wronskian Compression ratio q_W for each.

Usage:
    python cramer_wronskian_scanner.py [--limit N]

Titan Project -- Paper XI, February 2026
Author: Ruqing Chen, GUT Geoservice Inc.
"""

import sympy
import math
import time
import argparse


def compute_radical(n):
    """Compute the radical of n (product of distinct prime factors)."""
    if n <= 1:
        return 1
    factors = sympy.factorint(n)
    rad = 1
    for p in factors.keys():
        rad *= p
    return rad


def scan_cramer_extremes(limit):
    print("=" * 85)
    print("Cramer-Wronskian Scanner: Record Prime Gaps and Compression Ratios")
    print("=" * 85)
    print(f"{'P_n':<12} | {'Gap g':<8} | {'log^2(P_n)':<12} | "
          f"{'Cramer ratio':<14} | {'q_W':<10}")
    print("-" * 85)

    last_p = 2
    max_gap = 0

    start_time = time.time()

    for p in sympy.primerange(3, limit):
        gap = p - last_p

        # Only compute Wronskian for record-breaking gaps
        if gap > max_gap:
            max_gap = gap

            log_p = math.log(last_p)
            cramer_ratio = gap / (log_p ** 2)

            # Discrete Wronskian compression
            total_log_vol = 0.0
            global_factors = set()

            for composite in range(last_p + 1, p):
                total_log_vol += math.log(composite)
                factors = sympy.factorint(composite)
                for f in factors.keys():
                    global_factors.add(f)

            total_log_rad = sum(math.log(f) for f in global_factors)
            q_w = total_log_vol / total_log_rad if total_log_rad > 0 else 1.0

            print(f"{last_p:<12} | {gap:<8} | {log_p**2:<12.2f} | "
                  f"{cramer_ratio:<14.4f} | {q_w:<10.4f}")

        last_p = p

    elapsed = time.time() - start_time
    print("=" * 85)
    print(f"Scan complete. Depth: {limit}, max gap: {max_gap}, "
          f"time: {elapsed:.1f}s")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Scan for record prime gaps and Wronskian compression."
    )
    parser.add_argument("--limit", type=int, default=10_000_000,
                        help="Upper bound for prime scan (default: 10^7)")
    args = parser.parse_args()
    scan_cramer_extremes(args.limit)
