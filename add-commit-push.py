# Aliases
# alias g5='cd ~/sprint-5'
# alias acp='python ~/sprint-5/add-commit-push.py'

import subprocess
import sys

def run_command(command):
    """Prints and executes a command, returning the output."""
    print(f"\n> {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

def main():
    commit_message = "Auto commit"
    force = False

    if "-m" in sys.argv:
        msg_index = sys.argv.index("-m") + 1
        if msg_index < len(sys.argv):
            commit_message = sys.argv[msg_index]

    if "-f" in sys.argv:
        force = True

    print("\n git status:")
    run_command("git status")

    commands = [
        "git add .",
        f'git commit -m "{commit_message}"',
        "git push"
    ]

    print("\n Queued commands:")
    for c in commands:
        print(f"  {c}")

    if not force:
        confirm = input("\nRun these commands? (y/n): ").lower()
        if confirm != "y":
            print(" Operation cancelled.")
            sys.exit()

    for c in commands:
        run_command(c)

    print("\n All commands executed successfully")

if __name__ == "__main__":
    main()
