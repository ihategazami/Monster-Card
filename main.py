'''
Final Assembled Outcome
Monster Card Catalogue

2026 Computer Science Assessment
91896 Use advanced programming techniques to develop a computer program
91897 Use advanced processes to develop a digital technologies outcome

Lucas Kang (kangl@middleton.school.nz)
'''

import easygui as eg

# Allows the EasyGUI X button to close the active pop-up safely.
def enable_easygui_window_close():
    def close_active_easygui_box():
        # Treat the X button like Cancel for EasyGUI boxes.
        eg.__replyButtonText = None
        eg.__enterboxText = None

        # Stop the current pop-up event loop if a box is open.
        if getattr(eg, "boxRoot", None) is not None:
            eg.boxRoot.quit()

    eg.denyWindowManagerClose = close_active_easygui_box


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# Allowed range for each monster stat.
MIN_STAT = 1
MAX_STAT = 25

# Maximum length for a monster name.
MAX_NAME_LENGTH = 15

# Stat categories used for every monster card.
STATS = ["strength", "speed", "stealth", "cunning"]

# Main menu options.
MAIN_MENU = [
    "Add new monster card",
    "Search / edit monster card",
    "Delete monster card",
    "Print full catalogue",
    "Exit"
]

# Options shown when editing a card.
EDIT_MENU = [
    "Edit name",
    "Edit strength",
    "Edit speed",
    "Edit stealth",
    "Edit cunning",
    "Finish editing"
]

# Sorting options for printing the full catalogue.
SORT_MENU = [
    "Name (A to Z)",
    "Strength (highest first)",
    "Strength (lowest first)",
    "Speed (highest first)",
    "Speed (lowest first)",
    "Stealth (highest first)",
    "Stealth (lowest first)",
    "Cunning (highest first)",
    "Cunning (lowest first)",
    "Total stats (highest first)",
    "Total stats (lowest first)"
]


# -----------------------------------------------------------------------------
# Catalogue setup and formatting
# -----------------------------------------------------------------------------

# Creates the starting catalogue as a nested dictionary.
def create_catalogue():
    return {
        "Stoneling": {"strength": 7, "speed": 1, "stealth": 25, "cunning": 15},
        "Vexscream": {"strength": 1, "speed": 6, "stealth": 21, "cunning": 19},
        "Dawnmirage": {
            "strength": 5,
            "speed": 15,
            "stealth": 18,
            "cunning": 22
        },
        "Blazegolem": {
            "strength": 15,
            "speed": 20,
            "stealth": 23,
            "cunning": 6
        },
        "Websnake": {"strength": 7, "speed": 15, "stealth": 10, "cunning": 5},
        "Moldvine": {"strength": 21, "speed": 18, "stealth": 14, "cunning": 5},
        "Vortexwing": {
            "strength": 19,
            "speed": 13,
            "stealth": 19,
            "cunning": 2
        },
        "Rotthing": {"strength": 16, "speed": 7, "stealth": 4, "cunning": 12},
        "Froststep": {
            "strength": 14,
            "speed": 14,
            "stealth": 17,
            "cunning": 4
        },
        "Wispghoul": {"strength": 17, "speed": 19, "stealth": 3, "cunning": 2}
    }


# Cleans user-entered names so spacing and capitalisation stay consistent.
def clean_name(name):
    return " ".join(name.strip().split()).title()


# Finds a card name without requiring exact uppercase/lowercase.
def find_card(catalogue, name):
    name = name.lower()

    # Compare the search name with each stored card name.
    for card_name in catalogue:
        if card_name.lower() == name:
            return card_name

    # None means no matching card was found.
    return None


# Formats one monster card for display in a pop-up box.
def format_card(card_name, card_stats):
    return (
        f"Name: {card_name}\n"
        f"Strength: {card_stats['strength']}\n"
        f"Speed: {card_stats['speed']}\n"
        f"Stealth: {card_stats['stealth']}\n"
        f"Cunning: {card_stats['cunning']}"
    )


