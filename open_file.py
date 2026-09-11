def open_file(jobs):

    try:
        with open("jobs.txt", "a") as file:
            file.write(str(jobs))
    except FileNotFoundError:
        try:
            with open("jobs.txt", "w") as file:
                file.write(str(jobs))
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")