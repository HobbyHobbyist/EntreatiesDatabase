import mysql.connector



db = mysql.connector.connect(
  host="localhost",
  user="ExposedUser",
  password="ExposedPassword",
  database="Entreaties_DB"
  )

cursor = db.cursor(buffered=True)


def create_entreaties_database():
  cursor.execute("""CREATE DATABASE Entreaties_DB""")
  db.config(database="Entreaties_DB")
  db.reconnect()

  cursor.execute("""CREATE TABLE Profiles (
  Profile_ID VARCHAR(36) NOT NULL, Profile_Name VARCHAR(100) NOT NULL, Email TEXT, Password VARCHAR(512) NOT NULL, 
  Password_Salt VARCHAR(32), 
  PRIMARY KEY (Profile_ID)
  );""")

  cursor.execute("""CREATE TABLE Profilings (
  Profile_ID VARCHAR(36) NOT NULL, Care INTEGER DEFAULT 0, Wit INTEGER DEFAULT 0, Cool INTEGER DEFAULT 0,
  Crudeness INTEGER DEFAULT 0, Judgement INTEGER DEFAULT 0, Malice INTEGER DEFAULT 0, Art BOOL DEFAULT FALSE,
  Design BOOL DEFAULT FALSE, Gaming BOOL DEFAULT FALSE, Programming BOOL DEFAULT FALSE, Music BOOL DEFAULT FALSE,
  Writing BOOL DEFAULT 0, Roleplaying BOOL DEFAULT 0, 
  Profile_Avatar VARCHAR(40), Biography MEDIUMTEXT, Introduction VARCHAR(3000), Profile_Name VARCHAR(100) NOT NULL, 
  PRIMARY KEY (Profile_ID)
  ); """)

  cursor.execute("""CREATE TABLE Profiling_Ratings (Profile_ID VARCHAR(36) NOT NULL, 
  Profile_Name VARCHAR(100) NOT NULL, Target_Profile_Name VARCHAR(100) NOT NULL, 
  Care INTEGER DEFAULT 0, Wit INTEGER DEFAULT 0, Cool INTEGER DEFAULT 0, Crudeness INTEGER DEFAULT 0, 
  Judgement INTEGER DEFAULT 0, Malice INTEGER DEFAULT 0, 
  CONSTRAINT Compound_Unique UNIQUE (Target_Profile_Name, Profile_ID) ) """)

  cursor.execute("""CREATE TABLE Interests (
  Interest CHAR NOT NULL, Rating INTEGER NOT NULL, Profile_ID VARCHAR(36) NOT NULL
  );""")

  cursor.execute("""CREATE TABLE Posts (
  Profile_ID VARCHAR(36) NOT NULL, Post_ID VARCHAR(36) NOT NULL, Post_Title VARCHAR(250), Post_Content MEDIUMTEXT, 
  Amount_Of_Comments INTEGER Default 0, Thumbs_Up_Reactions INT DEFAULT 0, Thumbs_Down_Reactions INT DEFAULT 0, 
  Mindblown_Reactions INT DEFAULT 0, Deadpan_Reactions INT DEFAULT 0, Facepalm_Reactions INT DEFAULT 0, 
  Positive_Votes INT DEFAULT 0, Negative_Votes INT DEFAULT 0, Positive_Vote_Weighting FLOAT, 
  Negative_Vote_Weighting FLOAT, Post_Date TIMESTAMP NOT NULL, Profile_Name VARCHAR(100) NOT NULL, PRIMARY KEY (Post_ID)
  ); """)

  cursor.execute("""CREATE TABLE Post_Comments (
  Profile_ID VARCHAR(36) NOT NULL, Comment_ID VARCHAR(36) NOT NULL, Comment_Content MEDIUMTEXT, 
  Amount_Of_Comments INTEGER Default 0, 

  Thumbs_Up_Reactions INT DEFAULT 0, Thumbs_Down_Reactions INT DEFAULT 0, Mindblown_Reactions INT DEFAULT 0, 
  Deadpan_Reactions INT DEFAULT 0, Facepalm_Reactions INT DEFAULT 0, 

  Positive_Votes INT DEFAULT 0, Negative_Votes INT DEFAULT 0, Positive_Vote_Weighting FLOAT, Negative_Vote_Weighting FLOAT, 

  Comment_Date TIMESTAMP NOT NULL, Profile_Name VARCHAR(100) NOT NULL,
  Parent_Comment VARCHAR(36), Parent_Post VARCHAR(36) NOT NULL, Parent_Subject VARCHAR(36) NOT NULL,
  PRIMARY KEY (Comment_ID)
  ); """)

  
  cursor.execute("""CREATE TABLE Post_Subjects (
  Profile_ID VARCHAR(36) NOT NULL, Subject_ID VARCHAR(36) NOT NULL, Subject_Content TEXT, 
  Amount_Of_Comments INTEGER Default 0, Thumbs_Up_Reactions INT DEFAULT 0, Thumbs_Down_Reactions INT DEFAULT 0, 
  Mindblown_Reactions INT DEFAULT 0, Deadpan_Reactions INT DEFAULT 0, Facepalm_Reactions INT DEFAULT 0, 
  Positive_Votes INT DEFAULT 0, Negative_Votes INT DEFAULT 0, Positive_Vote_Weighting FLOAT, 
  Negative_Vote_Weighting FLOAT, Subject_Date TIMESTAMP NOT NULL, Profile_Name VARCHAR(100) NOT NULL,
  Parent_Post VARCHAR(36) NOT NULL, PRIMARY KEY (Subject_ID)
  ); """)


  cursor.execute("""CREATE TABLE Post_Reactions (
  Profile_ID VARCHAR(36) NOT NULL, Post_ID VARCHAR(36) NOT NULL, Reaction_Name VARCHAR(50) NOT NULL,
  CONSTRAINT Compound_Unique UNIQUE (Profile_ID, Post_ID, Reaction_Name), INDEX (Profile_ID)
  );""")

  cursor.execute("""CREATE TABLE Post_Subject_Reactions (
  Profile_ID VARCHAR(36) NOT NULL, Subject_ID VARCHAR(36) NOT NULL, Reaction_Name VARCHAR(50) NOT NULL,
  CONSTRAINT Compound_Unique UNIQUE (Profile_ID, Subject_ID, Reaction_Name), INDEX (Profile_ID)
  );""")

  cursor.execute("""CREATE TABLE Post_Comment_Reactions (
  Profile_ID VARCHAR(36) NOT NULL, Comment_ID VARCHAR(36) NOT NULL, Reaction_Name VARCHAR(50) NOT NULL,
  CONSTRAINT Compound_Unique UNIQUE (Profile_ID, Comment_ID, Reaction_Name), INDEX (Profile_ID)
  );""")


  cursor.execute("""CREATE TABLE Drafts (
  Profile_ID VARCHAR(36) NOT NULL, Draft_ID VARCHAR(36) NOT NULL, Draft_Title VARCHAR(250), Draft_Content MEDIUMTEXT,
  PRIMARY KEY (Draft_ID)
  ); """)


  cursor.execute("""CREATE TABLE Entreaties (
  Profile_ID VARCHAR(36) NOT NULL, Entreaty_ID VARCHAR(36) NOT NULL, Entreaty_Title VARCHAR(250), Entreaty_Content MEDIUMTEXT,
  Entreaty_Cover VARCHAR(40), 
  
  Art BOOL DEFAULT FALSE, Design BOOL DEFAULT FALSE, Gaming BOOL DEFAULT FALSE, Programming BOOL DEFAULT FALSE, 
  Music BOOL DEFAULT FALSE, Writing BOOL DEFAULT 0, Roleplaying BOOL DEFAULT 0,
  
  Entreaty_Date TIMESTAMP NOT NULL, Profile_Name VARCHAR(100) NOT NULL, Open_Access BOOLEAN NOT NULL, 
  PRIMARY KEY(Entreaty_ID)
  );""")

  cursor.execute("""CREATE TABLE Pinned_Entreaties ( 
    Entreaty_ID VARCHAR(36) NOT NULL, Profile_ID VARCHAR(100) NOT NULL,
    INDEX (Profile_ID), CONSTRAINT entreaty_profile_combo UNIQUE (Entreaty_ID, Profile_ID)
    ); """)



  cursor.execute("""CREATE TABLE Entreaty_Sections (
  Profile_ID VARCHAR(36) NOT NULL, Parent_Entreaty VARCHAR(36) NOT NULL, Section_ID VARCHAR(36) NOT NULL, 
  Section_Name VARCHAR(250) NOT NULL, Section_Date TIMESTAMP NOT NULL, Profile_Name VARCHAR(100) NOT NULL);""")


  cursor.execute("""CREATE TABLE Entreaty_Threads (
  Profile_ID VARCHAR(36) NOT NULL, Parent_Entreaty VARCHAR(36) NOT NULL, Parent_Section VARCHAR(36) NOT NULL, 
  Thread_ID VARCHAR(36) NOT NULL, Thread_Title VARCHAR(250) NOT NULL, Thread_Content MEDIUMTEXT, Thread_Date TIMESTAMP NOT NULL, 
  Profile_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY(Thread_ID)
  );""")


  cursor.execute("""CREATE TABLE Entreaty_Thread_Comments (
  Profile_ID VARCHAR(36) NOT NULL, Parent_Entreaty VARCHAR(36) NOT NULL, Parent_Section VARCHAR(36) NOT NULL, 
  Parent_Thread VARCHAR(36) NOT NULL, Comment_ID VARCHAR(36) NOT NULL, Comment_Content MEDIUMTEXT, Comment_Date TIMESTAMP NOT NULL, 
  Profile_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY(Comment_ID)
  );""")


  cursor.execute(""" CREATE TABLE Entreaty_Tags (
  Tag CHAR NOT NULL, Entreaty_ID VARCHAR(36) NOT NULL
  );""")

  cursor.execute(""" CREATE TABLE Entreaty_Members (
    Entreaty_ID VARCHAR(36) NOT NULL, Profile_ID VARCHAR(36) NOT NULL, Profile_Name VARCHAR(100) NOT NULL
  ); """)

  cursor.execute(""" CREATE TABLE Entreaty_Privileges (
    Entreaty_ID VARCHAR(36), Profile_ID VARCHAR(36), Profile_Name VARCHAR(100), Thread_Creation BOOLEAN NOT NULL,
    Thread_Moderation BOOLEAN NOT NULL, Member_Moderation BOOLEAN NOT NULL
  ); """)

  cursor.execute(""" CREATE TABLE Entreaty_Prompts (
    Entreaty_ID VARCHAR(36) NOT NULL, Prompt VARCHAR(3000) NOT NULL
  ); """)

  def trigger_statements():
    cursor.execute("""CREATE TRIGGER initialize_profiling_row
        AFTER INSERT ON Profiles FOR EACH ROW
        INSERT INTO Profilings (Profile_ID, Profile_Name) VALUES (NEW.Profile_ID, NEW.Profile_Name) """)
      
    cursor.execute("""CREATE TRIGGER initialize_entreaty_row 
      AFTER INSERT ON Entreaties FOR EACH ROW
      INSERT INTO Entreaty_Sections (Section_ID, Section_Name, Section_Date, Parent_Entreaty, Profile_ID, Profile_Name)
      VALUES ("000000000000000000000000000000000000", "General", NOW(), NEW.Entreaty_ID, NEW.Profile_ID, NEW.Profile_Name)""")
    
    cursor.execute("""CREATE TRIGGER remove_personality_rating_influence 
    AFTER DELETE ON Profiling_Ratings FOR EACH ROW 
    UPDATE Profilings SET Care = Care - OLD.Care, Wit = Wit - OLD.Wit, Cool = Cool - OLD.Cool, 
    Crudeness = Crudeness - OLD.Crudeness, Judgement = Judgement - OLD.Judgement, Malice = Malice - OLD.Malice 
    WHERE Profile_Name = OLD.Target_Profile_Name LIMIT 1 """)

    cursor.execute("""CREATE TRIGGER initialize_founding_member 
    AFTER INSERT ON Entreaties FOR EACH ROW
    INSERT INTO Entreaty_Members (Entreaty_ID, Profile_ID, Profile_Name) VALUES (NEW.Entreaty_ID, NEW.Profile_ID, 
    NEW.Profile_Name)""")

  
  def procedures(): # These are made into procedures because I'd rather their redundancy be somewhere with less eye traffic
    # POST
    cursor.execute("""
    CREATE PROCEDURE seek_post_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      SELECT COUNT(*) FROM Post_Reactions 
      WHERE Profile_ID = User AND Post_ID = Target_ID AND Reaction_Name = Reaction;
    END ;
    """)
    
    cursor.execute("""
    CREATE PROCEDURE create_post_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      INSERT INTO Post_Reactions (Profile_ID, Post_ID, Reaction_Name) VALUES (User, Target_ID, Reaction);
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      DELETE FROM Post_Reactions 
      WHERE Profile_ID = User AND Post_ID = Target_ID AND Reaction_Name = Reaction 
      LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Posts SET Posts.Thumbs_Up_Reactions = (Posts.Thumbs_Up_Reactions + 1) WHERE Post_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Posts SET Posts.Thumbs_Down_Reactions = (Posts.Thumbs_Down_Reactions + 1) WHERE Post_ID = Target_ID;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Posts SET Posts.Thumbs_Up_Reactions = (Posts.Thumbs_Up_Reactions - 1) WHERE Post_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Posts SET Posts.Thumbs_Down_Reactions = (Posts.Thumbs_Down_Reactions - 1) WHERE Post_ID = Target_ID LIMIT 1;
    END ;
    """)

    # SUBJECT
    cursor.execute("""
    CREATE PROCEDURE seek_post_subject_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      SELECT COUNT(*) FROM Post_Subject_Reactions 
      WHERE Profile_ID = User AND Subject_ID = Target_ID AND Reaction_Name = Reaction;
    END ;
    """)
    
    cursor.execute("""
    CREATE PROCEDURE create_post_subject_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      INSERT INTO Post_Subject_Reactions (Profile_ID, Subject_ID, Reaction_Name) VALUES (User, Target_ID, Reaction);
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_subject_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      DELETE FROM Post_Subject_Reactions 
      WHERE Profile_ID = User AND Subject_ID = Target_ID AND Reaction_Name = Reaction 
      LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_subject_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Subjects SET Post_Subjects.Thumbs_Up_Reactions = (Post_Subjects.Thumbs_Up_Reactions + 1) 
      WHERE Subject_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_subject_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Subjects SET Post_Subjects.Thumbs_Down_Reactions = (Post_Subjects.Thumbs_Down_Reactions + 1) 
      WHERE Subject_ID = Target_ID;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_subject_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Subjects SET Post_Subjects.Thumbs_Up_Reactions = (Post_Subjects.Thumbs_Up_Reactions - 1) 
      WHERE Subject_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_subject_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Subjects SET Post_Subjects.Thumbs_Down_Reactions = (Post_Subjects.Thumbs_Down_Reactions - 1) 
      WHERE Subject_ID = Target_ID LIMIT 1;
    END ;
    """)

    # COMMENT

    cursor.execute("""
    CREATE PROCEDURE seek_post_comment_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      SELECT COUNT(*) FROM Post_Comment_Reactions 
      WHERE Profile_ID = User AND Comment_ID = Target_ID AND Reaction_Name = Reaction;
    END ;
    """)
    
    cursor.execute("""
    CREATE PROCEDURE create_post_comment_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      INSERT INTO Post_Comment_Reactions (Profile_ID, Comment_ID, Reaction_Name) VALUES (User, Target_ID, Reaction);
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_comment_reaction ( IN User VARCHAR(36), IN Target_ID VARCHAR(36), IN Reaction VARCHAR(36) )
    BEGIN
      DELETE FROM Post_Comment_Reactions 
      WHERE Profile_ID = User AND Comment_ID = Target_ID AND Reaction_Name = Reaction 
      LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_comment_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Comments SET Post_Comments.Thumbs_Up_Reactions = (Post_Comments.Thumbs_Up_Reactions + 1) 
      WHERE Comment_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE give_post_comment_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Comments SET Post_Comments.Thumbs_Down_Reactions = (Post_Comments.Thumbs_Down_Reactions + 1) 
      WHERE Comment_ID = Target_ID;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_comment_thumbs_up ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Comments SET Post_Comments.Thumbs_Up_Reactions = (Post_Comments.Thumbs_Up_Reactions - 1) 
      WHERE Comment_ID = Target_ID LIMIT 1;
    END ;
    """)

    cursor.execute("""
    CREATE PROCEDURE remove_post_comment_thumbs_down ( IN Target_ID VARCHAR(36) )
    BEGIN
      UPDATE Post_Comments SET Post_Comments.Thumbs_Down_Reactions = (Post_Comments.Thumbs_Down_Reactions - 1) 
      WHERE Comment_ID = Target_ID LIMIT 1;
    END ;
    """)

    



  
  trigger_statements()
  procedures()


