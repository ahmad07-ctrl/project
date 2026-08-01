const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middlewares globaux
app.use(cors());
app.use(express.json());

// Import des routes de l'application
const gradesRoutes = require('./routes/grades');
const modulesRoutes = require('./routes/modules');
const scheduleRoutes = require('./routes/schedule');

// Activation des endpoints sécurisés
app.use('/api', gradesRoutes);
app.use('/api', modulesRoutes);
app.use('/api', scheduleRoutes);

// Route de test / état du serveur
app.get('/', (req, res) => {
  res.send('API de Gestion Scolaire opérationnelle et sécurisée.');
});

// Lancement du serveur sur le port défini
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Serveur démarré sur le port ${PORT}`);
});
