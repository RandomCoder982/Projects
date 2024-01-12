file_path = '/home/irene/.config/hypr/hyprland.conf'

num_lines_to_read = 5


with open(file_path, 'r+') as file:

    lines = [file.readline().strip() for _ in range(num_lines_to_read)]

    file.seek(0)

    modified_lines = []
    for line in lines:
        if '#monitor=' in line:
            modified_lines.append(line.replace("#", ""))
        elif "monitor=" in line:
            modified_lines.append(line.replace("", "#", 1))
        else:
            modified_lines.append(line)

    file.write('\n'.join(modified_lines))

