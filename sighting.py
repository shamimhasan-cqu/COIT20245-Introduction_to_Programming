# sighting.py


def display_menu():
    """
    Display the help menu with available commands.
    """
    menu = (
        "\n+----------------------------------------------+\n"
        "|                 Help Menu                    |\n"
        "+----------------------------------------------+\n"
        "| The following commands are recognised:       |\n"
        "|                                              |\n"
        "|  Display help menu      : help               |\n"
        "|  Display available cities: cities            |\n"
        "|  Display species in city: species <city>     |\n"
        "|  Display animal sightings in a city:         |\n"
        "|    wildlife> sightings <city> <taxonid>      |\n"
        "|  Exit the application   : exit               |\n"
        "+----------------------------------------------+\n"
    )
    print(menu)


def search_species(city):
    """
    Stub function to search for species in a given city.

    Args:
        city (str): The name of the city.

    Returns:
        list: A list of species dictionaries.
    """
    species_data = {
        "cairns": [
            {
                "Species": {
                    "TaxonID": 1039,
                    "AcceptedCommonName": "dolphin",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2045,
                    "AcceptedCommonName": "whipsnake",
                    "PestStatus": "Venomous",
                }
            },
            {
                "Species": {
                    "TaxonID": 1056,
                    "AcceptedCommonName": "koala",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2077,
                    "AcceptedCommonName": "redback spider",
                    "PestStatus": "Venomous",
                }
            },
        ],
        "brisbane": [
            {
                "Species": {
                    "TaxonID": 1010,
                    "AcceptedCommonName": "kangaroo",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 1045,
                    "AcceptedCommonName": "platypus",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2090,
                    "AcceptedCommonName": "brown snake",
                    "PestStatus": "Venomous",
                }
            },
            {
                "Species": {
                    "TaxonID": 2100,
                    "AcceptedCommonName": "funnel-web spider",
                    "PestStatus": "Venomous",
                }
            },
        ],
        "sydney": [
            {
                "Species": {
                    "TaxonID": 1020,
                    "AcceptedCommonName": "kookaburra",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2065,
                    "AcceptedCommonName": "tasmanian devil",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2080,
                    "AcceptedCommonName": "blue-ringed octopus",
                    "PestStatus": "Venomous",
                }
            },
            {
                "Species": {
                    "TaxonID": 2050,
                    "AcceptedCommonName": "box jellyfish",
                    "PestStatus": "Venomous",
                }
            },
        ],
        "melbourne": [
            {
                "Species": {
                    "TaxonID": 1035,
                    "AcceptedCommonName": "emu",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2025,
                    "AcceptedCommonName": "eastern brown snake",
                    "PestStatus": "Venomous",
                }
            },
            {
                "Species": {
                    "TaxonID": 1090,
                    "AcceptedCommonName": "wombat",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2055,
                    "AcceptedCommonName": "tiger snake",
                    "PestStatus": "Venomous",
                }
            },
        ],
        "perth": [
            {
                "Species": {
                    "TaxonID": 1040,
                    "AcceptedCommonName": "quokka",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2060,
                    "AcceptedCommonName": "dugong",
                    "PestStatus": "Nil",
                }
            },
            {
                "Species": {
                    "TaxonID": 2095,
                    "AcceptedCommonName": "western brown snake",
                    "PestStatus": "Venomous",
                }
            },
            {
                "Species": {
                    "TaxonID": 2110,
                    "AcceptedCommonName": "redback spider",
                    "PestStatus": "Venomous",
                }
            },
        ],
    }
    return species_data.get(city.lower(), [])


def display_species(species_list):
    """
    Display a list of species to the screen.

    Args:
        species_list (list): A list of species dictionaries.
    """
    if not species_list:
        message = "No species found for the specified city."
        border_length = len(message) + 2
        border = "+" + "-" * border_length + "+"
        print(f"\n{border}")
        print(f"| {message} |")
        print(f"{border}\n")
        return

    max_species_length = max(
        len(species["Species"]["AcceptedCommonName"]) for species in species_list
    )
    max_status_length = max(len("Non-venomous"), len("Venomous"))
    max_taxonid_length = len("TaxonID")
    total_length = (
        max_species_length + max_status_length + max_taxonid_length + 14
    )  # Adding spaces and separators
    border = "+" + "-" * (total_length + 2) + "+"

    print(f"\n{border}")
    header = " Species Found in City "
    print("|" + header.center(total_length + 2) + "|")
    print(f"{border}")
    sub_header = (
        "Species".ljust(max_species_length + 2)
        + "Status".center(max_status_length + 6)
        + "TaxonID".rjust(max_taxonid_length + 4)
    )
    print("| " + sub_header.ljust(total_length) + " |")
    print(f"{border}")

    for species in species_list:
        common_name = species["Species"]["AcceptedCommonName"]
        pest_status = (
            "Venomous"
            if species["Species"]["PestStatus"] == "Venomous"
            else "Non-venomous"
        )
        taxonid = species["Species"]["TaxonID"]
        line = (
            f"{common_name.capitalize()}".ljust(max_species_length + 2)
            + f"{pest_status}".center(max_status_length + 6)
            + f"{taxonid}".rjust(max_taxonid_length + 4)
        )
        print("| " + line.ljust(total_length) + " |")
    print(f"{border}\n")


