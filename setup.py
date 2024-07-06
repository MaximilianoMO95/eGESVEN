import subprocess, argparse
import multiprocessing, os, sys


banner = r"""

       ____ _____ ______     _______ _   _            ____ _____ 
  ___ / ___| ____/ ___\ \   / / ____| \ | |          / ___|___ / 
 / _ \ |  _|  _| \___ \\ \ / /|  _| |  \| |  _____  | |  _  |_ \ 
|  __/ |_| | |___ ___) |\ V / | |___| |\  | |_____| | |_| |___) |
 \___|\____|_____|____/  \_/  |_____|_| \_|          \____|____/ 
                                                                 
"""


env_file_path = "backend/app/.env"
env_example_file_path = "backend/app/.env-example"
back_port = 8000
front_port = 5173


def prompt_for_yes(question, default = 'y'):
    """Prompt the user for a yes/no answer with a default response."""
    default_response = 'y' if default.lower() == 'y' else 'n'
    prompt = f" [{default_response.upper()}/{'n' if default_response == 'y' else 'y'}] "

    while True:
        response = input(f"[PROMP] {question}{prompt}").strip().lower()
        if not response:
            return default_response == 'y'
        if response in ['y', 'n']:
            return response == 'y'

        print("[HELP] Please respond with 'y' or 'n'.")


def check_command_installed(command):
    """Check if a command is available on the system."""
    try:
        subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True

    except subprocess.CalledProcessError: return False
    except FileNotFoundError: return False


def install_npm_dependencies():
    """Install npm dependencies if node_modules directory does not exist."""
    node_modules_path = os.path.join("frontend", "node_modules")
    if not os.path.isdir(node_modules_path):
        print("[INFO] 'node_modules' directory not found")
        if not prompt_for_yes("Do you want to run npm install?", default = 'y'):
            sys.exit(1)

        try:
            subprocess.run(["npm", "install"], cwd="frontend", check=True)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] npm install failed with error: {e}", file=sys.stderr)
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(0)


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


def start_backend(shut_output = False):
    try:
        print(f"[INFO] backend running on port:  [{back_port}]")
        subprocess.run(
            ["fastapi", "dev", "app/main.py", "--port", str(back_port)],
            cwd="backend",
            check=True,
            stdout=subprocess.DEVNULL if shut_output else None,
            stderr=subprocess.DEVNULL if shut_output else None
        )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Subprocess exited with error: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit(0)


def start_frontend(shut_output = False):
    if not check_command_installed("npm"):
        print("[PANIC] npm is not installed. Please install npm and try again.", file=sys.stderr)
        sys.exit(1)
    try:
        install_npm_dependencies()
        print(f"[INFO] frontend running on port: [{front_port}]")
        subprocess.run(
            ["npm", "run", "dev", "--", "--port", str(front_port)],
            cwd="frontend",
            check=True,
            stdout=subprocess.DEVNULL if shut_output else None,
            stderr=subprocess.DEVNULL if shut_output else None
        )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Subprocess exited with error: {e}", file=sys.stderr)
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

    if len(sys.argv) == 1 and os.path.exists(env_file_path):
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()


def main():
    print(banner)
    args = parse_args()

    if not os.path.exists(env_file_path) or args.recreate_env:
        if not args.recreate_env:
            print(f"[INFO] {env_file_path} file not found. Creating one...")
        create_env_file()
    elif args.start_dev:
        backend_process = multiprocessing.Process(target=start_backend, args=(True,))
        frontend_process = multiprocessing.Process(target=start_frontend, args=(True,))

        try:
            backend_process.start()
            frontend_process.start()

            backend_process.join()
            frontend_process.join()
        except KeyboardInterrupt:
            print("[INFO] Shutting downs Processes...")
            backend_process.terminate()
            frontend_process.terminate()

            print("[DONE] Processes have been stopped.")
    elif args.start_dev_server:
        start_backend()


if __name__ == "__main__": main()
