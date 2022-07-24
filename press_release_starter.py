press_release = """

Doody Calls, a nationwide leader in dog poop removal services, is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. Doody Calls currently cleans up dog poop in over 57 territories across 23 states and has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# Remove the leading and trailing whitespace (new lines) from press_release
press_release.strip()
print(press_release)

# Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet waste" tests better than "dog poop"
replace_words = press_release.replace('dog poop', 'pet waste')
print(replace_words)


# We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)
change_name = replace_words.replace('Doody Calls', 'DoodyCalls')
print(change_name)

# Our research shows that it's best to shout our press releases. Make the entire press release uppercased!
shout = change_name.upper()
print(shout)

# Print out the updated press release with all of the above changes:
print(shout)

