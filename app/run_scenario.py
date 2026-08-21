import sys

from app.scenarios import SCENARIOS


def show_scenario(scenario_key):
    scenario = SCENARIOS.get(scenario_key)

    if scenario is None:
        print(f"Unknown scenario: {scenario_key}")
        print("\nAvailable scenarios:")

        for key in SCENARIOS:
            print(f"  - {key}")

        return

    patient = scenario["patient"]

    print("\nSelected patient scenario")
    print("-------------------------")
    print(f"Scenario: {scenario['name']}")
    print(f"Patient: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Goal: {scenario['goal']}")

    print("\nBehavior:")
    for behavior in scenario["behavior"]:
        print(f"  - {behavior}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m app.run_scenario <scenario>")
        print("\nAvailable scenarios:")

        for key in SCENARIOS:
            print(f"  - {key}")

        sys.exit(1)

    show_scenario(sys.argv[1])