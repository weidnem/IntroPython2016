"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
LAB: Dictionaries

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------

# ==============================================================================


def main():
    """

    """
    dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(dict1)
    del dict1["cake"]
    print(dict1)
    dict1["fruit"] = "Mango"
    print(dict1.keys())
    print(dict1.values())
    print("cake" in dict1)
    print("Mango" in dict1.values())



if __name__ == '__main__':
    main()
