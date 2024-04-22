import PySimpleGUI as sg

def process_phone_numbers(input_file, output_file):
    print("Processing phone numbers...")
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            # Strip any leading or trailing whitespace
            line = line.strip()
            # Replace '447' with '07' only at the beginning of the line
            if line.startswith('447'):
                line = '07' + line[3:]
            f.write(line + '\n')

    print("Phone numbers processed and saved to", output_file)
    sg.popup("Success", "Phone numbers processed and saved successfully!")

def upload_file():
    input_file = sg.popup_get_file("Select Input File")
    if input_file:
        output_file = sg.popup_get_file("Save As", save_as=True, file_types=(("Text Files", "*.txt"),))
        if output_file:
            process_phone_numbers(input_file, output_file)

# Define the layout
layout = [[sg.Button("Upload File", key="-UPLOAD-")]]

# Create the window
window = sg.Window("Phone Number Converter", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-UPLOAD-":
        upload_file()

# Close the window
window.close()
