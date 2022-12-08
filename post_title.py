'''
Script to convert the title of a Jekyll blog post to a valid filename format.
On MacOS, copies the result to clipboard.
'''

import datetime
import os

# Get the current date
current_date = datetime.date.today()

# Get the title of the post
title = input("Enter the title of the post: ")

# Convert the title to lowercase and replace spaces with dashes
filename = title.lower().replace(" ", "-")

# Append the date to the filename
filename = f"{current_date}-{filename}.md"

# Copy the filename to the clipboard
os.system(f"echo '{filename}' | pbcopy")

print(f"Filename '{filename}' copied to clipboard.")
