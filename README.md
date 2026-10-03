# Hands-On Lab — Shopping List Manager

This assignment practices Python lists, loops, indexing, conditions, and list methods.

## Files

- `list_warmup.py` — Creates and modifies a list of fruits using indexing, `append()`, `remove()`, and `len()`.
- `shopping_list.py` — Provides an interactive shopping list manager where users can add, remove, show, and finish their shopping list.
- `list_report.py` — Prints numbered shopping items, counts items with more than four letters, and finds the longest item.

## Why check `in` before `.remove()`?

Checking whether an item is in the list before using `.remove()` is safer because `.remove()` causes an error if the item does not exist. Using `in` first allows the program to show a helpful message instead of crashing.