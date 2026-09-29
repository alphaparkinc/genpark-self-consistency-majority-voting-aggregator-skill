# genpark-self-consistency-majority-voting-aggregator-skill

Wang et al. Self-Consistency majority voting aggregator computing consensus answers, vote distributions, and Shannon entropy over multi-path reasoning outputs.

## Architecture

```mermaid
flowchart TD
    Path1[Reasoning Path 1] --> Aggregator[Self-Consistency Aggregator]
    Path2[Reasoning Path 2] --> Aggregator
    Path3[Reasoning Path 3] --> Aggregator
    Aggregator --> Mode[Majority Mode Winner]
    Aggregator --> Stats[Confidence & Shannon Entropy]
```

## Features
- **Entropy Calculation**: Quantifies disagreement uncertainty across sampled paths.
- **Pure Python**: 100% standard library.
