from client import SelfConsistencyAggregator

samples = [
    {"answer": "True"},
    {"answer": "True"},
    {"answer": "False"}
]
vote = SelfConsistencyAggregator.aggregate_votes(samples)
print("Consensus Winner:", vote["winning_answer"], "Confidence:", vote["confidence"])
