print("Welcome to JukSCRIPT!!!")

#get file data of line
def readfile(file, line):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            if line < 1 or line > len(lines):
                return f"Error: Line {line} is out of range. The file has {len(lines)} lines."
            return lines[line - 1].strip()
    except FileNotFoundError:
        return f"Error: The file '{file}' was not found."
    except Exception as e:
        return f"Error: {str(e)}"
#get lenght of file
def linenumber(file):
    try:
        with open(file, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return f"Error: The file '{file}' was not found."
    except Exception as e:
        return f"Error: {str(e)}"
#write a line
def writeline(file, line, content):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        # Adjust the number of lines if necessary
        while len(lines) < line:
            lines.append('\n')

        # Insert the content at the specified line
        lines[line - 1] = content + '\n'

        with open(file, 'w') as f:
            f.writelines(lines)
        
        return f"Successfully wrote to line {line} in the file '{file}'."
    
    except FileNotFoundError:
        return f"Error: The file '{file}' was not found."
    except Exception as e:
        return f"Error: {str(e)}"

#mainloop
while True:
    filename = input("Filename: ")
    num = 0
    while num < linenumber(filename):
        num += 1
        cmd = readfile(filename, num)
        comm = cmd[0]
        if comm == "p": print(readfile(filename, cmd[1:4]))
        elif comm == "i": writeline(filename, cmd[1:4], input("fromScript? "))
        elif comm == "+": writeline(filename, cmd[9:12], cmd[1:4]+cmd[5:8])
        elif comm == "-": writeline(filename, cmd[9:12], cmd[1:4]-cmd[5:8])
        elif comm == "/": writeline(filename, cmd[9:12], cmd[1:4]/cmd[5:8])
        elif comm == "*": writeline(filename, cmd[9:12], cmd[1:4]*cmd[5:8])
        elif comm == "l":
            filename = readfile(filename, cmd[1:4])
            num = 0
        elif comm == "j": num = cmd[1:4]-1
        elif comm == "c":
             if not cmd[1:4] == cmd[5:8]: num += 1
        else: print("Error!!!")