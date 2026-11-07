import json
import statistics

SAMPLES = [12.4, 11.9, 13.1, 12.7, 12.2]


def main():
    summary = {
        "samples": SAMPLES,
        "mean": statistics.mean(SAMPLES),
        "stdev": statistics.pstdev(SAMPLES),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