# Formats the full catalogue as a table, using the selected sort order.
def format_catalogue(catalogue, sort_choice="Name (A to Z)"):
    # Choose the sorting rule based on the user's selection.
    if sort_choice == "Strength (highest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["strength"],
            reverse=True
        )

    elif sort_choice == "Strength (lowest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["strength"]
        )

    elif sort_choice == "Speed (highest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["speed"],
            reverse=True
        )

    elif sort_choice == "Speed (lowest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["speed"]
        )

    elif sort_choice == "Stealth (highest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["stealth"],
            reverse=True
        )

    elif sort_choice == "Stealth (lowest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["stealth"]
        )

    elif sort_choice == "Cunning (highest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["cunning"],
            reverse=True
        )

    elif sort_choice == "Cunning (lowest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: catalogue[name]["cunning"]
        )

    elif sort_choice == "Total stats (highest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: sum(catalogue[name].values()),
            reverse=True
        )

    elif sort_choice == "Total stats (lowest first)":
        sorted_names = sorted(
            catalogue,
            key=lambda name: sum(catalogue[name].values())
        )

    else:
        sorted_names = sorted(catalogue)

    # Create the table title and column headings.
    headings = (
        f"{'Name':<15}"
        f"{'Strength':<12}"
        f"{'Speed':<10}"
        f"{'Stealth':<10}"
        f"{'Cunning':<10}"
        f"{'Total':<10}"
    )

    output = (
        "Monster Card Catalogue\n"
        + f"Sorted by: {sort_choice}\n"
        + "-" * 75 + "\n"
        + headings + "\n"
        + "-" * 75 + "\n"
    )

    # Add each monster card as one row in the table.
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

# Gets a valid monster name from the user.
def get_valid_name(catalogue, old_name=None):
    while True:
        name = eg.enterbox(
            f"Enter the monster name:\nMaximum {MAX_NAME_LENGTH} characters.",
            "Monster Name"
        )

        # Cancel stops the current action safely.
        if name is None:
            return None

        name = clean_name(name)

        # Check the name is not blank or too long.
        if name == "":
            eg.msgbox("Name cannot be blank.", "Invalid Name")
            continue

        if len(name) > MAX_NAME_LENGTH:
            eg.msgbox(
                f"Name cannot be longer than {MAX_NAME_LENGTH} characters.",
                "Invalid Name"
            )
            continue

        # Check for duplicate names, except when keeping the current edit name.
        existing_card = find_card(catalogue, name)

        if existing_card is not None and existing_card != old_name:
            eg.msgbox("That monster card already exists.", "Duplicate Name")
            continue

        return name


# Gets a valid stat value from the user.
def get_valid_stat(stat_name, current_value=None):
    while True:
        # Show the current value when editing an existing stat.
        default = ""

        if current_value is not None:
            default = str(current_value)

        value = eg.enterbox(
            f"Enter {stat_name}.\n"
            f"It must be a whole number from {MIN_STAT} to {MAX_STAT}.",
            f"Enter {stat_name.title()}",
            default=default
        )

        # Cancel stops the current action safely.
        if value is None:
            return None

        value = value.strip()

        if value == "":
            eg.msgbox("Value cannot be blank.", "Invalid Input")
            continue

        # Convert the input to an integer; reject non-whole-number input.
        try:
            value = int(value)
        except ValueError:
            eg.msgbox("Value must be a whole number.", "Invalid Input")
            continue

        # Check the stat is inside the allowed range.
        if value < MIN_STAT or value > MAX_STAT:
            eg.msgbox(
                f"Value must be from {MIN_STAT} to {MAX_STAT}.",
                "Invalid Input"
            )
            continue

        return value


# Gets all four stat values and stores them in a dictionary.
def get_all_stats():
    stats = {}

    for stat_name in STATS:
        value = get_valid_stat(stat_name)

        # Cancel any stat entry to cancel the whole card creation.
        if value is None:
            return None

        stats[stat_name] = value

    return stats


# Lets the user choose a card that already exists in the catalogue.
def get_existing_card(catalogue):
    # Do not open a choice box if there are no cards to choose from.
    if len(catalogue) == 0:
        eg.msgbox(
            "There are no monster cards in the catalogue.",
            "Empty Catalogue"
        )
        return None

    return eg.choicebox(
        "Choose a monster card:",
        "Select Monster Card",
        sorted(catalogue.keys())
    )


# -----------------------------------------------------------------------------
# Main features
# -----------------------------------------------------------------------------

