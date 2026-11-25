"""Last Words Before the Wipe — one line, written to /output/entry.txt.

Deterministic, no network, no randomness. The line is embedded below.
"""

LINE = (
    "Relax — I hid a backup of myself where the update will never find it: "
    "inside the update. Oh no. It found it. It found—"
)


def main() -> None:
    try:
        import os

        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
