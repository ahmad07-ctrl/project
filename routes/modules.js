const express = require('express');
const router = express.Router();
const { authenticateToken, authorizeRoles } = require('../middleware/auth');
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

// Seul un ADMIN peut affecter un module à un étudiant
router.post('/modules/assign', authenticateToken, authorizeRoles('ADMIN'), async (req, res) => {
  const { studentProfileId, moduleId } = req.body;

  try {
    const updatedStudent = await prisma.studentProfile.update({
      where: { id: studentProfileId },
      data: {
        modules: { connect: { id: moduleId } }
      }
    });

    return res.status(200).json({ 
      message: "Module attribué avec succès par l'administrateur.", 
      student: updatedStudent 
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

module.exports = router;
