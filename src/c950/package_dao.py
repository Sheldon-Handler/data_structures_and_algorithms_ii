"""This module contains the PackageDAO class to store Package class in
"package" table of "identifier.sqlite" database."""

#  MIT License
#
#  Copyright (c) <year> <copyright holders>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Import sqlite3
import sqlite3

# Import Package from package
from package import Package

# Create connection to "identifier.sqlite" database
packages = sqlite3.connect("../data/identifier.sqlite")
# Set row_factory to sqlite3.Row
packages.row_factory = sqlite3.Row
# Set row_factory in cursor() to sqlite3.Row
packages.cursor().row_factory = sqlite3.Row

# Create 'package' table in 'identifier.sqlite' database if it does not exist.
packages.execute(
    "CREATE TABLE IF NOT EXISTS package (\n"
    "                              package_id INT PRIMARY KEY,\n"
    "                              address VARCHAR,\n"
    "                              city VARCHAR,\n"
    "                              state VARCHAR,\n"
    "                              zip VARCHAR,\n"
    "                              weight INT,\n"
    "                              deadline VARCHAR,\n"
    "                              note VARCHAR,\n"
    "                              status VARCHAR)"
)
# Commit changes to 'identifier.sqlite' database
packages.commit()

packages.row_factory(__cursor=packages.cursor(), __row=Package.package_id)


# PackageDAO class
class PackageDAO:
    """PackageDAO class to store Package class in 'package' table of
    'identifier.sqlite' database.

    Attributes:
        packages (sqlite3.Connection): The connection to the "identifier.sqlite" database.
    """

    def __init__(self):
        """Initializes the Packages class."""

        self.packages = sqlite3.connect("identifier.sqlite")
        self.packages.row_factory = sqlite3.Row
        self.packages.cursor().row_factory = sqlite3.Row

        self.packages.cursor().executescript(
            "CREATE TABLE IF NOT EXISTS package (\n"
            "                              package_id INT PRIMARY KEY,\n"
            "                              address VARCHAR,\n"
            "                              city VARCHAR,\n"
            "                              state VARCHAR,\n"
            "                              zip VARCHAR,\n"
            "                              weight INT,\n"
            "                              deadline VARCHAR,\n"
            "                              note VARCHAR,\n"
            "                              status VARCHAR)"
        )

    def get_packages(self) -> list:
        """Returns all packages from the 'package' table in
        'identifier.sqlite'."""

        self.packages.row_factory = sqlite3.Row

        return self.packages.cursor().execute("SELECT * FROM package").fetchall()

    def add_package(self, package: Package):
        """Adds a Package to the package table in packages.db."""

        try:
            self.cursor.execute(
                "INSERT INTO package VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    package.package_id,
                    package.address,
                    package.city,
                    package.state,
                    package.zip,
                    package.weight_kilo,
                    package.delivery_deadline,
                    package.special_notes,
                    package.status,
                ),
            )
            self.packages.commit()
        except sqlite3.IntegrityError as e:
            raise e

    def remove_package(self, package_id: int):
        """Removes a Package from the "package" table in the
        "identifier.sqlite" database.

        Args:
            self (PackageDAO): The PackageDAO object self-reference.
            package_id (int): The package ID of the package to remove.

        Returns:
            None
        """

        # Remove with given package ID from 'package' table in 'identifier.sqlite' database.
        try:
            self.packages.execute(
                "DELETE FROM package WHERE package_id = ?", package_id
            )
            self.packages.commit()
        except sqlite3.Error as e:
            raise e

    def update_package(self, package: Package):
        """Updates a Package in the packages table in packages.db.
        Args:
            self (PackageDAO): The PackageDAO object self-reference.
            package (Package): The Package object to update.

        Returns:
            None
        """

        # Update package in database with given package object values
        self.packages.execute(
            "UPDATE package SET address = ?, city = ?, state = ?, zip = ?, deadline = ?, "
            "weight = ?, note = ?, status = ? WHERE package_id = ?",
            (
                package.address,
                package.city,
                package.state,
                package.zip,
                package.delivery_deadline,
                package.weight_kilo,
                package.special_notes,
                package.status,
                package.package_id,
            ),
        )
        self.packages.commit()
