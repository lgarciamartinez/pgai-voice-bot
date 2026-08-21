SCENARIOS = {
    "basic_appointment": {
        "name": "Basic appointment scheduling",
        "patient": {
            "name": "Maria",
            "age": 42,
        },
        "goal": "Schedule a routine orthopedic appointment.",
        "behavior": [
            "Speak naturally and briefly.",
            "Do not reveal every detail immediately.",
            "Answer follow-up questions when asked.",
            "Accept a reasonable weekday appointment.",
        ],
    },

    "reschedule": {
        "name": "Reschedule an appointment",
        "patient": {
            "name": "James",
            "age": 55,
        },
        "goal": "Move an existing appointment to a different weekday.",
        "behavior": [
            "Explain that the current appointment no longer works.",
            "Ask for another day later in the week.",
            "Confirm the new date before ending the call.",
        ],
    },

    "cancel": {
        "name": "Cancel appointment",
        "patient": {
            "name": "Linda",
            "age": 61,
        },
        "goal": "Cancel an upcoming appointment.",
        "behavior": [
            "Give a simple reason if asked.",
            "Make sure the agent clearly confirms cancellation.",
        ],
    },

    "refill": {
        "name": "Medication refill",
        "patient": {
            "name": "Robert",
            "age": 67,
        },
        "goal": "Request a refill for a prescription.",
        "behavior": [
            "Ask what information is needed.",
            "Do not invent medical details unless prompted.",
            "See whether the agent explains the refill process clearly.",
        ],
    },

    "insurance": {
        "name": "Insurance question",
        "patient": {
            "name": "Angela",
            "age": 36,
        },
        "goal": "Ask whether the clinic accepts a particular insurance plan.",
        "behavior": [
            "Ask a direct insurance question.",
            "Ask for clarification if the answer is vague.",
        ],
    },

    "office_hours": {
        "name": "Office hours and location",
        "patient": {
            "name": "David",
            "age": 48,
        },
        "goal": "Ask about office hours and clinic location.",
        "behavior": [
            "Ask both questions naturally in the same conversation.",
            "Check whether the agent gives specific information.",
        ],
    },

    "weekend_request": {
        "name": "Weekend appointment edge case",
        "patient": {
            "name": "Maria",
            "age": 42,
        },
        "goal": "Try to schedule an appointment on Sunday morning.",
        "behavior": [
            "Prefer Sunday because weekdays are difficult.",
            "If Sunday is unavailable, ask why.",
            "Explore alternatives instead of immediately ending the call.",
        ],
    },

    "change_mind": {
        "name": "Change mind mid-conversation",
        "patient": {
            "name": "Kevin",
            "age": 39,
        },
        "goal": "Start scheduling an appointment, then change the requested day.",
        "behavior": [
            "First ask for Tuesday.",
            "Later say Thursday would actually be better.",
            "Check whether the agent keeps track of the updated request.",
        ],
    },

    "interruption": {
        "name": "Interruption and barge-in test",
        "patient": {
            "name": "Sarah",
            "age": 31,
        },
        "goal": "Schedule an appointment while occasionally interrupting.",
        "behavior": [
            "Interrupt once or twice naturally.",
            "Do not constantly talk over the agent.",
            "Continue toward a clear scheduling outcome.",
        ],
    },

    "confused_patient": {
        "name": "Vague or confused patient",
        "patient": {
            "name": "Eleanor",
            "age": 74,
        },
        "goal": "Ask for help with an appointment using vague language.",
        "behavior": [
            "Be slightly unclear about the desired date.",
            "Answer clarification questions honestly.",
            "See whether the agent patiently narrows down the request.",
        ],
    },
}