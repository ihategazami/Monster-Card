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
EDIT_MENU = [
    "Edit name",
    "Edit strength",
    "Edit speed",
    "Edit stealth",
    "Edit cunning",
    "Finish editing"
]

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

def format_card(card_name, card_stats):
    """Format one monster card for a GUI message."""
    return (
        f"Name: {card_name}\n"
        f"Strength: {card_stats['strength']}\n"
        f"Speed: {card_stats['speed']}\n"
        f"Stealth: {card_stats['stealth']}\n"
        f"Cunning: {card_stats['cunning']}"
    )

def format_catalogue(catalogue):
    """Format the catalogue alphabetically before the sorting improvement."""
    sorted_names = sorted(catalogue)
    output = (
        "Monster Card Catalogue\n"
        + "Sorted by: Name (A to Z)\n"
        + "-" * 75 + "\n"
        + f"{'Name':<15}{'Strength':<12}{'Speed':<10}{'Stealth':<10}{'Cunning':<10}{'Total':<10}\n"
        + "-" * 75 + "\n"
    )
    for card_name in sorted_names:
        stats = catalogue[card_name]
        total_stats = sum(stats.values())
        output += (
            f"{card_name:<15}"
            f"{stats['strength']:<12}"
            f"{stats['speed']:<10}"
            f"{stats['stealth']:<10}"
            f"{stats['cunning']:<10}"
            f"{total_stats:<10}\n"
        )
    return output

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

def get_existing_card(catalogue):
    """Let the user choose an existing monster card."""
    if len(catalogue) == 0:
        eg.msgbox("There are no monster cards in the catalogue.", "Empty Catalogue")
        return None
    return eg.choicebox("Choose a monster card:", "Select Monster Card", sorted(catalogue.keys()))

# -----------------------------------------------------------------------------
# Main features
# -----------------------------------------------------------------------------
def edit_card(catalogue, card_name):
    """Edit a card. Earlier versions only edited the name; later versions edit stats too."""
    while True:
        choice = eg.buttonbox(format_card(card_name, catalogue[card_name]), "Edit Card", EDIT_MENU)
        if choice is None or choice == "Finish editing":
            return card_name
        if choice == "Edit name":
            new_name = get_valid_name(catalogue, old_name=card_name)
            if new_name is not None:
                catalogue[new_name] = catalogue.pop(card_name)
                card_name = new_name
        else:
            stat_name = choice.replace("Edit ", "")
            new_value = get_valid_stat(stat_name, catalogue[card_name][stat_name])
            if new_value is not None:
                catalogue[card_name][stat_name] = new_value

def add_card(catalogue):
    """Complete add version with confirmation and edit-before-save option."""
    card_name = get_valid_name(catalogue)
    if card_name is None:
        return
    card_stats = get_all_stats()
    if card_stats is None:
        return
    while True:
        choice = eg.buttonbox(format_card(card_name, card_stats) + "\n\nAre these details correct?", "Confirm New Card", ["Save card", "Edit details", "Cancel"])
        if choice == "Save card":
            catalogue[card_name] = card_stats
            eg.msgbox("Card added successfully.", "Card Added")
            return
        if choice == "Edit details":
            temp_catalogue = catalogue.copy()
            temp_catalogue[card_name] = card_stats
            card_name = edit_card(temp_catalogue, card_name)
            card_stats = temp_catalogue[card_name]
            continue
        return

def search_edit_card(catalogue):
    """Search/edit version: select a card and optionally edit it."""
    card_name = get_existing_card(catalogue)
    if card_name is None:
        return
    choice = eg.buttonbox(format_card(card_name, catalogue[card_name]) + "\n\nDo you want to edit this card?", "Search / Edit Card", ["Edit", "Back to menu"])
    if choice == "Edit":
        edit_card(catalogue, card_name)

def delete_card(catalogue):
    """Complete delete version with confirmation and success message."""
    card_name = get_existing_card(catalogue)
    if card_name is None:
        return
    choice = eg.buttonbox(format_card(card_name, catalogue[card_name]) + "\n\nDelete this card?", "Delete Card", ["Delete", "Cancel"])
    if choice == "Delete":
        catalogue.pop(card_name)
        eg.msgbox("Card deleted successfully.", "Card Deleted")

def print_catalogue(catalogue):
    """Selected trial version: normal Python formatting without external libraries."""
    print()
    print(format_catalogue(catalogue))
    print()
    eg.msgbox("The full catalogue has been printed to the Python console.", "Printed")

def show_main_menu():
    """Show the main menu and return the user selection."""
    return eg.buttonbox("Choose an option:", "Monster Card Catalogue", MAIN_MENU)

def confirm_exit():
    """Ask the user to confirm whether they want to exit the program."""
    return eg.buttonbox(
        "Are you sure you want to exit?",
        "Confirm Exit",
        ["Yes", "No"]
    )


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------
def main():
    catalogue = create_catalogue()
    eg.msgbox("Welcome to the Monster Card Catalogue.", "Welcome")
    while True:
        choice = show_main_menu()
        if choice == EXIT_OPTION:
            exit_choice = confirm_exit()
            if exit_choice == "No" or exit_choice is None:
                # If the user does not confirm, the loop continues and the main menu appears again.
                continue
            eg.msgbox("Exit confirmed. Goodbye behaviour will be added next.", "Exit Test")
            continue
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

if __name__ == "__main__":
    main()
