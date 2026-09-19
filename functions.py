import json

def load_jobs():
    '''Loads jobs from jobs.json. Returns a list of job dictionaries.'''
    try:
        with open("jobs.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_jobs(jobs):
    '''Saves the list of jobs to jobs.json.'''
    try:
        with open("jobs.json", "w") as file:
            json.dump(jobs, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving jobs: {e}")


def add_job():
    '''Prompts the user to input job details and returns a dictionary.'''
    print("\nYou have selected Add a Job")
    company_name = input("Enter the company name: ").strip()
    job_title = input("Enter the job title: ").strip()

    job_status = "n/a" 
    while job_status == "n/a":
        job_status = input("Enter the job status (e.g., applied, interview, offer, decline): ").strip().capitalize()
        if job_status.lower() not in {"applied", "interview", "offer", "decline"}:
            print("Invalid job status. Please try again.")
            job_status = "n/a"

    return {
        "company_name": company_name,
        "job_title": job_title,
        "job_status": job_status
    }


def search(keyword):
    '''Searches for a keyword across company names and job titles.'''
    jobs = load_jobs()
    found_jobs = []
    query = keyword.strip().lower()

    if not query:
        return []

    for job in jobs:
        if (query in job["company_name"].lower() or query in job["job_title"].lower()):
            found_jobs.append(job)

    return found_jobs


def edit_job_in_list(jobs, company_name, job_title):
    '''
    Finds the exact job in the master jobs list, prompts for updates,
    and saves changes back to jobs.json.
    '''
    target_job = None
    
    # Locate the exact dictionary using company_name and job_title
    for job in jobs:
        if job["company_name"].lower() == company_name.lower() and job["job_title"].lower() == job_title.lower():
            target_job = job
            break

    if not target_job:
        print(f"Could not locate '{job_title}' at '{company_name}' in the list.")
        return

    print(f"\nEditing: {target_job['company_name']} - {target_job['job_title']}")
    
    new_company = input(f"Enter new company name (Leave blank to keep '{target_job['company_name']}'): ").strip()
    if new_company:
        target_job['company_name'] = new_company

    new_title = input(f"Enter new job title (Leave blank to keep '{target_job['job_title']}'): ").strip()
    if new_title:
        target_job['job_title'] = new_title

    new_status = input(f"Enter new job status (Leave blank to keep '{target_job['job_status']}'): ").strip().capitalize()
    if new_status:
        while new_status.lower() not in {"applied", "interview", "offer", "decline"}:
            print("Invalid status. Choose: Applied, Interview, Offer, or Decline.")
            new_status = input("Enter new job status: ").strip().capitalize()
        target_job['job_status'] = new_status

    save_jobs(jobs)
    print("Job updated successfully!")


def delete_job_from_list(jobs, company_name, job_title):
    '''Removes the specified job dictionary from the master list and saves changes.'''
    target_job = None
    
    for job in jobs:
        if job["company_name"].lower() == company_name.lower() and job["job_title"].lower() == job_title.lower():
            target_job = job
            break

    if target_job:
        jobs.remove(target_job)
        save_jobs(jobs)
        print(f"Deleted '{company_name} - {job_title}' successfully!")
    else:
        print(f"Could not locate '{job_title}' at '{company_name}' to delete.")