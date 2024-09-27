def welcome():
    print("\nWelcome to the University Admissions and Scholarships Chatbot!")
    print("How can I assist you today?")
    print("1. Admission Requirements")
    print("2. Scholarship Information")
    print("3. Application Process")
    print("4. Exit")


def admission_requirements():
    print("Admission Requirements:")
    print("1. Completed application form")
    print("2. High school diploma or equivalent")
    print("3. Letters of recommendation")
    print("4. Personal statement")
    print("5. Standardized test scores (if applicable)")
    input("Press Enter to return to the main menu...")


def scholarship_information():
    print("Scholarship Information:")
    print("1. Academic scholarships")
    print("2. Need-based scholarships")
    print("3. Athletic scholarships")
    print("4. Diversity scholarships")
    print("For more details, visit our scholarship webpage.")
    input("Press Enter to return to the main menu...")


def application_process():
    print("Application Process:")
    print("1. Fill out the application form online.")
    print("2. Submit required documents.")
    print("3. Pay the application fee.")
    print("4. Await admission decision.")
    input("Press Enter to return to the main menu...")


def main():
    while True:
        welcome()
        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            admission_requirements()
        elif choice == '2':
            scholarship_information()
        elif choice == '3':
            application_process()
        elif choice == '4':
            confirm = input("Are you sure you want to exit? (yes/no): ")
            if confirm.lower() == 'yes':
                print("Thank you for using the chatbot. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
