
#!/usr/bin/env python3

"""
NVIDIA NetQ-Based Network Monitoring & Deployment Automation
Module: Network Event Analyzer

Analyzes simulated network events and classifies their severity.
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_events(file_path):
    """Load network event records."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("events", [])
    except FileNotFoundError:
        print("[ERROR] Network events file not found.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print("[ERROR] Invalid network events JSON.")
        raise SystemExit(1)


def analyze_events(events):
    """Calculate event counts by severity."""
    counts = Counter()

    for event in events:
        severity = event.get("severity", "unknown").lower()
        counts[severity] += 1

    return counts


def display_events(events, counts):
    """Display event summary and detailed records."""
    print("=" * 65)
    print(" NVIDIA NETQ - NETWORK EVENT ANALYZER")
    print("=" * 65)

    print(f"\nTotal Events: {len(events)}")
    print(f"Critical Events: {counts.get('critical', 0)}")
    print(f"Warning Events: {counts.get('warning', 0)}")
    print(f"Informational Events: {counts.get('info', 0)}")

    print("\nEVENT DETAILS")
    print("-" * 65)

    severity_order = {
        "critical": 0,
        "warning": 1,
        "info": 2
    }

    sorted_events = sorted(
        events,
        key=lambda event: severity_order.get(
            event.get("severity", "unknown").lower(), 3
        )
    )

    for event in sorted_events:
        severity = event.get("severity", "unknown").upper()

        print(f"\n[{severity}]")
        print(f"Timestamp : {event.get('timestamp', 'N/A')}")
        print(f"Device    : {event.get('node', 'Unknown')}")
        print(f"Message   : {event.get('message', 'No description')}")

    print("\n" + "=" * 65)


def main():
    events_file = ROOT / "data" / "network_events.json"

    events = load_events(events_file)
    counts = analyze_events(events)

    display_events(events, counts)


if __name__ == "__main__":
    main()
