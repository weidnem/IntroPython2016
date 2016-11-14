"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session: 03
Assignment: Mailroom Tests

Description:
Tests for mailroom
"""

# -------------------------------Imports----------------------------------------
import mailroom

# -------------------------------Functions--------------------------------------


def test_list_donors():
    """
    Verifies content of the list_donors output.
    """
    listing = mailroom.list_donors
    assert listing.startswith('Donors:\n')
    assert "Sheryl Sandberg" in listing
    assert "Satya Nadella" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """
    Checks to see if a donor exists but with varied whitespace and cases.
    """
    assert mailroom.find_donor("satYa nADella ", mailroom.donor_dict)


# ==============================================================================
def main():
    """

    """


if __name__ == '__main__':
    main()
