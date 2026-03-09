# Lost & Found Portal

A Django-based web app where users can report, browse, and manage lost or found items — with image uploads, filtering, and activity logging.

## What It Does

- Auth: sign up, login, logout
- Create, edit, delete lost/found item posts
- Upload item images
- Filter items by Lost / Found / My Posts
- Logs user actions (login, create, update, delete) via middleware & signals

## Stack

- **Backend:** Django + SQLite  
- **Frontend:** Tailwind CSS  + DTL
- **Logging:** Custom middleware & Django signals → `user_activity.log`

## Structure

```
lost-found-portal/
├── core/         # Middleware, activity logger, shared utilities
├── items/        # Item model, forms, views, templates
├── accounts/     # Signup & login views
├── templates/    # Base HTML templates
├── static/       # Tailwind CSS, static assets
├── manage.py
└── settings.py
```

## Architecture

```
Request → Django Middleware (logs activity)
              ↓
         URL Router
              ↓
     accounts/  →  Auth views (login, signup)
     items/     →  CRUD views (list, detail, add, edit, delete)
              ↓
         SQLite DB  ←→  Item & User models
              ↓
       Tailwind templates rendered & returned
              ↓
    Django Signals  →  user_activity.log
```