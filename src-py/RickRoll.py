from time import time
start = time()

from sys import argv, stdout
# from os.path import exists
# from traceback2 import format_exc

# from interpreter import run_in_interpreter
# from pyrickroll import run_in_py, Token
# from crickroll import run_in_cpp
# import AudioGenerator

# Help message
rick_help = """
Programming by writing code:   rickroll -py [File_Name]
Generate an audio: rickroll -py [File_Name] -audio [Audio_Name]

Other Options:
--time:      Show execution time of your code
--help/--h:  Help
"""

# Set and start a timer


def play_audio(src_file_name):
    import AudioGenerator
    from pyrickroll import Token

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for statement in content:
            obj = Token(statement)

            for i in range(len(obj.t_types)):
                AudioGenerator.play(obj.t_values[i])

def main():
    is_audio = False
    is_help = False
    show_time = False

    is_cpp = False
    is_py = False
    is_intpr = False

    src_file_name = ''

    if len(argv) <= 1:
        exit(rick_help)

    for i in range(len(argv)):
        current_arg = argv[i].lower()

        # Run code -py [file_name]
        if current_arg == '-py':
            src_file_name = argv[i + 1]
            is_py = True
        # Run code -cpp [file_name]
        if current_arg == '-cpp':
            src_file_name = argv[i + 1]
            is_cpp = True
        # Run code -intpr [file_name]
        if current_arg == '-intpr':
            src_file_name = argv[i + 1]
            is_intpr = True
        # Generate audio. --audio [Output audio file name]
        if current_arg == '--audio':
            is_audio = True
        # Help message
        if current_arg == '--help':
            is_help = True

        # Show execution time
        if current_arg == '--time':
            show_time = True

    # Run the RickRoll program
    if src_file_name:
        from os.path import exists
        if exists(src_file_name):
            # Convert .rickroll to C++
            if is_cpp:
                from crickroll import run_in_cpp
                run_in_cpp(src_file_name)

            # Convert .rickroll to Python
            elif is_py:
                try:
                    from pyrickroll import run_in_py
                    exec(run_in_py(src_file_name), globals(), globals())
                except:
                    from traceback2 import format_exc
                    error_msg = format_exc().split('File "<string>",')[-1]
                    stdout.write(f'Exception in{error_msg}')

            # Execute .rickroll using the interpreter
            elif is_intpr:
                from interpreter import run_in_interpreter
                run_in_interpreter(src_file_name)

        else: exit(f"File [{src_file_name}] doesn't exist...")
    else: stdout.write('Warning: [Not executing any script...]')


    if is_audio:
        play_audio(src_file_name)

    if is_help:
        stdout.write(rick_help)

    if show_time:
        stdout.write(f'\nExecution Time: [{time() - start}] sec.')


if __name__ == "__main__":
    main()