def display_cities():
    """
    Display a list of available cities.
    """
    cities = ["Cairns", "Brisbane", "Sydney", "Melbourne", "Perth"]
    print("\n+----------------------------------------------+")
    print("|               Available Cities               |")
    print("+----------------------------------------------+")
    for city in cities:
        print(f"| {city:<44} |")
    print("+----------------------------------------------+\n")


def search_sightings(taxonid, city):
    """
    Stub function to search for sightings of a particular species in a given city.

    Args:
        taxonid (int): The taxon ID of the species.
        city (str): The name of the city.

    Returns:
        list: A list of sightings dictionaries.
    """
    species = search_species(city)
    if not any(s["Species"]["TaxonID"] == taxonid for s in species):
        return None

    return [
        {
            "properties": {
                "TaxonID": taxonid,
                "StartDate": "1999-11-15",
                "LocalityDetails": "Tinaroo",
                "SiteCode": "INCIDENTAL",
            }
        }
    ]


def display_sightings(sightings):
    """
    Display a list of animal sightings to the screen.

    Args:
        sightings (list): A list of sightings dictionaries.
    """
    if not sightings:
        print("\n+-------------------------------------------------+")
        print("| No sightings found for the specified criteria.  |")
        print("+-------------------------------------------------+\n")
        return

    max_date_length = len("Start Date")
    max_location_length = max(
        len(sighting["properties"]["LocalityDetails"]) for sighting in sightings
    )
    max_taxonid_length = len("TaxonID")
    max_sitecode_length = len("SiteCode")
    total_length = (
        max_date_length
        + max_location_length
        + max_taxonid_length
        + max_sitecode_length
        + 20
    )
    border = "+" + "-" * (total_length + 2) + "+"

    print(f"\n{border}")
    header = " Animal Sightings "
    print("|" + header.center(total_length + 2) + "|")
    print(f"{border}")
    sub_header = (
        "Start Date".ljust(max_date_length + 2)
        + "Location".center(max_location_length + 6)
        + "TaxonID".center(max_taxonid_length + 6)
        + "SiteCode".rjust(max_sitecode_length + 4)
    )
    print("| " + sub_header.ljust(total_length) + " |")
    print(f"{border}")

    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        location = sighting["properties"]["LocalityDetails"]
        taxonid = sighting["properties"]["TaxonID"]
        sitecode = sighting["properties"]["SiteCode"]
        line = (
            f"{start_date}".ljust(max_date_length + 2)
            + f"{location}".center(max_location_length + 6)
            + f"{taxonid}".center(max_taxonid_length + 6)
            + f"{sitecode}".rjust(max_sitecode_length + 4)
        )
        print("| " + line.ljust(total_length) + " |")
    print(f"{border}\n")


def main():
    """
    Main function to display the help menu and prompt user commands.
    """
    print("\n+---------------------------------------------------------+")
    print("|    Welcome to the Wildlife Sightings Application!       |")
    print("+---------------------------------------------------------+")
    display_menu()  # Display the help menu initially

    while True:
        command = (
            input("\nEnter command (type 'help' for menu): wildlife> ").strip().lower()
        )

        if command == "help":
            display_menu()
        elif command == "exit":
            print("\n+----------------------------------------------+")
            print("| Exiting the application. Goodbye!            |")
            print("+----------------------------------------------+\n")
            break
        elif command == "cities":
            display_cities()
        elif command.startswith("species "):
            city = command.split(" ", 1)[1]
            species_list = search_species(city)
            display_species(species_list)
        elif command.startswith("sightings "):
            parts = command.split(" ")
            if len(parts) == 3:
                city = parts[1]
                taxonid = int(parts[2])
                sightings = search_sightings(taxonid, city)
                if sightings is None:
                    print("\n+----------------------------------------------+")
                    print("| Error: No species with the specified taxonid |")
                    print("| found in the specified city.                 |")
                    print("+----------------------------------------------+\n")
                else:
                    display_sightings(sightings)
            else:
                error_message1 = "Error: Invalid command format."
                error_message2 = "Please use the format 'sightings <city> <taxonid>'."
                max_length = max(len(error_message1), len(error_message2))
                border = "+" + "-" * (max_length + 2) + "+"
                print(f"\n{border}")
                print(f"| {error_message1.ljust(max_length)} |")
                print(f"| {error_message2.ljust(max_length)} |")
                print(f"{border}\n")
        else:
            command_error = f"Error: Unrecognized command '{command}'."
            help_prompt = "Please type 'help' for available commands."
            max_length = max(len(command_error), len(help_prompt))
            border = "+" + "-" * (max_length + 2) + "+"
            print(f"\n{border}")
            print(f"| {command_error.ljust(max_length)} |")
            print(f"| {help_prompt.ljust(max_length)} |")
            print(f"{border}\n")


if __name__ == "__main__":
    main()