def create_dummy_profiles():
  cursor.execute("""INSERT INTO Profiles (Profile_ID, Profile_Name, Email, Password) 
  VALUES ("account", "No-Account Account", "account@accounts.com", "password123" ) """)

  cursor.execute("""UPDATE Profilings SET Biography = %s WHERE Profile_ID = "account"
  """, ("""  [{"type":"paragraph","children":[{"text":""}]},{"type":"paragraph","children":[{"text":""}]},{"type":"paragraph","children":[{"text":"If you're using this account, it's likely because you were referred here. This account allows the user to edit and create as they please without the need to register. "}]}]
""",))
  
  cursor.execute("""INSERT INTO Profiles (Profile_ID, Profile_Name, Email, Password) 
  VALUES ("fakeAccount", "Fake-Account Account", "fakeAccount@accounts.com", "password123" ) """)

  cursor.execute("""UPDATE Profilings SET Biography = %s WHERE Profile_ID = "fakeAccount"
  """, ("""  [{"type":"paragraph","children":[{"text":""}]},{"type":"paragraph","children":[{"text":""}]},{"type":"paragraph","children":[{"text":"I'm a fake account that was created to submit example entreaties and posts."}]}]
""",))
  
  cursor.execute("""UPDATE Profilings SET Profile_Avatar = %s WHERE Profile_ID = "fakeAccount" """, ("___robot_avatar.png",))
  
