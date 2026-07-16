#!/usr/bin/env python3
import subprocess
import sys

<<<<<<< HEAD
def run_git(args):
    """Runs a git command with a list of args. No shell quoting issues."""
    result = subprocess.run(["git"] + args, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"\n❌ Error: git {' '.join(args)}")
=======
def run_command(cmd):
    """Runs a shell command and returns output, raising an exception on error."""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"\n❌ Error executing command: {cmd}")
>>>>>>> 4c4af82f5d52777863c8bbe3a0dfe4695fdb1612
        print(f"Details:\n{result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()

def main():
    print("🚀 =========================================")
    print("🚀  MELLOTECH GIT DEPLOYMENT HELPER")
    print("🚀 =========================================\n")

    # 1. Show current git status
    print("📋 Checking current status...")
<<<<<<< HEAD
    status = run_git(["status", "-s"])
    if not status:
        git_status_full = run_git(["status"])
        if "Your branch is ahead of" not in git_status_full:
            print("✅ No changes to commit or push. Everything is up to date!")
            sys.exit(0)

=======
    status = run_command("git status -s")
    if not status:
        # Check if we are ahead of any remote branches
        # e.g., if git status shows we need to push
        git_status_full = run_command("git status")
        if "Your branch is ahead of" not in git_status_full:
            print("✅ No changes to commit or push. Everything is up to date!")
            sys.exit(0)
    
>>>>>>> 4c4af82f5d52777863c8bbe3a0dfe4695fdb1612
    if status:
        print("\nModified/New Files:")
        print(status)
        print("")

        # 2. Get commit message
        if len(sys.argv) > 1:
            commit_message = " ".join(sys.argv[1:])
        else:
            try:
                commit_message = input("💬 Enter commit message: ").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled.")
                sys.exit(0)
<<<<<<< HEAD

=======
                
>>>>>>> 4c4af82f5d52777863c8bbe3a0dfe4695fdb1612
            if not commit_message:
                commit_message = "Update Mellotech website"
                print(f"⚠️ No message entered. Using default: '{commit_message}'")

        # 3. Add all changes
        print("\n📦 Staging changes (git add -A)...")
<<<<<<< HEAD
        run_git(["add", "-A"])

        # 4. Commit changes
        print(f"💾 Committing changes: '{commit_message}'...")
        commit_out = run_git(["commit", "-m", commit_message])
        print(commit_out)

    # 5. Push to all configured remotes
    remotes = run_git(["remote"]).split()
    branch = run_git(["branch", "--show-current"])

    if not remotes:
        print("❌ No git remotes configured to push to!")
        sys.exit(1)

    for remote in remotes:
        print(f"\n⚡ Pushing to {remote.upper()} ({remote} branch: {branch})...")
        run_git(["push", remote, branch])
        print(f"✅ Successfully pushed to {remote}!")
=======
        run_command("git add -A")

        # 4. Commit changes
        print(f"💾 Committing changes: '{commit_message}'...")
        commit_out = run_command(f'git commit -m "{commit_message}"')
        print(commit_out)

    # 5. Push to all configured remotes
    remotes = run_command("git remote").split()
    branch = run_command("git branch --show-current")
    
    if not remotes:
        print("❌ No git remotes configured to push to!")
        sys.exit(1)
        
    for remote in remotes:
        print(f"\n⚡ Pushing to {remote.upper()} ({remote} branch: {branch})...")
        try:
            push_out = run_command(f"git push {remote} {branch}")
            print(f"✅ Successfully pushed to {remote}!")
        except Exception as e:
            print(f"❌ Failed to push to {remote}.")
>>>>>>> 4c4af82f5d52777863c8bbe3a0dfe4695fdb1612

    print("\n🚀 Deployment workflows triggered on active remotes!")

if __name__ == "__main__":
    main()
