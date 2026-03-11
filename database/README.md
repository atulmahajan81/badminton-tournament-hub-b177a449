# Badminton Tournament Hub Database

This database schema is designed to manage a badminton tournament hub, handling users, tournaments, matches, scores, notifications, and registrations.

## Schema Diagram

- **users**: Contains registered users including players, organizers, and umpires. Each user has an email, password hash, and a role with constraints to ensure only valid roles are used.
- **tournaments**: Contains details of the tournaments such as name, location, date, and rules.
- **matches**: Contains scheduled matches within tournaments, including IDs of players and umpires.
- **scores**: Contains scores recorded for matches.
- **notifications**: Contains notifications and alerts sent to users.
- **registrations**: Contains player registrations for tournaments.

## Setup

1. Run the `schema.sql` to create the database schema.
2. Use Alembic to apply migrations (see `migrations/env.py` for configuration).
3. Seed the database with initial data using `seed_data.py` or `seed_data.sql`.

## Migrations

Migrations are managed using Alembic. To create a new migration, run:

```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:

```bash
alembic upgrade head
```

## Seed Data

Seed data includes realistic sample data for users, tournaments, matches, scores, notifications, and registrations to simulate a live application.

## Scalability

- **Caching**: Utilize Redis for caching hot data with a 5-minute TTL.
- **Horizontal Scaling**: Supported for read replicas.
- **Async Tasks**: Use Celery for background jobs such as sending notifications.