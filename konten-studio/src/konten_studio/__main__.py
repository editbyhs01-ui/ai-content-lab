from .engine import SPECIALISTS, workflow_overview


def main() -> None:
    print("Konten Studio — starter workflow (no external agents are executed)")
    print(workflow_overview())
    print("Specialist roles:")
    for role in SPECIALISTS:
        print(f"- {role}")


if __name__ == "__main__":
    main()
