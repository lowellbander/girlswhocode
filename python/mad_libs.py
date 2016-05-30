'''
Mad Libs
adapted from the Shel Silverstein poem "Magic" from
"Where the Sidewalk Ends"
Original Poem
Sandra’s seen a leprechaun,
Eddie touched a troll,
Laurie danced with witches once,
Charlie found some goblins’ gold.
Donald heard a mermaid sing,
Susy spied an elf,
But all the magic I have known
I’ve had to make myself.
'''

name_1 = input("Give me a person's name: ")
magic_creature1 = input("Give the name of a magic creature: ")

line_1 = name_1 + " seen a " + magic_creature1

name_2 = input("Give me a another person's name: ")
magic_creature2 = input("Give the name of another magic creature: ")

line_2 = name_2 + " touched a " + magic_creature2 

physical_activity = input("Give me a physical activity: ")

line_3 = "Laurie " + physical_activity + " with witches once"

precious_item = input("Give me precious item: ")

line_4 = "Charlie found some globin's " + precious_item

verb = input("Give me a verb: ")
 
line_5 = "Donald heard a mermaid " + verb

quiet_activity = input("Give me a quiet activity: ")

line_6 = "Susy " +  quiet_activity + " an elf"

last_lines = '''But all the magic I've known
I've had to make myself
'''

print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
print(last_lines)

