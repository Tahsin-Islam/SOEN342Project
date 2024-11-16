from client_controller import handle_client_menu
from admin_controller import handle_admin_menu
from instructor_controller import handle_instructor_menu
from lesson_controller import create_lesson
# Yoga
def main_menu():
    # while True:
    #     print("\nLesson Management System Menu")
    #     print("==============================")
    #     print("1. Client Menu")
    #     print("2. Admin Menu")
    #     print("3. Instructor Menu")
    #     print("4. Exit")
        
    #     choice = input("\nSelect an option: ")
        
    #     if choice == "1":
    #         handle_client_menu()
    #         print("Displaying Client menu")
    #     elif choice == "2":
    #         handle_admin_menu()
    #         print("Displaying Admin menu")
    #     elif choice == "3":
    #         handle_instructor_menu()
    #         print("Displaying intructor menu")
    #     elif choice == "4":
    #         print("Exiting program.")
    #         break
    #     else:
    #         print("Invalid option. Please try again.")
    # create_database()
    create_lesson()

if __name__ == "__main__":
    main_menu()
