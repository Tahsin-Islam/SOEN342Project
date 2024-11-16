# client_view.py
def display_client_menu():
    print("\n--- Client Menu ---")
    print("1. View Available Lessons")
    print("2. Book a Lesson")
    print("3. View My Bookings")
    print("4. Manage Lesson")
    print("5. Log Out")
    
def get_client_choice():
    return input("\nSelect an option: ")
