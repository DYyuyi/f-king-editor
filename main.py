import sys, os
if len(sys.argv) < 2:
    print("no files input")
    sys.exit()
elif len(sys.argv) > 2:
    print("too much files input")
    sys.exit()

exist = os.path.exists(sys.argv[1])
if not(exist):
    print(f"No Such File Or Directory: {sys.argv[1]}")
    sys.exit()

file = open(sys.argv[1], "r+t", encoding="utf-8")
while True:
    cmd = input("> ")
    for cmd_ in cmd:
        if cmd_ == ".":
            print("---fe---read---start")
            file.seek(0)
            data = file.read()
            print(data)
            print("---fe---read---end--")
        elif cmd_ == "!":
            file.close()
            sys.exit()
        elif cmd_ == "#":
            break
        elif cmd_ == " ":
            continue
        elif cmd_ == "0":
            file.seek(0)
        elif cmd_ == "e":
            file.read()
        elif cmd_ == "a":
            while True:
                line = input()  
                if line == "fwe":  
                    break
                file.write(f"{line}\n")
        elif cmd_ == "c":
                data = file.read()
                file.seek(0)
                for i in range(len(data)):
                    file.write("")
        else:
            print(f"< ? {cmd_}")