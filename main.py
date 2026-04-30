import easygui as eg

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
MIN_STAT = 1
MAX_STAT = 25
STATS = ["strength", "speed", "stealth", "cunning"]

# -----------------------------------------------------------------------------
# Catalogue setup and formatting
# -----------------------------------------------------------------------------
def create_catalogue():
    """Create a small test catalogue while the data structure is being developed."""
    return {
        "Stoneling": {"strength": 7, "speed": 1, "stealth": 25, "cunning": 15},
        "Vexscream": {"strength": 1, "speed": 6, "stealth": 21, "cunning": 19}
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

# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------
def main():
    catalogue = create_catalogue()
    eg.msgbox("Welcome to the Monster Card Catalogue.", "Welcome")
    eg.msgbox("Starting version complete.", "Development Version")

if __name__ == "__main__":
    main()