def create_dummy_entreaties():
  cursor.execute("""INSERT INTO Entreaties (Profile_ID, Profile_Name, Entreaty_ID, Entreaty_Title, Entreaty_Content, 
  Entreaty_Cover, Art, Design, Gaming, Programming, Music, Writing, Roleplaying, Open_Access, Entreaty_Date) 
  VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW() )""",
  ("fakeAccount", "Fake-Account Account", "swordDesignRequest", "Sword Design Request", 
  """[{"type":"paragraph","children":[{"text":"\\n \\n ","Bold":true},{"text":"Hey!","Bold":true,"Size":"50px"}]},{"type":"paragraph","children":[{"text":"I'm looking for people who have an interest in 2d art and concept art to design cool and silly swords with!! Please join!!"}]}]""", 
  "___swordRequestCover.png", 1, 1, 0, 0, 0, 0, 0, 0))

  cursor.execute("""INSERT INTO Entreaties (Profile_ID, Profile_Name, Entreaty_ID, Entreaty_Title, Entreaty_Content, 
  Entreaty_Cover, Art, Design, Gaming, Programming, Music, Writing, Roleplaying, Open_Access, Entreaty_Date) 
  VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW() )""",
  ("fakeAccount", "Fake-Account Account", "narutoRoleplayRequest", "Naruto Roleplay Group :)", 
  """[{"type":"paragraph","children":[{"text":"\\n \\n ","Bold":true},{"text":"Dattebayo! Those interested in roleplaying as a group in a Naruto world shaped by us and hopefully you, join! Become an honored shinobi or deadly evildoer!! The possibilities are in your in hands!"}]}]""", 
  "___narutoCover.png", 0, 0, 0, 0, 0, 1, 1, 1))  


