import easygui as eg

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
MIN_STAT = 1
MAX_STAT = 25
STATS = ["strength", "speed", "stealth", "cunning"]

ADD_OPTION = 'Add new monster card'
SEARCH_OPTION = 'Search / edit monster card'
DELETE_OPTION = 'Delete monster card'
PRINT_OPTION = 'Print full catalogue'
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

def clean_name(name):
    """Clean spacing and capitalisation in a monster name."""
    return " ".join(name.strip().split()).title()

def find_card(catalogue, name):
    """Find a card without caring about uppercase/lowercase."""
    name = name.lower()
    for card_name in catalogue:
        if card_name.lower() == name:
            return card_name
    return None

# -----------------------------------------------------------------------------
# Validation functions
# -----------------------------------------------------------------------------
def get_valid_name(catalogue, old_name=None):
    """Ask the user for a monster name and validate it as development progressed."""
    while True:
        name = eg.enterbox('Enter the monster name:', "Monster Name")
        if name is None:
            return None
        name = clean_name(name)
        if name == "":
            eg.msgbox("Name cannot be blank.", "Invalid Name")
            continue
        existing_card = find_card(catalogue, name)
        if existing_card is not None and existing_card != old_name:
            eg.msgbox("That monster card already exists.", "Duplicate Name")
            continue
        return name

def get_valid_stat(stat_name, current_value=None):
    """Ask for a stat and validate blank, integer and range errors."""
    while True:
        default = ""
        if current_value is not None:
            default = str(current_value)
        value = eg.enterbox(
            f"Enter {stat_name}.\nIt must be a whole number from {MIN_STAT} to {MAX_STAT}.",
            f"Enter {stat_name.title()}",
            default=default
        )
        if value is None:
            return None
        value = value.strip()
        if value == "":
            eg.msgbox("Value cannot be blank.", "Invalid Input")
            continue
        try:
            value = int(value)
        except ValueError:
            eg.msgbox("Value must be a whole number.", "Invalid Input")
            continue
        if value < MIN_STAT or value > MAX_STAT:
            eg.msgbox(f"Value must be from {MIN_STAT} to {MAX_STAT}.", "Invalid Input")
            continue
        return value

def get_all_stats():
    """Ask the user for strength, speed, stealth and cunning."""
    stats = {}
    for stat_name in STATS:
        value = get_valid_stat(stat_name)
        if value is None:
            return None
        stats[stat_name] = value
    return stats

# -----------------------------------------------------------------------------
# Main features
# -----------------------------------------------------------------------------
def add_card(catalogue):
    """Add version that collects the name and all four stats."""
    card_name = get_valid_name(catalogue)
    if card_name is None:
        return
    card_stats = get_all_stats()
    if card_stats is None:
        return
    catalogue[card_name] = card_stats
    eg.msgbox("Card added successfully.", "Card Added")

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
