const express = require('express');
const router = express.Router();
const { authenticateToken } = require('../middleware/auth');
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

// Récupération de l'emploi du temps adapté au rôle
router.get('/schedule', authenticateToken, async (req, res) => {
  const { userId, role } = req.user;

  try {
    if (role === 'STUDENT') {
      // Vue Étudiant : uniquement ses cours inscrits
      const schedule = await prisma.schedule.findMany({
        where: { module: { students: { some: { userId } } } },
        include: { module: true }
      });
      return res.json(schedule);
    }

    if (role === 'PROFESSOR') {
      // Vue Enseignant : uniquement ses cours dispensés
      const schedule = await prisma.schedule.findMany({
        where: { module: { professor: { userId } } },
        include: { module: true }
      });
      return res.json(schedule);
    }

    if (role === 'ADMIN') {
      // Vue Admin / Gestionnaire : vue globale
      const schedule = await prisma.schedule.findMany({ include: { module: true } });
      return res.json(schedule);
    }
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

module.exports = router;
