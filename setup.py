import subprocess, argparse, sys, os


banner = r"""

       ____ _____ ______     _______ _   _            ____ _____ 
  ___ / ___| ____/ ___\ \   / / ____| \ | |          / ___|___ / 
 / _ \ |  _|  _| \___ \\ \ / /|  _| |  \| |  _____  | |  _  |_ \ 
|  __/ |_| | |___ ___) |\ V / | |___| |\  | |_____| | |_| |___) |
 \___|\____|_____|____/  \_/  |_____|_| \_|          \____|____/ 
                                                                 
"""


env_file_path = "backend/app/.env"
env_example_file_path = "backend/app/.env-example"


def read_env_example():
    env_vars = {}
    if os.path.exists(env_example_file_path):
        with open(env_example_file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, default_value = line.split("=", 1)
                    env_vars[key] = default_value

    return env_vars


def create_env_file():
    env_vars = read_env_example()

    if not env_vars:
        print(f"[PANIC] {env_example_file_path} file is missing or empty.")
        return


    print(f"[INFO] Creating {env_file_path} file.")
    print("\n[PROMP] Please provide the following values:")

    with open(env_file_path, "w") as file:
        for key, default_value in env_vars.items():
            value = input(f"{key} (default: {default_value}): ") or default_value

            file.write(f"{key}={value}\n")
            print(f"{key} set to: {value}")

    print(f"[DONE] {env_file_path} has been created successfully.")


def start_backend():
    try:
        subprocess.run(["fastapi", "dev", "app/main.py"], cwd="backend", check=True)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess exited with error: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit(0)


def start_frontend():
    try:
        subprocess.run(["npm", "run", "dev"], cwd="frontend", check=True)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess exited with error: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit(0)



def parse_args():
    parser = argparse.ArgumentParser(description="Setup Script For eGESVEN.")
    parser.add_argument(
        "--recreate-env",
        action="store_true",
        help=f"Force recreation of the {env_file_path} file even if it already exists."
    )
    parser.add_argument(
        "--start-dev",
        action="store_true",
        help="Start both the server and react app."
    )
    parser.add_argument(
        "--start-dev-server",
        action="store_true",
        help="Start just the development server."
    )
    return parser.parse_args()


def main():
    print(banner)
    args = parse_args()

    if not os.path.exists(env_file_path) or args.recreate_env:
        if not args.recreate_env:
            print(f"[INFO] {env_file_path} file not found. Creating one...")
        create_env_file()
    elif args.start_dev:
        start_backend()
        start_frontend()
    elif args.start_dev_server:
        start_backend()


if __name__ == "__main__": main()
