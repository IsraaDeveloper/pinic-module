import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: nano <filename>")
        return

    filename = sys.argv[1]

    # pastikan path relatif (tetap di virtual fs)
    path = os.path.abspath(filename)

    print("=== PINICOS nano ===")
    print("CTRL+D to save & exit")
    print("---------------------")

    content = []

    # jika file sudah ada → tampilkan dulu
    if os.path.exists(path):
        if os.path.isdir(path):
            print("Error: Is a directory")
            return

        print("[ Existing content ]")
        with open(path, "r") as f:
            old = f.read()
            print(old)
            if old:
                content = old.splitlines()

        print("---------------------")

    print("Start typing:")

    try:
        while True:
            line = input()
            content.append(line)
    except EOFError:
        pass

    # simpan file
    try:
        with open(path, "w") as f:
            f.write("\n".join(content) + "\n")
        print(f"\nSaved: {filename}")
    except Exception as e:
        print("Failed to save file:", e)


if __name__ == "__main__":
    main()
