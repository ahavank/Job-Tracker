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



def add_job():
    '''
    This function prompts the user to input the company name, job title, and job status for a new job entry.
    It returns a dictionary containing the job details.
    '''
    print("You have selected Add a Job")
    company_name = input("Enter the company name: ")
    job_title = input("Enter the job title: ")

    # Default value for job_status to ensure the while loop runs at least once
    job_status = "n/a" 

    # Get user input for job status
    while job_status == "n/a":
        job_status = input("Enter the job status (e.g., applied, interview, offer, decline): ")
        job_status = job_status.lstrip().lower().capitalize()  # Convert to lowercase for consistency
        # Check if the job status is valid
        if job_status.lower() not in {"applied", "interview", "offer", "decline"}:
            print("Invalid job status. Please enter a valid job status.")
            job_status = "n/a"

    return {"company_name": company_name,
            "job_title": job_title,
            "job_status": job_status
    }


def search(name):
    '''
    This function searches for a keyword through the text file.
    Returns the lines with the keywords as a list.
    '''
    found_lines = []
    try:
        with open("jobs.txt", "r", encoding='utf-8') as file:
            for line in file:
                if name in line:
                    found_lines.append(line)
    except Exception as e:
        print(f"An error occurred while searching the file: {e}")

    return found_lines


def edit_jobs():

    job_list = []

    company = input("Enter Company name: ")

    job_list = search(company)
    print(job_list)



    

