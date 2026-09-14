import add_job
import open_file
'''
This is the main.py file for the Job Tracker application. It provides a command-line interface for users to add and view job entries.
The application allows users to input the company name, job title, and job status for each job entry. 
The job entries are stored in a list and can be viewed by the user.
The application runs in a loop until the user selects the exit option from the menu.
'''

def main():
    jobs = []

    # This while statement keeps the program running until the user selects exit.
    while True:
        # This menu shows the user all the possible options.
        print("\n----Welcome to JobTracker!----")
        print("1. Add a Job")
        print("2. View Jobs")
        print("3. Exit")

        option = input("Please select an option: ")

        # If the user selects one of the menu options, the corresponding code runs.
        if option == "1":

            # Add the company name and job title to the jobs list.
            jobs.append(add_job.add_job())

            open_file.open_file(jobs)

            print("Job added successfully!")


        elif option == "2":
        
            print("\nYou have selected View Jobs")
            try:
                with open("jobs.txt", "r") as file:
                    contents = file.read()
                    print(contents)
            except FileNotFoundError:
                print("No jobs found. Please add a job first.")
        
            '''
            for job in contents:
                print("Company:", job["company_name"])
                print("Job Title:", job["job_title"])
                print("Job Status:", job["job_status"])
                print()
            '''
        elif option == "3":
            print("You have selected Exit")
            exit()
    # The else statement is to insure that is the user selects a valid option from the menu. 
    # If they do not select a valid option they will be prompted to try again.
        else:
            print("Invalid option selected. Please try again.")

main()