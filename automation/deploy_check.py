
#!/usr/bin/env python3

"""
NVIDIA NetQ-Based Network Monitoring & Deployment Automation
Module: Deployment Configuration Validator

Purpose:
Validate sample network topology and configuration
before a proposed deployment.

Note: This script performs local validation only.
It does not deploy configurations to real switches.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(file_path):
    """Load and parse a JSON configuration file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        raise SystemExit(1)
    except json.JSONDecodeError as error:
        print(f"[ERROR] Invalid JSON: {error}")
        raise SystemExit(1)


def validate_topology(topology):
    """Validate topology nodes and network links."""
    errors = []

    nodes = topology.get("nodes", [])
    links = topology.get("links", [])

    if not nodes:
        errors.append("No network nodes found.")

    node_ids = [node.get("id") for node in nodes]

    if None in node_ids:
        errors.append("A network node is missing its ID.")

    if len(node_ids) != len(set(node_ids)):
        errors.append("Duplicate network node IDs detected.")

    valid_nodes = set(node_ids) - {None}

    for link in links:
        source = link.get("source")
        target = link.get("target")

        if source not in valid_nodes:
            errors.append(f"Unknown link source: {source}")

        if target not in valid_nodes:
            errors.append(f"Unknown link target: {target}")

    return errors, valid_nodes, links


def validate_telemetry(telemetry, valid_nodes):
    """Check whether telemetry references known devices."""
    errors = []

    for device in telemetry.get("devices", []):
        node = device.get("node")

        if node not in valid_nodes:
            errors.append(
                f"Telemetry references unknown device: {node}"
            )

    return errors


def main():
    print("=" * 55)
    print(" NVIDIA NETQ - DEPLOYMENT VALIDATION")
    print("=" * 55)

    topology_file = ROOT / "configs" / "network-topology.json"
    telemetry_file = ROOT / "data" / "sample_telemetry.json"

    topology = load_json(topology_file)
    telemetry = load_json(telemetry_file)

    errors, valid_nodes, links = validate_topology(topology)
    errors.extend(validate_telemetry(telemetry, valid_nodes))

    if errors:
        print("\n[FAILED] Configuration validation failed.")

        for error in errors:
            print(f"  - {error}")

        raise SystemExit(1)

    print("\n[SUCCESS] Configuration validation passed.")
    print(f"Validated Nodes : {len(valid_nodes)}")
    print(f"Validated Links : {len(links)}")
    print(
        "Telemetry Devices :",
        len(telemetry.get("devices", []))
    )

    print("\nDeployment readiness: PASSED")
    print("Note: No real network deployment was performed.")
    print("=" * 55)


if __name__ == "__main__":
    main()
