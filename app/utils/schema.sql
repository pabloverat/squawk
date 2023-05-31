DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS squawks;


CREATE TABLE event (
  event_id INTEGER PRIMARY KEY AUTOINCREMENT,
  type_of_action INT NOT NULL,
  user_id VARCHAR NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR NOT NULL,
  password VARCHAR NOT NULL,
  is_admin BOOLEAN NOT NULL
);

CREATE TABLE squawks (
  squawk_id INTEGER PRIMARY KEY AUTOINCREMENT,
  content VARCHAR NOT NULL,
  is_reply_to INT,
  user_id INT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (user_id, username, password, is_admin) VALUES (1, 'Pablito', 'yacomiocompanero', 1);
INSERT INTO users (user_id, username, password, is_admin) VALUES (2, 'Macias77', 'holi', 1);
INSERT INTO users (user_id, username, password, is_admin) VALUES (3, 'Rafa', 'peppapig', 1);
INSERT INTO users (user_id, username, password, is_admin) VALUES (258, 'MiaThompson', 'thompson14', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (259, 'EthanAdams5', 'Ocean95', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (260, 'ParkOurLivia', 'ParkerO83', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (261, 'HayesBenjamin', 'HayMonkey9', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (262, 'TheOnlyAva', '@va5parks', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (263, 'WriteOnSam', 'heavyfeather22', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (264, 'StellarBella', 'missy67', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (265, 'HarryCarter', 'Fu5ion32', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (266, 'TurnerSophia12', 'R4inJungle2', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (267, 'DannyInDaValley', 'Nets4Life', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (268, 'JollyCharlotte', 'johnsonvelvet', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (269, 'WillTheChill', 'erica58', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (270, 'AmeliaRobrs', 'StarrySky28', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (271, 'J-Morgan', 'Jackson#Comet', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (272, 'SnowyHarper', 'WhiteRose', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (273, 'XanderClark88', 'alex250602', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (274, 'EmmaThePanda', 'bl4cknwh1te', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (275, 'OllieHallelujah', 'Hall#Rocket44', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (276, 'AbbyOnWard', 'SunFlower09', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (277, 'CooperTrooper', 's37c28p19r', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (278, 'MrBrownie', 'ob1canolli', 0);
INSERT INTO users (user_id, username, password, is_admin) VALUES (279, 'EmmyMorris23', 'Skyline0723', 0);

INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Can''t wait for the weekend!', NULL, 261);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Adventures await just beyond the horizon.', NULL, 277);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Nature never ceases to amaze me.', NULL, 258);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Unleashing my creativity with every brushstroke.', NULL, 275);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Feeling inspired to create some art today.', NULL, 263);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Catching up on my favorite TV show.', NULL, 279);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Finding joy in the simplest of things.', 0, 276);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Loved the painting you gave me!', 4, 272);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('OMG! Let''s hang out!', 1, 272);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Live life to the fullest, every single day!', 0, 267);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Embracing the magic of the moment.', 0, 268);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Cheering on my favorite team! #LaU', 0, 267);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Exploring new horizons. #AdventureTime', 0, 259);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Enjoying a relaxing evening with a good book.', 0, 260);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('¡Somos campeones 8tra vez! #SiempreContigo', 0, 2);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Chilling with good company and good music.', 0, 269);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('How''s the book going?', 5, 258);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Dream big and reach for the stars!', 0, 264);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Yea, let''s get together at @CooperTrooper''s', 1, 275);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Inhaling the crisp air of a winter morning. #BlessNorway', 0, 272);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('First!', 18, 278);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Let''s do it again sometime!', 16, 274);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Enjoying the sunshine and good vibes.', 0, 265);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Lost in the depths of the jungle.', 0, 266);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Notice me @StellarBella', 18, 276);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Stargazing on a clear night is pure bliss.', 0, 270);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('With love for my love <3', 4, 275);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('I''ll go find u lol', 24, 276);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Just had a wonderful day at the park!', 0, 258);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Hiii!', 18, 266);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Yea! Next weekend!', 16, 260);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('This season ours! #BringDaThunder', 0, 271);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Feeling motivated and ready to tackle the day', 0, 263);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Working on a new project', 0, 264);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Wait til I''m back in the city!', 16, 270);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Sounds good!', 1, 277);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Adventures await!', 0, 266);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Can''t even tackle @EmmyMorris23 lol', 33, 258);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('U go girl!', 18, 268);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('We''ll wait for u @AmeliaRobrs', 16, 269);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Good luck, bro #GoThunders', 32, 273);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Chilling with a good book', 0, 269);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('I''ll bring the games!', 1, 261);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Stargazing on a clear night', 0, 270);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Feeling grateful for the little things', 0, 275);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Movie night with friends!', 0, 261);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Just had a great day at the park!', 0, 264);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Excited for the weekend!', 0, 259);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('The book was better jk', 46, 262);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Embracing the joy of music', 0, 279);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Enjoying the sunshine ☀️', 0, 260);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Trying out a new recipe tonight', 0, 262);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Creating memories with loved ones', 0, 277);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Dancing like nobody''s watching', 0, 268);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Exploring new places', 0, 273);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Invite meee!', 52, 272);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Reflecting on a wonderful vacation', 0, 264);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('#BringDaTrophy #BringDaThunder', 32, 267);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Need to explain? #BringDaThunder', 0, 271);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Always welcome @SnowyHarper <3', 52, 262);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Lost in my thoughts', 0, 276);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Champions!!!', 15, 267);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Brown''s Brownieees!!!', 0, 278);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Feeling hungry :( #MakeItStop', 0, 262);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Enjoying the beauty of nature', 0, 272);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Taking a break to enjoy a peaceful moment', 0, 260);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Indulging in delicious treats and good vibes.', 0, 278);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Totally celebrating with brownies tonight!', 15, 278);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Capturing precious moments', 0, 274);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Unos tacos o q?', 64, 2);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Are you bringing to campus?', 63, 274);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Bring some, @MrBrownie!', 15, 2);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('The world is full of surprises.', 0, 262);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Three for me!', 63, 259);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Exploring the world one step at a time.', 0, 273);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Embracing both the light and the darkness.', 0, 274);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('Making memories with loved ones.', 0, 259);
INSERT INTO squawks (content, is_reply_to, user_id) VALUES ('How much?', 63, 260);