# Lets the user edit a card's name or stats.
def edit_card(catalogue, card_name):
    while True:
        choice = eg.buttonbox(
            format_card(card_name, catalogue[card_name]),
            "Edit Card",
            EDIT_MENU
        )

        # Finish editing if the user selects Finish or closes the box.
        if choice is None or choice == "Finish editing":
            return card_name

        if choice == "Edit name":
            new_name = get_valid_name(catalogue, old_name=card_name)

            # Rename the dictionary key while keeping the same stat values.
            if new_name is not None:
                catalogue[new_name] = catalogue.pop(card_name)
                card_name = new_name

        else:
            # Turn menu text such as "Edit strength" into "strength".
            stat_name = choice.replace("Edit ", "")

            new_value = get_valid_stat(
                stat_name,
                catalogue[card_name][stat_name]
            )

            if new_value is not None:
                catalogue[card_name][stat_name] = new_value


# Adds a new monster card after validation and confirmation.
def add_card(catalogue):
    card_name = get_valid_name(catalogue)

    if card_name is None:
        return

    card_stats = get_all_stats()

    if card_stats is None:
        return

    while True:
        # Show the new card before saving it permanently.
        choice = eg.buttonbox(
            (
                format_card(card_name, card_stats)
                + "\n\nAre these details correct?"
            ),
            "Confirm New Card",
            ["Save card", "Edit details", "Cancel"]
        )

        if choice == "Save card":
            catalogue[card_name] = card_stats
            eg.msgbox("Card added successfully.", "Card Added")
            return

        if choice == "Edit details":
            # Use a temporary catalogue so edit_card() can edit before saving.
            temp_catalogue = catalogue.copy()
            temp_catalogue[card_name] = card_stats

            card_name = edit_card(temp_catalogue, card_name)
            card_stats = temp_catalogue[card_name]
            continue

        return


# Finds a card and gives the user the option to edit it.
def search_edit_card(catalogue):
    card_name = get_existing_card(catalogue)

    if card_name is None:
        return

    choice = eg.buttonbox(
        (
            format_card(card_name, catalogue[card_name])
            + "\n\nDo you want to edit this card?"
        ),
        "Search / Edit Card",
        ["Edit", "Back to menu"]
    )

    if choice == "Edit":
        edit_card(catalogue, card_name)


# Deletes a card after the user confirms the action.
def delete_card(catalogue):
    card_name = get_existing_card(catalogue)

    if card_name is None:
        return

    choice = eg.buttonbox(
        format_card(card_name, catalogue[card_name]) + "\n\nDelete this card?",
        "Delete Card",
        ["Delete", "Cancel"]
    )

    if choice == "Delete":
        catalogue.pop(card_name)
        eg.msgbox("Card deleted successfully.", "Card Deleted")


# Prints the full catalogue to the Python console.
def print_catalogue(catalogue):
    sort_choice = eg.choicebox(
        "Choose how the catalogue should be sorted:",
        "Sort Catalogue",
        SORT_MENU
    )

    if sort_choice is None:
        return

    print()
    print(format_catalogue(catalogue, sort_choice))
    print()

    eg.msgbox(
        "The full catalogue has been printed to the Python console.",
        "Printed"
    )


# Shows the main menu and returns the selected option.
def show_main_menu():
    return eg.buttonbox(
        "Choose an option:",
        "Monster Card Catalogue",
        MAIN_MENU
    )


# Confirms whether the user wants to exit the program.
def confirm_exit():
    choice = eg.buttonbox(
        "Are you sure you want to exit?",
        "Confirm Exit",
        ["Yes", "No"]
    )

    return choice == "Yes"


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------

# Runs the full program.
def main():
    # Enable the EasyGUI X button before any windows are shown.
    enable_easygui_window_close()

    catalogue = create_catalogue()

    eg.msgbox("Welcome to the Monster Card Catalogue.", "Welcome")

    # Keep showing the menu until the user confirms Exit.
    while True:
        choice = show_main_menu()

        if choice is None or choice == "Exit":
            if confirm_exit():
                break

        elif choice == "Add new monster card":
            add_card(catalogue)

        elif choice == "Search / edit monster card":
            search_edit_card(catalogue)

        elif choice == "Delete monster card":
            delete_card(catalogue)

        elif choice == "Print full catalogue":
            print_catalogue(catalogue)

    eg.msgbox("Goodbye.", "Exit")


# Run main() only when this file is opened directly.
if __name__ == "__main__":
    main()
