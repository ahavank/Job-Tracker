def open_file(jobs):

    try:
        with open("jobs.txt", "a") as file:
            for job in jobs:
                file.write(f"Company: {job['company_name']}\n")
                file.write(f"Job Title: {job['job_title']}\n")
                file.write(f"Job Status: {job['job_status']}\n")
                file.write("----------------\n")

                           
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")