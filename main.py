import functions

'''
This is the main.py file for the Job Tracker application.
'''

def main():
    print("\n----Welcome to JobTracker!----")
    welcome = 1

    while True:
        if welcome == 0:
            print("\n----JobTracker----")

        print("1. Add a Job")
        print("2. View/Edit Jobs")
        print("3. Exit")

        option = input("Please select an option: ").strip()

        if option == "1":
            jobs = functions.load_jobs()
            job = functions.add_job()
            jobs.append(job)
            functions.save_jobs(jobs)
            print("Job added successfully!")

        elif option == "2":
            print("\n\nYou have selected View Jobs\n")
            jobs = functions.load_jobs()

            if not jobs:
                print("No jobs found. Please add a job first.")
                welcome = 0
                continue

            for job in jobs:
                print(f"Company:   {job['company_name']}")
                print(f"Job Title: {job['job_title']}")
                print(f"Status:    {job['job_status']}")
                print("-----------------")

            answer = input("\nWould you like to edit or delete a job? (y/n): ").strip().lower()

            if answer == "y":
                company_name = input("Enter the Company name: ").strip()
                job_list = functions.search(company_name)

                if not job_list:
                    print(f"No jobs found for '{company_name}'.")
                    welcome = 0
                    continue

                print(f"\nJobs found matching '{company_name}':")
                for job in job_list:
                    print(f"Company: {job['company_name']} | Title: {job['job_title']} | Status: {job['job_status']}")
                print("-----------------")

                job_title = input("\nEnter the exact Job Title to select: ").strip()
                
                # Find exact match inside job_list
                target_job = None
                for job in job_list:
                    if job["job_title"].lower() == job_title.lower():
                        target_job = job
                        break

                if not target_job:
                    print(f"No job with title '{job_title}' found under '{company_name}'.")
                else:
                    action = input("Type 'edit' to update or 'delete' to remove: ").strip().lower()
                    if action == "edit":
                        functions.edit_job_in_list(jobs, company_name, job_title)
                    elif action == "delete":
                        functions.delete_job_from_list(jobs, target_job)
                    else:
                        print("Invalid action. Returning to main menu.")

        elif option == "3":
            print("You have selected Exit")
            break

        else:
            print("Invalid option selected. Please try again.")

        welcome = 0


if __name__ == "__main__":
    main()