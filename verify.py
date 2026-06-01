import os
import subprocess
import sys

def check_git_exists():
    if not os.path.exists(".git"):
        print("[ERROR] Error: .git directory not found.")
        sys.exit(1)
    print("[SUCCESS] Success: .git directory exists.")

def check_branch_name():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        if branch != "main":
            print(f"[ERROR] Error: Current branch is '{branch}', expected 'main'.")
            sys.exit(1)
        print("[SUCCESS] Success: Current branch is 'main'.")
    except Exception as e:
        print(f"[ERROR] Error while checking branch: {e}")
        sys.exit(1)

def check_remote_url():
    try:
        remote_url = subprocess.check_output(["git", "remote", "get-url", "origin"]).decode().strip()
        expected = "https://github.com/gilppon/slm-agent-home"
        if remote_url != expected:
            print(f"[ERROR] Error: Remote URL is '{remote_url}', expected '{expected}'.")
            sys.exit(1)
        print(f"[SUCCESS] Success: Remote URL matches '{expected}'.")
    except Exception as e:
        print(f"[ERROR] Error while checking remote URL: {e}")
        sys.exit(1)

def check_gitignore():
    try:
        result = subprocess.run(["git", "check-ignore", "relocation_report.txt"], capture_output=True)
        if result.returncode == 0:
            print("[SUCCESS] Success: 'relocation_report.txt' is correctly ignored by git.")
        else:
            print("[ERROR] Error: 'relocation_report.txt' is NOT ignored by git.")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Error checking gitignore: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("[START] Running Global PMO Harness Gate verification...")
    check_git_exists()
    check_branch_name()
    check_remote_url()
    check_gitignore()
    print("[OK] All local verification gates PASSED successfully!")
