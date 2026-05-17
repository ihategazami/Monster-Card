"""
Final Assembled Outcome
Monster Card Catalouge

2026 Computer Science Assessment
- 91896 Use advanced programming techniques to develop a computer program
- 91897 Use advanced processes to develop a digital technologies outcome

Lucas Kang (kangl@middleton.school.nz)
"""

# Import EasyGUI so the program can use pop-up boxes instead of console input.
import easygui as eg


def enable_easygui_window_close():
    """
    Change this bundled EasyGUI file so the window X button works.
    """
    def close_active_easygui_box():
        # buttonbox/msgbox normally returns the selected button text.
        # Set this to None so X is treated like closing/cancelling the box.
        eg.__replyButtonText = None

        # enterbox normally stores its text here. Setting it to None makes
        # X behave like pressing Cancel.
        eg.__enterboxText = None

        # End the current EasyGUI Tkinter event loop so the box can close.
        if getattr(eg, "boxRoot", None) is not None:
            eg.boxRoot.quit()

    eg.denyWindowManagerClose = close_active_easygui_box


# -----------------------------------------------------------------------------
# Constants (constants, variables and derived values in place of literals)
# -----------------------------------------------------------------------------

# The minimum and maximum values allowed for each monster stat.
MIN_STAT = 1
MAX_STAT = 25

# The maximum number of characters allowed for a monster name.
# This keeps the catalogue table neat and readable.
MAX_NAME_LENGTH = 15

# The four stat categories required by the assessment specifications.
STATS = ["strength", "speed", "stealth", "cunning"]

# These are the options shown on the main menu.
# The user's selection decides which main function will run.
MAIN_MENU = [
    "Add new monster card",
    "Search / edit monster card",
    "Delete monster card",
    "Print full catalogue",
    "Exit"
]

# These are the options shown when the user edits a card.
# The same edit menu is reused for both existing cards and newly added cards.
EDIT_MENU = [
    "Edit name",
    "Edit strength",
    "Edit speed",
    "Edit stealth",
    "Edit cunning",
    "Finish editing"
]

# These are the options shown when the user prints the full catalogue.
# The user can choose how the monster cards should be sorted.
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

def create_catalogue():
    """
    Create and return the starting monster card catalogue.

    The catalogue is a nested dictionary:
    - The outside dictionary stores each monster name.
    - The inside dictionary stores that monster's stat values.
    """
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


def clean_name(name):
    """
    Clean the monster name entered by the user.

    strip() removes spaces from the start and end.
    split() separates the words and removes extra spaces between words.
    join() puts the words back together with one space.
    title() makes the name look consistent.
    """
    return " ".join(name.strip().split()).title()


def find_card(catalogue, name):
    """
    Find a card in the catalogue without caring about uppercase/lowercase.

    This makes searching more flexible because "stoneling" and "Stoneling"
    will both match the same card.
    """
    name = name.lower()

    # Loop through every card name in the catalogue.
    for card_name in catalogue:
        # Compare both names in lowercase so the search is case-insensitive.
        if card_name.lower() == name:
            return card_name

    # Return None if no matching card is found.
    return None


def format_card(card_name, card_stats):
    """
    Convert one monster card into a readable string.

    This function is reused whenever the program needs to display one card.
    """
    return (
        f"Name: {card_name}\n"
        f"Strength: {card_stats['strength']}\n"
        f"Speed: {card_stats['speed']}\n"
        f"Stealth: {card_stats['stealth']}\n"
        f"Cunning: {card_stats['cunning']}"
    )


def format_catalogue(catalogue, sort_choice="Name (A to Z)"):
    """
    Convert the whole catalogue into a readable table.

    The table is printed to the Python console when the user chooses
    "Print full catalogue". The user can choose the order of the table
    before it is printed.
    """
    # Decide how the catalogue should be sorted.
    # The lambda functions tell sorted() which value to compare.
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
        # Default sorting is alphabetical by monster name.
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

    # Add one row to the table for each monster card.
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
    """
    Ask the user for a valid monster name.

    Validation checks:
    - The name cannot be blank.
    - The name cannot be longer than MAX_NAME_LENGTH characters.
    - The name cannot already exist in the catalogue.
    - When editing a card, the user is allowed to keep the same old name.

    A while loop is used so the user can try again after invalid input.
    """
    while True:
        # Ask the user to enter a monster name using a GUI input box.
        name = eg.enterbox(
            f"Enter the monster name:\nMaximum {MAX_NAME_LENGTH} characters.",
            "Monster Name"
        )

        # If the user presses Cancel, return None safely.
        if name is None:
            return None

        # Clean the name before checking it or storing it.
        name = clean_name(name)

        # Reject blank names.
        if name == "":
            eg.msgbox("Name cannot be blank.", "Invalid Name")
            continue

        # Reject names that are too long.
        if len(name) > MAX_NAME_LENGTH:
            eg.msgbox(
                f"Name cannot be longer than {MAX_NAME_LENGTH} characters.",
                "Invalid Name"
            )
            continue

        # Check whether the card name already exists.
        existing_card = find_card(catalogue, name)

        # Reject duplicate names.
        # old_name is used so a card can keep its current name while editing.
        if existing_card is not None and existing_card != old_name:
            eg.msgbox("That monster card already exists.", "Duplicate Name")
            continue

        # If all checks pass, return the valid name.
        return name


