#!/usr/bin/env python3

"""Generate and display list of fruits"""
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruits:
    print(fruit)

"""Prompt user for another fruit and add to list"""
new_fruit = input("Please tell me which fruit I should add to the list > ")
fruits.append(new_fruit)
for fruit in fruits:
    print(fruit)