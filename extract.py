# Open the source file for reading
with open("content.txt", "r") as file:
    lines = file.readlines()

# Initialize an empty list to store event information
today_events = []

# Iterate over the lines to find events happening TODAY
i = 0
while i < len(lines):
    if "TODAY" in lines[i]:
        # Extract event name (usually the line before TODAY)
        event_name = lines[i].strip()
        # Split the event name by spaces into a list of words
        event_name_parts = lines[i].strip().split()

        # Join all the parts except the last one ("TODAY")
        event_name = " ".join(event_name_parts[:-1])
        
        # Extract event time (the line after TODAY)
        event_time = lines[i + 2].strip()
        
        # Extract event location (two lines after TODAY)
        event_location = lines[i + 4].strip()

        # Store the extracted information
        today_events.append(f"Event: {event_name}\nTime: {event_time}\nPlace: {event_location}\n")
        
    i += 1

# Write the extracted events to a new file
with open("eventcredential.txt", "w") as outfile:
    for event in today_events:
        outfile.write(event + "\n")