def get_valid_stat(stat_name, current_value=None):
    """
    Ask the user for a valid stat value.

    Validation checks:
    - The value cannot be blank.
    - The value must be a whole number.
    - The value must be between MIN_STAT and MAX_STAT.

    try/except is used so letters, symbols, and decimals do not crash the
    program.
    """
    while True:
        # If the user is editing an existing value, show the current value
        # as the default in the input box.
        default = ""

        if current_value is not None:
            default = str(current_value)

        # Ask the user to enter the value for one stat.
        value = eg.enterbox(
            f"Enter {stat_name}.\n"
            f"It must be a whole number from {MIN_STAT} to {MAX_STAT}.",
            f"Enter {stat_name.title()}",
            default=default
        )

        # If the user presses Cancel, return None safely.
        if value is None:
            return None

        # Remove spaces around the input before checking it.
        value = value.strip()

        # Reject blank values.
        if value == "":
            eg.msgbox("Value cannot be blank.", "Invalid Input")
            continue

        # Try to convert the input into an integer.
        # If it cannot be converted, show an error and ask again.
        try:
            value = int(value)
        except ValueError:
            eg.msgbox("Value must be a whole number.", "Invalid Input")
            continue

        # Check the value is within the allowed range.
        if value < MIN_STAT or value > MAX_STAT:
            eg.msgbox(
                f"Value must be from {MIN_STAT} to {MAX_STAT}.",
                "Invalid Input"
            )
            continue

        # If all checks pass, return the valid integer.
        return value


def get_all_stats():
    """
    Ask the user for all four monster stats.

    Each stat is checked by get_valid_stat().
    The valid values are stored in a dictionary and returned.
    """
    stats = {}

    # Loop through strength, speed, stealth, and cunning.
    for stat_name in STATS:
        value = get_valid_stat(stat_name)

        # If the user cancels while entering any stat, cancel the
        # whole process.
        if value is None:
            return None

        # Store the valid value in the stats dictionary.
        stats[stat_name] = value

    return stats


def get_existing_card(catalogue):
    """
    Let the user choose an existing monster card from the catalogue.

    This is used for search/edit and delete, because both features need the
    user to choose a card that already exists.
    """
    # If the catalogue is empty, there is no card to select.
    if len(catalogue) == 0:
        eg.msgbox(
            "There are no monster cards in the catalogue.",
            "Empty Catalogue"
        )
        return None

    # Show all card names in alphabetical order.
    return eg.choicebox(
        "Choose a monster card:",
        "Select Monster Card",
        sorted(catalogue.keys())
    )


# -----------------------------------------------------------------------------
# Main features
# -----------------------------------------------------------------------------

def edit_card(catalogue, card_name):
    """
    Allow the user to edit a card's name or stat values.

    This function keeps showing the edit menu until the user chooses
    "Finish editing" or closes the box.
    """
    while True:
        # Display the current card details and ask what should be edited.
        choice = eg.buttonbox(
            format_card(card_name, catalogue[card_name]),
            "Edit Card",
            EDIT_MENU
        )

        # Finish editing and return the current card name.
        if choice is None or choice == "Finish editing":
            return card_name

        # If the user edits the name, validate the new name first.
        if choice == "Edit name":
            new_name = get_valid_name(catalogue, old_name=card_name)

            # Only update the dictionary if the user entered a valid new name.
            if new_name is not None:
                # pop() removes the old key and keeps the card stats.
                # The stats are then stored again under the new name.
                catalogue[new_name] = catalogue.pop(card_name)
                card_name = new_name

        else:
            # For stat edits, remove "Edit " from the selected option.
            # Example: "Edit strength" becomes "strength".
            stat_name = choice.replace("Edit ", "")

            # Ask for a new valid stat value.
            new_value = get_valid_stat(
                stat_name,
                catalogue[card_name][stat_name]
            )

            # Only update the stat if the user entered a valid value.
            if new_value is not None:
                catalogue[card_name][stat_name] = new_value


