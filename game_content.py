story_text = f"""
                       In a world where magic and technology intertwine, you are an aspiring wizard named Merlin who discovers a mysterious tome filled with ancient knowledge. As you delve deeper into the pages, you realize that this book holds the secrets to mastering the mystical language of SQL, a powerful tool that can manipulate data in ways never before imagined.

Eager to prove yourself as a worthy apprentice, you embark on a journey to various enchanted realms, each ruled by a different SQL concept. Along the way, you encounter challenges and puzzles that test your problem-solving skills and your understanding of SQL syntax.

From the bustling markets of the Query Kingdom to the treacherous dungeons of the Join Forest, you must use your newfound SQL abilities to uncover hidden truths, forge alliances with magical creatures, and ultimately confront the dark wizard who seeks to misuse the power of SQL for his own sinister purposes.

As you progress through the game, you not only hone your SQL skills but also learn valuable lessons about the importance of data integrity, efficiency, and collaboration. In the end, you emerge victorious, having not only saved the realms from destruction but also gained the respect of your peers as a true SQL master.

Are you ready to embark on this epic adventure and unlock the secrets of SQL? The fate of the magical world lies in your hands, young wizard.
                       """
dataset_text = f"""
                         CREATE TABLE Realms (
    realm_id INTEGER PRIMARY KEY,
    realm_name TEXT
);

INSERT INTO Realms (realm_id, realm_name) VALUES 
(1, "Query Kingdom"),
(2, "Join Forest");

CREATE TABLE Challenges (
    challenge_id INTEGER PRIMARY KEY,
    realm_id INTEGER,
    challenge_name TEXT,
    difficulty INTEGER
);

INSERT INTO Challenges (challenge_id, realm_id, challenge_name, difficulty) VALUES
(1, 1, "Market Puzzle", 3),
(2, 2, "Dungeon Maze", 5);

CREATE TABLE MagicalCreatures (
    creature_id INTEGER PRIMARY KEY,
    realm_id INTEGER,
    creature_name TEXT,
    power_level INTEGER
);

INSERT INTO MagicalCreatures (creature_id, realm_id, creature_name, power_level) VALUES
(1, 1, "Oracle Owl", 8),
(2, 2, "Join Dragon", 10);

CREATE TABLE DarkWizard (
    wizard_id INTEGER PRIMARY KEY,
    wizard_name TEXT,
    realm_id INTEGER
);

INSERT INTO DarkWizard (wizard_id, wizard_name, realm_id) VALUES
(1, "Malicious Malfoy", 2);"""
                         
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