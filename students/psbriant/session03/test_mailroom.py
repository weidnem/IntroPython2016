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


# ==============================================================================
def main():



if __name__ == '__main__':
    main()
