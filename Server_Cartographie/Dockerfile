# Spécifie l'image de base
FROM python:3.8

# Définit le répertoire de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code source
COPY . .

# Expose le port de l'API
EXPOSE 8000

# Définit la commande pour lancer l'API
CMD ["python", "main.py"]
