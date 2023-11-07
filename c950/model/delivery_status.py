#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from enum import Enum


class DeliveryStatus(Enum):
    """Enum of frozen dataclass to represent the delivery status of a package.

    Attributes:
        NOT_AVAILABLE: Enum constant for package not available
        AT_HUB: Enum constant for package at hub
        EN_ROUTE: Enum constant for package en route
        DELIVERED: Enum constant for package delivered

    Returns:
        DeliveryStatus: A DeliveryStatus Enum class instance.
    """

    NOT_AVAILABLE = 0
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3

    @staticmethod
    def get_delivery_status(id: int) -> Enum:
        """Returns a DeliveryStatus Enum constant from an id.
        Raises a ValueError if the id is invalid.

        Args:
            id (int): The id of the DeliveryStatus Enum constant to return.

        Returns:
            Enum: The DeliveryStatus Enum constant with the specified id.
        """

        if id == 0:
            return DeliveryStatus.NOT_AVAILABLE
        elif id == 1:
            return DeliveryStatus.AT_HUB
        elif id == 2:
            return DeliveryStatus.EN_ROUTE
        elif id == 3:
            return DeliveryStatus.DELIVERED
        else:
            raise ValueError("Invalid id for DeliveryStatus")
