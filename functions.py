import json


def load_jobs():
    '''
    Loads jobs from jobs.json.
    Returns a list of job dictionaries.
    '''

    try:
        with open("jobs.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_jobs(jobs):
    '''
    Saves the list of jobs to jobs.json.
    '''

    try:
        with open("jobs.json", "w") as file:
            json.dump(jobs, file, indent=4)

    except Exception as e:
        print(f"An error occurred while saving jobs: {e}")

'''
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
'''


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

    return {
            "company_name": company_name,
            "job_title": job_title,
            "job_status": job_status
    }


def search(name):
    '''
    Searches for a keyword through the text file.
    Returns matching jobs as a list of dictionaries.
    '''
    jobs = load_jobs()
    found_jobs = []

    for job in jobs:
        if (name.lower() in job["company_name"].lower()
            or name.lower() in jon["job_title"].lower()):
            
            found_jobs.append(job)

    return found_jobs


def edit_jobs():

    job_list = []

    company = input("Enter Company name: ")

    job_list = search(company)
    print(job_list)



    

