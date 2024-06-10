story_text = f"""
In a world where magic and technology intertwine, you step into the shoes of a novice mage seeking to unravel the mysteries of the ancient Library of Data. Legends tell of a powerful oracle hidden within its walls, holding the key to unlocking unimaginable knowledge. As you embark on your journey, you must navigate through the treacherous dungeons of SQL queries, facing challenges and adversaries along the way.

Your mentor, a wise wizard named SQLius, guides you on your quest. He teaches you the ways of SQL, a magical language that allows you to summon and manipulate data with precision. Armed with this knowledge, you delve deeper into the Library, uncovering hidden truths and untold stories.

As you progress through the Library, you encounter strange creatures guarding valuable information. With each query you master, you unlock new abilities and uncover the secrets of the Oracle. But beware, for dark forces also seek to exploit the power within the Library for their own nefarious purposes.

In the final showdown, you face off against the sinister sorcerer Datacorruptor, who seeks to twist the Oracle's knowledge for his own gain. With the fate of the Library hanging in the balance, you must use all your SQL skills to outwit and outmaneuver your foe. Only by mastering the language of SQL can you unlock the true power of the Oracle and emerge victorious, fulfilling your destiny as the hero of the Library of Data.
"""

dataset_text = f"""
CREATE TABLE Characters (
    character_id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    level INTEGER
);

INSERT INTO Characters (name, class, level) VALUES ("SQLius", "Wizard", 50);
INSERT INTO Characters (name, class, level) VALUES ("Novice Mage", "Mage", 10);
INSERT INTO Characters (name, class, level) VALUES ("Runekeeper", "Warlock", 25);
INSERT INTO Characters (name, class, level) VALUES ("Energia", "Sorcerer", 30);
INSERT INTO Characters (name, class, level) VALUES ("Mystica", "Druid", 15);

CREATE TABLE Spells (
    spell_id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    power INTEGER
);

INSERT INTO Spells (name, type, power) VALUES ("Fireball", "Attack", 50);
INSERT INTO Spells (name, type, power) VALUES ("Heal", "Support", 30);
INSERT INTO Spells (name, type, power) VALUES ("Lightning Bolt", "Attack", 60);
INSERT INTO Spells (name, type, power) VALUES ("Protective Shield", "Defense", 40);
INSERT INTO Spells (name, type, power) VALUES ("Teleport", "Utility", 45);

CREATE TABLE Items (
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    value INTEGER
);

INSERT INTO Items (name, type, value) VALUES ("Staff", "Weapon", 20);
INSERT INTO Items (name, type, value) VALUES ("Robe", "Armor", 30);
INSERT INTO Items (name, type, value) VALUES ("Potion", "Consumable", 10);
INSERT INTO Items (name, type, value) VALUES ("Ring", "Accessory", 15);
INSERT INTO Items (name, type, value) VALUES ("Scroll", "Artifact", 25);
"""
                           
                           
                           
                           
questions_text = f"""
    questions:
    - intro: "Welcome to the Query Kingdom! The Oracle Owl has foreseen that only those who master SQL can save our realm from the Maleficent Horde. Let's start by recruiting the most powerful magical creatures to aid us."
      prompt: "Find the magical creatures with power levels greater than 5."
      solution: "SELECT * FROM MagicalCreatures WHERE power_level > 5"
      success: "Excellent work! The Oracle Owl is impressed. Now, let's move on to recruiting the most skilled wizards to our cause."

    - intro: "Our next challenge awaits in the Join Forest, where the Join Dragon guards the entrance to the Maleficent Horde's lair. To gain access, we must enlist the help of the most talented wizards from both realms."
      prompt: "Find the wizards from the Query Kingdom and Join Forest."
      solution: "SELECT * FROM DarkWizard WHERE realm_id IN (SELECT realm_id FROM Realms WHERE realm_name IN ('Query Kingdom', 'Join Forest'))"
      success: "Well done! The fellowship of wizards is growing stronger. Now, let's gather information on the challenges that await us in the Maleficent Horde's lair."

    - intro: "The Maleficent Horde has set up challenging obstacles in the Market Puzzle and Dungeon Maze. To overcome these challenges, we must understand their difficulties."
      prompt: "Find the names of the challenges and their difficulties."
      solution: "SELECT challenge_name, difficulty FROM Challenges"
      success: "Great job! Knowing the challenges' difficulties will help us prepare for what lies ahead. Let's now uncover the power levels of all the magical creatures in both realms."

    - intro: "The power levels of the magical creatures will determine our strategy against the Maleficent Horde. We must gather this vital information to ensure our success."
      prompt: "Find the power levels of all magical creatures."
      solution: "SELECT creature_name, power_level FROM MagicalCreatures"
      success: "Fantastic work! Knowing the power levels of the magical creatures will guide our decisions in the upcoming battles. Now, let's identify the dark wizard who poses a threat to our cause."

    - intro: "Malicious Malfoy, the dark wizard, has aligned himself with the Maleficent Horde. We must locate him and neutralize this threat to our mission."
      prompt: "Find the name of the dark wizard and his realm."
      solution: "SELECT wizard_name, realm_name FROM DarkWizard JOIN Realms ON DarkWizard.realm_id = Realms.realm_id"
      success: "Well done! With Malicious Malfoy's whereabouts known, we can now focus on our final preparations before facing the Maleficent Horde."
                           """


dalle_prompt = "An apprentice magician of Hispanic descent stands before the antiquated Hall of Information, encircled by twirling mystic forces and enigmatic symbols reminiscent of advanced data management languages. An aged wizard of South Asian descent, known for his wisdom in these languages, accompanies them. Towering doors of the information hall stand in the grand background, suggesting the immense wisdom concealed within. Photo-realistic, in full high-definition, digital environment resembling popular sandbox video games of the 2010s."