def create_dummy_posts():
  cursor.execute("""INSERT INTO Posts (Profile_ID, Profile_Name, Post_ID, Post_Title, Post_Content, Post_DATE) 
            VALUES (%s, %s, %s, %s, %s, NOW())""", ("fakeAccount", "Fake-Account Account", "ExamplePost1", "Example Post",
            """[{"type":"paragraph","children":[{"text":""}]},{"type":"paragraph","children":[{"text":"This is an example post "},{"text":"showing ","Bold":true},{"text":"some","Italic":true},{"text":" "},{"text":"features; ","Underline":true},{"text":"It","Size":"50px"},{"text":" "},{"text":"can (link) ","highlight":"inherit","Link":"https://www.google.com/search?q=define+can"},{"text":"be given reactions and clicked to comment on."}]}]"""))


def print_profiles():
  cursor.execute("""SELECT * FROM Profiles """)
  print(cursor.fetchall())

def print_profilings():
  cursor.execute("""SELECT * FROM Profilings """)
  print(cursor.fetchall())

def print_profiling_ratings():
  cursor.execute("""SELECT * FROM Profiling_Ratings """)
  print(cursor.fetchall())

def print_entreaties():
  cursor.execute("""SELECT * FROM Entreaties """)
  print(cursor.fetchall())


def do_it_all():
  cursor.execute("SELECT Schema_Name FROM Information_Schema.Schemata WHERE Schema_Name = 'Entreaties_DB' ")
  if len(cursor.fetchall()) > 0:
    cursor.execute("""DROP DATABASE entreaties_db""")
  create_entreaties_database()
  db.commit()
  create_dummy_profiles()
  create_dummy_entreaties()
  create_dummy_posts()
  db.commit()

do_it_all()

print_profiles()


