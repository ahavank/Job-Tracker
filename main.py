jobs = []
# I used this While statement in the very beginning of the code to insure the full code runs in a loop until the user selects exit themselves. 
# This is so the user can select multiple options from the menu without having to restart the program each time they want to select a new option.
while True:
    #This is the menu texts that show the user all the possible options they can select from.
    print("Welcome to JobTracker!")
    print("1. Add a Job")
    print("2. View Jobs")
    print("3. Exit")
    option=input("Please select an option: ")


    # If the user selects one of the 3 numbers from the menu these if statements will run the code that corresponds to the option selected.
    if option == "1":
        print ("You have selected Add a Job")
        company_name = input("Enter the company name: ")
        job_title = input("Enter the job title: ")
        # I used the append method to add the company name to the end of the list in job
        jobs.append
        ({
            "company_name": company_name, 
            "job_title": job_title
        })
        print("Job added successfully!")

    elif option == "2":
        print ("You have selected View Jobs")
        for job in jobs:
            print("Company Name: ", job["company_name"]) 
            print("Job Title: ", job["job_title"])
            print()   

    elif option == "3":
        print ("You have selected Exit")
        exit()

# The else statement is to insure that is the user selects a valid option from the menu. 
# If they do not select a valid option they will be prompted to try again.
    else:
        print ("Invalid option selected. Please try again.")
    