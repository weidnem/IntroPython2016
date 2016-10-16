"""
Name: Paul Briant
Date: 10/18/16
Class: Introduction to Python
Session: 03
Assignment String Lab

Description:


"""
# -------------------------------Functions--------------------------------------


def str_format1(num_list):
    """

    """
    print("File {:03d}: \t{:.2f}, {:.0e}".format(num_list[0], num_list[1],
          num_list[2]))


def main():
    """

    """
    num_list = [2, 123.4567, 10000]
    str_format1(num_list)
    str_format1([10, 1.999, 100])
    str_format1([100, 0.117, 567])

if __name__ == '__main__':
    main()
