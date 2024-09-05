final_text = """Hello. My name is Charles Dickens.
I am an English novelist.
I was born on February 7, 1812, in Portsmouth, England.
I am most famous as a writer of the Victorian era.
I married Catherine Hogarth in 1836. We have ten children.
Some of my most famous works include "A Christmas Carol", "Oliver Twist", "David Copperfield", and "Great Expectations".
Besides being a writer, my other talent was doing dramatic public readings of my work.
I died on June 9, 1870, at my home in Gad's Hill Place, Kent, England."""

# Split the text by lines and process
lines = final_text.split('\n')
output = ""

for line in lines:
    line = line.strip()

    if "My name is" in line:
        name = line.split("My name is ")[1]
        output += f"Name: {name}\n"

    elif "I was born on" in line:
        dob_part = line.split("I was born on ")[1]
        dob, birthplace = dob_part.split(", in ")
        output += f"Date of Birth: {dob}\nBirthplace: {birthplace}\n"

    elif "most famous as" in line:
        famous_for = line.split("most famous as ")[1]
        output += f"Most Famous For: {famous_for}\n"

    elif "I married" in line:
        married_part = line.split("I married ")[1]
        spouse, year_of_marriage = married_part.split(" in ")
        output += f"Married To: {spouse}\nYear of Marriage: {year_of_marriage.strip('.')}\n"

    elif "We have" in line:
        children = line.split("We have ")[1].split(" ")[0]
        output += f"Number of Children: {children}\n"

    elif "Some of my most famous works include" in line:
        works = line.split("include ")[1].strip('.')
        output += f"Famous Works: {works}\n"

    elif "my other talent was" in line:
        other_talent = line.split("my other talent was ")[1].strip('.')
        output += f"Other Talent: {other_talent}\n"

    elif "I died on" in line:
        death_part = line.split("I died on ")[1]
        date_of_death, place_of_death = death_part.split(", at my home in ")
        output += f"Date of Death: {date_of_death}\nPlace of Death: {place_of_death.strip('.')}\n"

# Print final output
print(output)
