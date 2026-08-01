const jwt = require('jsonwebtoken');

// 1. Authentification JWT
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.status(401).json({ message: "Accès refusé. Token manquant." });

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ message: "Token invalide ou expiré." });
    req.user = user;
    next();
  });
};

// 2. Contrôle d'accès basé sur le rôle (RBAC)
const authorizeRoles = (...allowedRoles) => {
  return (req, res, next) => {
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ 
        message: "Accès interdit : privilèges insuffisants." 
      });
    }
    next();
  };
};

module.exports = { authenticateToken, authorizeRoles };
