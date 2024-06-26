import datetime

# import data_structures_and_algorithms_ii.hash_table


class Package:
    """This dataclass represents a package instance with its information which has not had any data mutated."""

    def __init__(
        self,
        id: int,
        address: int,
        city: str,
        state: str,
        zip: str,
        delivery_deadline: str,
        weight_kilo: int,
        special_notes: str,
        delivery_status: str = None,
        truck_id: int = None,
        departure_time: datetime.time = None,
        delivery_time: datetime.time = None,
    ):
        """
        Initializes a Package class instance. Converts the string values to the appropriate data types.

        Args:
            id (int): The package id.
            address (int): The package address.
            city (str): The package city.
            state (str): The package state.
            zip (str): The package zip code.
            delivery_deadline (datetime.time): The package delivery deadline.
            weight_kilo (int): The package weight in kilos.
            special_notes (str): The package special notes.
            delivery_status (str): The package delivery status.
            truck_id (int): The truck id.
            delivery_time (datetime.time): The package delivery time.
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.delivery_time = delivery_time

    def update_delivery_status(self, delivery_status: str) -> bool:
        """Updates the delivery status of the package. If a delivery time is provided, it will also update the
        delivery time of the package.

        Args:
            delivery_status (str): The delivery status of the package.

        Returns:
            bool: True if the delivery status was updated successfully. False if the delivery status was not updated
                successfully.
        """

        # Check that the delivery_status is a valid value.
        if delivery_status == (
            "Not Available" or "At Hub" or "En Route" or "Delivered"
        ):
            self.delivery_status = delivery_status
            print(
                f"Package {self.id} delivery status updated to {self.delivery_status}.\n"
            )
            return True
        else:
            raise ValueError(
                "Invalid delivery status value. Please enter either one of the following:\n",
                "'Not Available'\n'At Hub'\n'En Route'\n'Delivered'\n",
            )

    def update_address(self, correct_address_id: int):
        """
        Updates the address field to a corrected one.

        Args:
            correct_address_id (int): The correct address to replace existing address with.

        Returns:
            None
        """
        self.address = correct_address_id

    def load_package(self, truck_id: int):
        """Loads the package onto the truck. Updates the truck_id attribute.

        Args:
            truck_id (int): The ID of the truck that will carry the package.
        """
        self.truck_id = truck_id
        self.delivery_status = "At Hub"
        print(f"Package {self.id} loaded onto truck {self.truck_id}.\n")

    def package_departure(self, departure_time: datetime.time):
        """Sends the truck to deliver the package. Updates departure_time and delivery_status attributes.

        Args:
            departure_time (datetime.time): The time that the truck will depart to deliver the package.
        """
        self.departure_time = departure_time
        self.delivery_status = "En Route"
        print(
            f"Truck {self.truck_id} sent to deliver package {self.id} at {self.departure_time}.\n"
        )

    def deliver_package(self, delivery_time: datetime.time):
        """Delivers the package. Updates the delivery_status and delivery_time attributes.

        Args:
            delivery_time (datetime.time): The time that the package was delivered. Defaults to the current time.
        """
        self.delivery_status = "Delivered"
        self.delivery_time = delivery_time
        print(f"Package {self.id} delivered at {self.delivery_time}.\n")

    def _str(self):
        return (
            f"Package ID: {self.id}\n"
            f"Address: {self.address.__str__()}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip: {self.zip}\n"
            f"Delivery Deadline: {self.delivery_deadline}\n"
            f"Weight: {self.weight_kilo} kilos\n"
            f"Special Notes: {self.special_notes}\n"
            f"Delivery Status: {self.delivery_status}\n"
            f"Truck ID: {self.truck_id}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Delivery Time: {self.delivery_time}\n"
        )

    def __repr__(self):
        return f"Package ID: {self.id} Address: {self.address}\n"


# def get_package_ids_with_address_id(
#     address_id: int,
#     packages: data_structures_and_algorithms_ii.hash_table.HashTable = data_structures_and_algorithms_ii.packages,
# ) -> list:
#
#     package_ids_with_matching_addresses = []
#     package_tuples = packages.get_all()
#     temp_list = list(package_tuples)
#     package_list = []
#     for i in package_tuples:
#         package_list.append(list(i))
#
#     for package in package_list:
#         if package[1].address == address_id:
#             package_ids_with_matching_addresses.append(package[1].id)
#
#     return package_ids_with_matching_addresses
