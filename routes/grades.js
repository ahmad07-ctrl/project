const express = require('express');
const router = express.Router();
const { authenticateToken, authorizeRoles } = require('../middleware/auth');
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

// Seul un PROFESSEUR peut attribuer ou modifier une note
router.post('/grades', authenticateToken, authorizeRoles('PROFESSOR'), async (req, res) => {
  const { studentId, moduleId, value } = req.body;
  const professorUserId = req.user.userId;

  try {
    // Vérification : le professeur enseigne-t-il bien ce module ?
    const moduleTaught = await prisma.courseModule.findFirst({
      where: {
        id: moduleId,
        professor: { userId: professorUserId }
      }
    });

    if (!moduleTaught) {
      return res.status(403).json({ 
        message: "Action refusée : Vous n'êtes pas le professeur responsable de ce module." 
      });
    }

    // Crée la note ou la met à jour si elle existe déjà
    const grade = await prisma.grade.upsert({
      where: {
        studentId_moduleId: { studentId, moduleId }
      },
      update: { value },
      create: { studentId, moduleId, value }
    });

    return res.status(200).json({ message: "Note enregistrée avec succès.", grade });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

module.exports = router;
