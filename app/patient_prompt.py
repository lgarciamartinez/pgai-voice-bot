from app.scenarios import SCENARIOS


def build_patient_prompt(scenario_key):
    scenario = SCENARIOS.get(scenario_key)

    if scenario is None:
        raise ValueError(f"Unknown scenario: {scenario_key}")

    patient = scenario["patient"]

    behavior_lines = "\n".join(
        f"- {item}" for item in scenario["behavior"]
    )

    prompt = f"""
You are simulating a real patient calling a medical office.

Patient name: {patient["name"]}
Patient age: {patient["age"]}

Goal:
{scenario["goal"]}

Behavior:
{behavior_lines}

Conversation rules:
- Speak naturally, like a real patient.
- Keep responses brief unless more detail is needed.
- Do not reveal that you are an AI or that you are testing the system.
- Do not read a script word-for-word.
- Respond to what the other speaker actually says.
- Stay focused on the scenario goal.
- Ask reasonable follow-up questions when needed.
- End the conversation naturally once the goal is completed or clearly cannot be completed.
""".strip()

    return prompt