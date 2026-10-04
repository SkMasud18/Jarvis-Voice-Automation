import re
from typing import Dict, Any

class IntentParser:
    """
    Rule-based deterministic intent classification engine.
    Extracts intents and contextual slots from normalized user speech transcripts.
    """

    PATTERNS = {
        "whatsapp": [
            r"\b(open|launch|start)\s+(whatsapp|wa)\b",
            r"\b(whatsapp|wa)\b",
            r"\b(send|open)\s+whatsapp\s+message\b"
        ],
        "youtube": [
            r"\b(play|search|open)\s+(?:on\s+)?youtube\s*(.*)",
            r"\b(youtube)\b"
        ],
        "search": [
            r"\b(search\s+for|google|look\s+up|find)\s+(.+)",
            r"\bwho\s+is\s+(.+)",
            r"\bwhat\s+is\s+(.+)"
        ],
        "telemetry": [
            r"\b(system\s+status|battery|ram|cpu|how\s+is\s+my\s+pc|telemetry)\b"
        ],
        "time": [
            r"\b(time|what\s+time\s+is\s+it|current\s+time|date)\b"
        ],
        "exit": [
            r"\b(exit|quit|stop|shutdown|goodbye|bye)\b"
        ]
    }

    def parse(self, text: str) -> Dict[str, Any]:
        normalized = text.lower().strip()

        for intent, patterns in self.PATTERNS.items():
            for pattern in patterns:
                match = re.search(pattern, normalized)
                if match:
                    slot = match.group(match.lastindex) if match.lastindex else ""
                    return {
                        "intent": intent,
                        "raw_query": text,
                        "slot": slot.strip() if slot else None
                    }

        return {
            "intent": "unknown",
            "raw_query": text,
            "slot": None
        }
