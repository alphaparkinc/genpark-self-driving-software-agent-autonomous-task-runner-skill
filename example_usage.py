from client import SelfDrivingSoftwareAgentAutonomousTaskRunnerClient

def main():
    client = SelfDrivingSoftwareAgentAutonomousTaskRunnerClient()
    res = client.run_autonomous_task("Deploy database migration and verify API endpoints")
    print(f"Result: {res['execution_result']}")
    print(f"Self-healed Errors: {res['self_healed_errors']}")

if __name__ == "__main__":
    main()
