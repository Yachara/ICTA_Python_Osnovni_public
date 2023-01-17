# Rešitev
def funkcija04():
    with open("naloga04_input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        sorted_lines = sorted(lines, key=lambda x: int(x.split(";")[0]), reverse=False)
    
    with open("naloga04_output.txt", "w", encoding="utf-8") as f:
        for line in sorted_lines:
            print(line, end="")
            f.write(line)
funkcija04()