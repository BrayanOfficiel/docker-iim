# Reverse Proxy avec Nginx

## Description

Ce projet implémente un reverse proxy avec Nginx qui route les requêtes vers deux applications web distinctes :
- **Flask App** : Une API REST en Python accessible via `/api`
- **HTML App** : Un site HTML statique servi par Nginx accessible via `/site`

Le but de cet exercice est de comprendre le concept de reverse proxy : un seul point d'entrée (port 8080) qui route les requêtes vers les services backend selon l'URL.

## Architecture

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ http://localhost:8080
┌──────▼──────────────────────┐
│   Nginx (Reverse Proxy)     │
│   Port: 8080                │
└──┬───────────────────────┬──┘
   │ /api                  │ /site
┌──▼──────┐          ┌─────▼─────┐
│ Flask   │          │ HTML App │
│ :5000   │          │ :80       │
└─────────┘          └───────────┘
```

## Installation

### Prérequis

- Docker Desktop installé et démarré
- Docker Compose installé

### Commandes

```bash
# Construire et démarrer tous les services
docker-compose up --build
```

## Accès

- **Site HTML** : http://localhost:8080/site
- **API Flask** : http://localhost:8080/api
- **API Health** : http://localhost:8080/api/health
- **API Info** : http://localhost:8080/api/info

**Note** : Le port 5000 n'est pas exposé directement. Toutes les requêtes passent par Nginx sur le port 8080.

## Configuration

### Nginx

Configuration dans `nginx/default.conf` :
- Route `/api` → `flask-app:5000`
- Route `/site` → `html-app:80`
- Redirection `/` → `/site`

### Flask

Routes disponibles :
- `/` : Message de bienvenue
- `/health` : Health check
- `/info` : Informations sur le service

### Ports

- 8080 : Port exposé sur l'hôte (Nginx)
- 5000 : Port interne Flask (non exposé)
- 80 : Port interne HTML app (non exposé)

---

**Auteur** : Boudjemeline Haider - IIM A3  
**Date** : 2025
