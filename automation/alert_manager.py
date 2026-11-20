
#!/usr/bin/env python3

"""
NVIDIA NetQ-Based Network Monitoring & Deployment Automation
Module: Network Alert Manager

Reads simulated network alerts and generates an alert report.
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_alerts(file_path):
    """Load active alerts from the JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("alerts", [])
    except FileNotFoundError:
        print("[ERROR] Alert data file not found.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print("[ERROR] Invalid alert JSON.")
        raise SystemExit(1)


def generate_summary(alerts):
    """Generate alert counts by severity."""
    counts = Counter(
        alert.get("severity", "unknown").lower()
        for alert in alerts
    )

    return counts


def display_alerts(alerts, counts):
    """Display alert summary and suggested actions."""
    print("=" * 70)
    print(" NVIDIA NETQ - NETWORK ALERT MANAGEMENT")
    print("=" * 70)

    print(f"\nTotal Active Alerts: {len(alerts)}")
    print(f"Critical Alerts: {counts.get('critical', 0)}")
    print(f"Warning Alerts: {counts.get('warning', 0)}")
    print(f"Informational Alerts: {counts.get('info', 0)}")

    print("\nALERT DETAILS")
    print("-" * 70)

    severity_order = {
        "critical": 0,
        "warning": 1,
        "info": 2
    }

    sorted_alerts = sorted(
        alerts,
        key=lambda alert: severity_order.get(
            alert.get("severity", "unknown").lower(), 3
        )
    )

    for alert in sorted_alerts:
        severity = alert.get("severity", "unknown").upper()

        print(f"\nAlert ID : {alert.get('id', 'N/A')}")
        print(f"Severity : {severity}")
        print(f"Device   : {alert.get('node', 'Unknown')}")
        print(f"Title    : {alert.get('title', 'No title')}")
        print(
            "Suggested Action: "
            f"{alert.get('suggested_action', 'Investigate the issue.')}"
        )

    print("\n" + "=" * 70)


def main():
    alerts_file = ROOT / "data" / "sample_alerts.json"

    alerts = load_alerts(alerts_file)
    counts = generate_summary(alerts)

    display_alerts(alerts, counts)


if __name__ == "__main__":
    main()