def add_card(catalogue):
    """
    Add a new monster card to the catalogue.

    The card is not added immediately. The details are first stored in
    temporary variables, then shown back to the user for confirmation.
    """
    # Get and validate the new card name.
    card_name = get_valid_name(catalogue)

    # Stop the add process if the user cancels.
    if card_name is None:
        return

    # Get and validate all four stat values.
    card_stats = get_all_stats()

    # Stop the add process if the user cancels while entering stats.
    if card_stats is None:
        return

    while True:
        # Show the new card details before saving them into the real catalogue.
        choice = eg.buttonbox(
            (
                format_card(card_name, card_stats)
                + "\n\nAre these details correct?"
            ),
            "Confirm New Card",
            ["Save card", "Edit details", "Cancel"]
        )

        # Save the card into the catalogue only after the user confirms it.
        if choice == "Save card":
            catalogue[card_name] = card_stats
            eg.msgbox("Card added successfully.", "Card Added")
            return

        # Let the user fix the card before saving it.
        if choice == "Edit details":
            # Make a temporary catalogue so edit_card() can reuse the same edit
            # function before the new card is saved to the real catalogue.
            temp_catalogue = catalogue.copy()
            temp_catalogue[card_name] = card_stats

            # Update the temporary card details.
            card_name = edit_card(temp_catalogue, card_name)
            card_stats = temp_catalogue[card_name]
            continue

        # If the user chooses Cancel or closes the box, do not save the card.
        return


def search_edit_card(catalogue):
    """
    Search for an existing monster card and allow the user to edit it.

    The user first selects a card, then chooses whether to edit it or go back.
    """
    # Get the existing card from the user.
    card_name = get_existing_card(catalogue)

    # If the user cancels, return to the main menu.
    if card_name is None:
        return

    # Display the selected card details and ask if the user wants to edit it.
    choice = eg.buttonbox(
        (
            format_card(card_name, catalogue[card_name])
            + "\n\nDo you want to edit this card?"
        ),
        "Search / Edit Card",
        ["Edit", "Back to menu"]
    )

    # If the user chooses Edit, run the editing function.
    # If the user chooses Back to menu, this function ends naturally.
    if choice == "Edit":
        edit_card(catalogue, card_name)


def delete_card(catalogue):
    """
    Delete a monster card from the catalogue after confirmation.

    The card is only removed if the user chooses "Delete".
    """
    # Get the existing card from the user.
    card_name = get_existing_card(catalogue)

    # If the user cancels, return to the main menu.
    if card_name is None:
        return

    # Show the selected card details before asking for deletion.
    choice = eg.buttonbox(
        format_card(card_name, catalogue[card_name]) + "\n\nDelete this card?",
        "Delete Card",
        ["Delete", "Cancel"]
    )

    # Remove the card from the dictionary only if the user confirms.
    if choice == "Delete":
        catalogue.pop(card_name)
        eg.msgbox("Card deleted successfully.", "Card Deleted")


def print_catalogue(catalogue):
    """
    Print the full catalogue to the Python console.

    The user can choose the order of the catalogue before it is printed.
    This makes the printed catalogue more useful because the cards can be
    compared by different stat values instead of only by name.
    """
    # Ask the user how they want the catalogue to be sorted.
    sort_choice = eg.choicebox(
        "Choose how the catalogue should be sorted:",
        "Sort Catalogue",
        SORT_MENU
    )

    # If the user cancels, return to the main menu without printing.
    if sort_choice is None:
        return

    print()
    print(format_catalogue(catalogue, sort_choice))
    print()

    # Tell the user where the catalogue has been printed.
    eg.msgbox(
        "The full catalogue has been printed to the Python console.",
        "Printed"
    )


def show_main_menu():
    """
    Show the main menu and return the user's choice.

    The returned choice is used in main() to decide which function should run.
    """
    return eg.buttonbox(
        "Choose an option:",
        "Monster Card Catalogue",
        MAIN_MENU
    )


def confirm_exit():
    """
    Ask the user to confirm before exiting the program.

    Returns True if the user chooses Yes.
    Returns False if the user chooses No.
    """
    choice = eg.buttonbox(
        "Are you sure you want to exit?",
        "Confirm Exit",
        ["Yes", "No"]
    )

    return choice == "Yes"


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------

def main():
    """
    Run the full program.

    The while loop keeps showing the main menu until the user chooses Exit
    or clicks the main menu X button, then confirms that they want to leave.
    """
    # Make the EasyGUI window X button work before any pop-up boxes appear.
    enable_easygui_window_close()

    # Create the starting catalogue when the program begins.
    catalogue = create_catalogue()

    # Welcome message shown before the main menu appears.
    eg.msgbox("Welcome to the Monster Card Catalogue.", "Welcome")

    # Keep repeating the menu until break is used.
    while True:
        choice = show_main_menu()

        # If the user chooses Exit or closes the main menu window,
        # ask for confirmation before ending the program.
        if choice is None or choice == "Exit":
            if confirm_exit():
                break

        # Selection statements decide which function runs.
        elif choice == "Add new monster card":
            add_card(catalogue)

        elif choice == "Search / edit monster card":
            search_edit_card(catalogue)

        elif choice == "Delete monster card":
            delete_card(catalogue)

        elif choice == "Print full catalogue":
            print_catalogue(catalogue)

    # This message appears after the loop has ended.
    eg.msgbox("Goodbye.", "Exit")


# This makes sure main() only runs when this file is opened directly.
if __name__ == "__main__":
    main()
