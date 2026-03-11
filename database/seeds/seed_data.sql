-- SQL seed data for Badminton Tournament Hub

INSERT INTO users (id, email, password_hash, role) VALUES
(gen_random_uuid(), 'admin@example.com', 'hash1', 'admin'),
(gen_random_uuid(), 'player1@example.com', 'hash2', 'player'),
(gen_random_uuid(), 'player2@example.com', 'hash3', 'player');

INSERT INTO tournaments (id, name, location, date, rules) VALUES
(gen_random_uuid(), 'Spring Open', 'New York', CURRENT_DATE, 'Standard Rules'),
(gen_random_uuid(), 'Summer Open', 'Los Angeles', CURRENT_DATE + INTERVAL '10 days', 'Standard Rules');

-- Assuming the UUIDs for matches and users are known for this seed
INSERT INTO matches (id, tournament_id, player1_id, player2_id, umpire_id, scheduled_time) VALUES
(gen_random_uuid(), (SELECT id FROM tournaments WHERE name='Spring Open'), (SELECT id FROM users WHERE email='player1@example.com'), (SELECT id FROM users WHERE email='player2@example.com'), (SELECT id FROM users WHERE email='admin@example.com'), CURRENT_TIMESTAMP + INTERVAL '1 day'),
(gen_random_uuid(), (SELECT id FROM tournaments WHERE name='Summer Open'), (SELECT id FROM users WHERE email='player1@example.com'), (SELECT id FROM users WHERE email='player2@example.com'), (SELECT id FROM users WHERE email='admin@example.com'), CURRENT_TIMESTAMP + INTERVAL '2 days');

INSERT INTO scores (id, match_id, player1_score, player2_score) VALUES
(gen_random_uuid(), (SELECT id FROM matches LIMIT 1), 21, 15),
(gen_random_uuid(), (SELECT id FROM matches OFFSET 1 LIMIT 1), 18, 21);

INSERT INTO notifications (id, user_id, message) VALUES
(gen_random_uuid(), (SELECT id FROM users WHERE email='player1@example.com'), 'Your match is scheduled for tomorrow.'),
(gen_random_uuid(), (SELECT id FROM users WHERE email='player2@example.com'), 'Your match is scheduled for tomorrow.');

INSERT INTO registrations (id, user_id, tournament_id) VALUES
(gen_random_uuid(), (SELECT id FROM users WHERE email='player1@example.com'), (SELECT id FROM tournaments WHERE name='Spring Open')),
(gen_random_uuid(), (SELECT id FROM users WHERE email='player2@example.com'), (SELECT id FROM tournaments WHERE name='Summer Open'));