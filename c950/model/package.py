"""This module provides the Package class to store package information."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import enum
import dataclasses
import time
import c950


class DeliveryStatus(enum.Enum):
    """Enum dataclass to represent the delivery status of a package.

    Attributes:
        __order__ (str): The order of the enum constants.
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


@dataclasses.dataclass
class Package:
    """This dataclass defines a package instance with its information.

    Attributes:
        id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        weight_kilo (int): The package weight in kilos.
        delivery_deadline (time): The package delivery deadline.
        special_notes (str): The package special notes.
        delivery_status (DeliveryStatus): The package delivery status.
        truck (truck): The package delivery truck.
        delivery_time (time): The package delivery time.

    Returns:
        Package: A Package class instance.
    """

    id: int
    address: str
    city: str
    state: str
    zip: str
    weight_kilo: int
    delivery_deadline: time
    special_notes: str
    delivery_status: DeliveryStatus
    truck: c950.model.truck.Truck
    delivery_time: time
