import easygui as eg

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
MIN_STAT = 1
MAX_STAT = 25
STATS = ["strength", "speed", "stealth", "cunning"]

ADD_OPTION = 'Add'
SEARCH_OPTION = 'Search / edit'
DELETE_OPTION = 'Delete'
PRINT_OPTION = 'Print'
EXIT_OPTION = 'Exit'
MAIN_MENU = [ADD_OPTION, SEARCH_OPTION, DELETE_OPTION, PRINT_OPTION, EXIT_OPTION]

# -----------------------------------------------------------------------------
# Catalogue setup and formatting
# -----------------------------------------------------------------------------
def create_catalogue():
    """Create and return the starting nested dictionary catalogue."""
    return {
        "Stoneling": {"strength": 7, "speed": 1, "stealth": 25, "cunning": 15},
        "Vexscream": {"strength": 1, "speed": 6, "stealth": 21, "cunning": 19},
        "Dawnmirage": {"strength": 5, "speed": 15, "stealth": 18, "cunning": 22},
        "Blazegolem": {"strength": 15, "speed": 20, "stealth": 23, "cunning": 6},
        "Websnake": {"strength": 7, "speed": 15, "stealth": 10, "cunning": 5},
        "Moldvine": {"strength": 21, "speed": 18, "stealth": 14, "cunning": 5},
        "Vortexwing": {"strength": 19, "speed": 13, "stealth": 19, "cunning": 2},
        "Rotthing": {"strength": 16, "speed": 7, "stealth": 4, "cunning": 12},
        "Froststep": {"strength": 14, "speed": 14, "stealth": 17, "cunning": 4},
        "Wispghoul": {"strength": 17, "speed": 19, "stealth": 3, "cunning": 2}
    }

# -----------------------------------------------------------------------------
# Main features
# -----------------------------------------------------------------------------
def add_card(catalogue):
    """Placeholder before Add New Monster Card was developed."""
    eg.msgbox("Add new monster card has not been developed yet.", "Not Developed")

def search_edit_card(catalogue):
    """Placeholder before Search/Edit was developed."""
    eg.msgbox("Search / edit monster card has not been developed yet.", "Not Developed")

def delete_card(catalogue):
    """Placeholder before Delete was developed."""
    eg.msgbox("Delete monster card has not been developed yet.", "Not Developed")

def print_catalogue(catalogue):
    """Placeholder before Print Full Catalogue was developed."""
    eg.msgbox("Print full catalogue has not been developed yet.", "Not Developed")

def show_main_menu():
    """Show the main menu and return the user selection."""
    return eg.buttonbox("Choose an option:", "Monster Card Catalogue", MAIN_MENU)

# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------
def main():
    catalogue = create_catalogue()
    eg.msgbox("Welcome to the Monster Card Catalogue.", "Welcome")
    while True:
        choice = show_main_menu()
        if choice == EXIT_OPTION:
            break
        elif choice == ADD_OPTION:
            add_card(catalogue)
        elif choice == SEARCH_OPTION:
            search_edit_card(catalogue)
        elif choice == DELETE_OPTION:
            delete_card(catalogue)
        elif choice == PRINT_OPTION:
            print_catalogue(catalogue)
        elif choice is None:
            # Before end user testing #2, closing the window did not exit the loop.
            pass
    eg.msgbox("Goodbye.", "Exit")

if __name__ == "__main__":
    main()