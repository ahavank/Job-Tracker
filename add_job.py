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

    return {"company_name": company_name, "job_title": job_title, "job_status": job_status}