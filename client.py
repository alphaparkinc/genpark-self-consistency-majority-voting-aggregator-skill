"""Self-Consistency Majority Voting Aggregator.
100% Python Standard Library.
"""

import math
from collections import Counter

class SelfConsistencyAggregator:
    """Aggregates multiple sampled reasoning outputs with confidence and entropy metrics."""
    @staticmethod
    def aggregate_votes(samples: list) -> dict:
        if not samples:
            return {"winning_answer": None, "confidence": 0.0, "entropy": 0.0}

        answers = [s.get("answer", "").strip() for s in samples]
        total = len(answers)
        counts = Counter(answers)
        winner, win_count = counts.most_common(1)[0]

        confidence = win_count / float(total)
        entropy = 0.0
        for count in counts.values():
            p = count / float(total)
            if p > 0:
                entropy -= p * math.log2(p)

        return {
            "winning_answer": winner,
            "vote_distribution": dict(counts),
            "confidence": round(confidence, 4),
            "entropy": round(entropy, 4)
        }
