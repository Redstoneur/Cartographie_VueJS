# Utiliser l'image Node.js 14 comme base
FROM node:14

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances du projet
RUN npm install

# Construire le projet pour la production
RUN npm run build

# Exposer le port 8080 pour la communication
EXPOSE 8080

# Démarrer le serveur web avec la commande "npm start"
CMD ["npm", "start"]
