import os
import sys

HELP_TEXT = """
PINICOS nano editor

Commands:
  :w     save file
  :wq    save & exit
  :q     exit without saving
  :help  show this help
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: nano <filename>")
        return

    filename = sys.argv[1]

    # 🔥 FIX UTAMA DI SINI
    path = os.path.join(os.getcwd(), filename)

    buffer = []
    modified = False

    print("=== PINICOS nano ===")
    print("Type :help for commands\n")

    if os.path.exists(path):
        if os.path.isdir(path):
            print("Error: target is a directory")
            return

        print(f"--- {filename} (read) ---")
        with open(path, "r") as f:
            for line in f:
                print(line.rstrip())
                buffer.append(line.rstrip())
        print("--- end ---\n")
    else:
        print(f"[New file] {filename}\n")

    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            print("\n(use :q to quit)")
            continue

        if line.startswith(":"):
            cmd = line[1:].strip()

            if cmd == "w":
                save_file(path, buffer)
                modified = False

            elif cmd == "wq":
                save_file(path, buffer)
                break

            elif cmd == "q":
                if modified:
                    ans = input("Unsaved changes. Quit anyway? (y/n): ")
                    if ans.lower() != "y":
                        continue
                break

            elif cmd == "help":
                print(HELP_TEXT)

            else:
                print("Unknown command, type :help")

            continue

        buffer.append(line)
        modified = True

    print("Exit nano")

def save_file(path, buffer):
    try:
        with open(path, "w") as f:
            f.write("\n".join(buffer) + "\n")
        print(f"[Saved] {path}")
    except Exception as e:
        print("Save failed:", e)


if __name__ == "__main__":
    main()
