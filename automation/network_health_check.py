
#!/usr/bin/env python3

"""
NVIDIA NetQ-Based Network Monitoring & Deployment Automation
Module: Network Health Monitor

Analyzes simulated network telemetry using monitoring thresholds.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

METRICS = {
    "temperature_celsius": "temperature_celsius",
    "link_utilization_percent": "link_utilization_percent",
    "buffer_utilization_percent": "buffer_utilization_percent",
    "packet_drop_rate_percent": "packet_drop_rate_percent"
}


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_thresholds(file_path):
    """Read the simple threshold structure from monitoring-rules.yml."""
    thresholds = {}
    current_metric = None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            metric_match = re.match(
                r"^  ([a-z_]+):\s*$", line
            )

            if metric_match:
                current_metric = metric_match.group(1)
                thresholds[current_metric] = {}

            value_match = re.match(
                r"^    (warning|critical):\s*([0-9.]+)\s*$",
                line
            )

            if value_match and current_metric:
                severity = value_match.group(1)
                value = float(value_match.group(2))
                thresholds[current_metric][severity] = value

    return thresholds


def get_status(value, limits):
    """Classify a metric according to its configured limits."""
    warning = limits.get("warning", float("inf"))
    critical = limits.get("critical", float("inf"))

    if value >= critical:
        return "CRITICAL"

    if value >= warning:
        return "WARNING"

    return "HEALTHY"


def main():
    telemetry_file = ROOT / "data" / "sample_telemetry.json"
    rules_file = ROOT / "configs" / "monitoring-rules.yml"

    telemetry = load_json(telemetry_file)
    thresholds = load_thresholds(rules_file)

    severity_rank = {
        "HEALTHY": 0,
        "WARNING": 1,
        "CRITICAL": 2
    }

    overall_status = "HEALTHY"

    print("=" * 60)
    print(" NVIDIA NETQ - NETWORK HEALTH REPORT")
    print("=" * 60)

    for device in telemetry.get("devices", []):
        print(f"\nDevice: {device.get('node', 'Unknown')}")

        for metric, threshold_key in METRICS.items():
            if metric not in device:
                print(f"  {metric}: DATA MISSING")
                continue

            value = float(device[metric])
            limits = thresholds.get(threshold_key, {})
            status = get_status(value, limits)

            print(f"  {metric}: {value:g} [{status}]")

            if severity_rank[status] > severity_rank[overall_status]:
                overall_status = status

    print("\n" + "-" * 60)
    print(f"OVERALL NETWORK STATUS: {overall_status}")
    print("=" * 60)


if __name__ == "__main__":
    main()
