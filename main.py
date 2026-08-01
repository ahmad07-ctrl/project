import os

# Define the HTML code with high styling, full responsiveness, smooth scrolling, and complete feature coverage
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portail Universitaire - Gestion des Notes & Scolarité</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
            box-sizing: border-box;
        }

        /* Custom Scrollbar for smooth scrolling */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(226, 232, 240, 0.8);
        }

        .gradient-bg {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        }

        .active-nav {
            background-color: #3b82f6 !important;
            color: #ffffff !important;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col antialiased overflow-x-hidden">

    <!-- NAVIGATION BAR TOP -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3 cursor-pointer" onclick="showSection('landing-section')">
                <div class="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center font-bold text-xl shadow-lg shadow-blue-500/30">
                    <i class="fa-solid fa-graduation-cap"></i>
                </div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight block leading-none">UNI-PORTAL</span>
                    <span class="text-xs text-slate-400 font-medium">Système de Scolarité & Notes</span>
                </div>
            </div>

            <!-- Header Right Menu -->
            <div class="flex items-center space-x-4">
                <div id="user-pill" class="hidden flex items-center bg-slate-800 px-3 py-1.5 rounded-full border border-slate-700 text-sm">
                    <span class="w-2.5 h-2.5 bg-emerald-500 rounded-full mr-2"></span>
                    <span id="user-display-name" class="font-semibold text-slate-200 mr-2">Utilisateur</span>
                    <span id="user-display-role" class="bg-blue-500/20 text-blue-300 text-xs px-2 py-0.5 rounded-md font-bold uppercase">Rôle</span>
                    <button onclick="logout()" class="ml-3 text-slate-400 hover:text-red-400 transition" title="Déconnexion">
                        <i class="fa-solid fa-right-from-bracket"></i>
                    </button>
                </div>
                <button onclick="showSection('landing-section')" class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs px-3 py-2 rounded-lg border border-slate-700 font-medium transition">
                    <i class="fa-solid fa-house mr-1.5"></i> Accueil
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN WRAPPER -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

        <!-- 1. LANDING & ROLE SELECTION SECTION -->
        <section id="landing-section" class="py-8">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="bg-blue-100 text-blue-700 text-xs font-extrabold uppercase px-3 py-1 rounded-full tracking-wider">Espace Numérique de Travail</span>
                <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-4 mb-3 tracking-tight">Bienvenue sur le Portail Universitaire</h1>
                <p class="text-slate-600 text-base sm:text-lg">Sélectionnez votre profil d'accès pour gérer la scolarité, les notes, bulletins, emplois du temps et le réseau Alumni.</p>
            </div>

            <!-- Role Selector Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <!-- Portal Student Card -->
                <div class="glass-card rounded-2xl p-8 hover:shadow-2xl transition duration-300 transform hover:-translate-y-1 flex flex-col justify-between border-t-4 border-t-blue-600">
                    <div>
                        <div class="w-16 h-16 bg-blue-100 text-blue-600 rounded-2xl flex items-center justify-center text-3xl mb-6 shadow-inner">
                            <i class="fa-solid fa-user-graduate"></i>
                        </div>
                        <h2 class="text-2xl font-bold text-slate-900 mb-2">Espace Étudiant</h2>
                        <p class="text-slate-600 text-sm mb-6 leading-relaxed">
                            Consultez vos notes par semestre, téléchargez vos bulletins officiels, envoyez des réclamations, visualisez votre emploi du temps et contactez les anciens étudiants (Alumni).
                        </p>
                    </div>
                    <div class="space-y-3">
                        <button onclick="openAuthModal('ETUDIANT', 'login')" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl shadow-lg shadow-blue-500/25 transition flex items-center justify-center">
                            <i class="fa-solid fa-right-to-bracket mr-2"></i> Se Connecter (Étudiant)
                        </button>
                        <button onclick="openAuthModal('ETUDIANT', 'register')" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3 px-4 rounded-xl transition flex items-center justify-center border border-slate-300">
                            <i class="fa-solid fa-user-plus mr-2"></i> S'inscrire comme Étudiant
                        </button>
                    </div>
                </div>

                <!-- Portal Teacher Card -->
                <div class="glass-card rounded-2xl p-8 hover:shadow-2xl transition duration-300 transform hover:-translate-y-1 flex flex-col justify-between border-t-4 border-t-emerald-600">
                    <div>
                        <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-2xl flex items-center justify-center text-3xl mb-6 shadow-inner">
                            <i class="fa-solid fa-chalkboard-user"></i>
                        </div>
                        <h2 class="text-2xl font-bold text-slate-900 mb-2">Espace Enseignant / Admin</h2>
                        <p class="text-slate-600 text-sm mb-6 leading-relaxed">
                            Saisissez les notes de vos étudiants par département/école, consultez votre emploi du temps d'enseignement, fixez les coefficients et gérez l'organisation des emplois du temps.
                        </p>
                    </div>
                    <div class="space-y-3">
                        <button onclick="openAuthModal('PROFESSEUR', 'login')" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-4 rounded-xl shadow-lg shadow-emerald-500/25 transition flex items-center justify-center">
                            <i class="fa-solid fa-right-to-bracket mr-2"></i> Se Connecter (Enseignant)
                        </button>
                        <button onclick="openAuthModal('PROFESSEUR', 'register')" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3 px-4 rounded-xl transition flex items-center justify-center border border-slate-300">
                            <i class="fa-solid fa-user-plus mr-2"></i> S'inscrire comme Enseignant
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. AUTHENTICATION MODAL (Dynamic Login / Register) -->
        <div id="auth-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 sm:p-8 relative border border-slate-200 my-8">
                <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 flex items-center justify-center rounded-full hover:bg-slate-100">
                    <i class="fa-solid fa-xmark text-xl"></i>
                </button>

                <!-- Auth Header -->
                <div class="text-center mb-6">
                    <div id="auth-badge" class="inline-block px-3 py-1 text-xs font-bold rounded-full mb-2 uppercase">Profil</div>
                    <h3 id="auth-title" class="text-2xl font-bold text-slate-900">Connexion</h3>
                    <p id="auth-subtitle" class="text-xs text-slate-500 mt-1">Saisissez vos identifiants pour continuer</p>
                </div>

                <!-- Auth Tab Switches -->
                <div class="flex bg-slate-100 p-1 rounded-xl mb-6">
                    <button id="tab-login-btn" onclick="switchAuthTab('login')" class="flex-1 py-2 text-xs font-bold rounded-lg transition bg-white text-slate-800 shadow-sm">Se Connecter</button>
                    <button id="tab-register-btn" onclick="switchAuthTab('register')" class="flex-1 py-2 text-xs font-bold rounded-lg transition text-slate-500">S'inscrire</button>
                </div>

                <!-- Form Login -->
                <form id="login-form" onsubmit="handleLogin(event)" class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Adresse E-mail Universitaire</label>
                        <div class="relative">
                            <i class="fa-solid fa-envelope absolute left-3 top-3.5 text-slate-400 text-sm"></i>
                            <input type="email" required placeholder="nom.prenom@univ.edu" class="w-full pl-9 pr-3 py-2.5 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Mot de passe</label>
                        <div class="relative">
                            <i class="fa-solid fa-lock absolute left-3 top-3.5 text-slate-400 text-sm"></i>
                            <input type="password" required placeholder="••••••••" class="w-full pl-9 pr-3 py-2.5 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                        </div>
                    </div>
                    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl text-sm shadow-md transition">
                        Se connecter à l'espace
                    </button>
                </form>

                <!-- Form Register -->
                <form id="register-form" onsubmit="handleRegister(event)" class="space-y-3 hidden">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Nom</label>
                        <input id="reg-nom" type="text" required placeholder="Diallo" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Prénom</label>
                        <input id="reg-prenom" type="text" required placeholder="Amadou" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Adresse E-mail</label>
                        <input id="reg-email" type="email" required placeholder="amadou@univ.edu" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Numéro de Téléphone</label>
                        <input id="reg-tel" type="tel" required placeholder="+221 77 000 00 00" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Département / École</label>
                        <select class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                            <option>Génie Électrique (ESP)</option>
                            <option>Génie Informatique</option>
                            <option>Génie Mécanique</option>
                            <option>Faculté des Sciences</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Créer un mot de passe</label>
                        <input type="password" required placeholder="••••••••" class="w-full px-3 py-2 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none">
                    </div>
                    <button type="submit" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-xl text-sm shadow-md transition mt-2">
                        Finaliser l'inscription
                    </button>
                </form>
            </div>
        </div>

        <!-- 3. DASHBOARD WORKSPACE (Sidebar Menu + Dynamic Content) -->
        <section id="dashboard-section" class="hidden">
            <div class="flex flex-col lg:flex-row gap-6">

                <!-- SIDEBAR MENU (UNIFIED DASHBOARD NAVIGATION) -->
                <aside class="w-full lg:w-64 bg-white rounded-2xl shadow-sm border border-slate-200 p-4 h-fit sticky top-20">
                    <div class="pb-4 mb-4 border-b border-slate-100 flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg" id="avatar-initials">
                            U
                        </div>
                        <div class="overflow-hidden">
                            <p id="menu-user-name" class="font-bold text-slate-800 text-sm truncate">Nom Prénom</p>
                            <p id="menu-user-role" class="text-xs text-slate-500 font-medium">Rôle</p>
                        </div>
                    </div>

                    <!-- Menu Title -->
                    <p class="text-[11px] font-extrabold text-slate-400 uppercase tracking-wider mb-2 px-3">Menu Principal</p>

                    <!-- Student Navigation Menu -->
                    <nav id="student-menu" class="space-y-1">
                        <button onclick="switchTab('tab-bulletin')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition active-nav" id="btn-tab-bulletin">
                            <i class="fa-solid fa-file-invoice text-base w-6 text-center mr-2"></i> Bulletins & Notes
                        </button>
                        <button onclick="switchTab('tab-edt-etudiant')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-edt-etudiant">
                            <i class="fa-solid fa-calendar-days text-base w-6 text-center mr-2"></i> Emploi du Temps
                        </button>
                        <button onclick="switchTab('tab-reclamations')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-reclamations">
                            <i class="fa-solid fa-circle-exclamation text-base w-6 text-center mr-2"></i> Mes Réclamations
                        </button>
                        <button onclick="switchTab('tab-alumni')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-alumni">
                            <i class="fa-solid fa-users-rectangle text-base w-6 text-center mr-2"></i> Annuaire Alumni
                        </button>
                    </nav>

                    <!-- Teacher Navigation Menu -->
                    <nav id="teacher-menu" class="space-y-1 hidden">
                        <button onclick="switchTab('tab-saisie-notes')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition active-nav" id="btn-tab-saisie-notes">
                            <i class="fa-solid fa-pen-to-square text-base w-6 text-center mr-2"></i> Saisie des Notes
                        </button>
                        <button onclick="switchTab('tab-coefficients')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-coefficients">
                            <i class="fa-solid fa-sliders text-base w-6 text-center mr-2"></i> Config. Coefficients
                        </button>
                        <button onclick="switchTab('tab-edt-prof')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-edt-prof">
                            <i class="fa-solid fa-calendar-check text-base w-6 text-center mr-2"></i> Mon Mon Emploi du Temps
                        </button>
                        <button onclick="switchTab('tab-gestion-edt')" class="nav-btn w-full flex items-center px-3 py-2.5 text-xs font-semibold rounded-xl text-slate-600 hover:bg-slate-100 transition" id="btn-tab-gestion-edt">
                            <i class="fa-solid fa-clock flex-shrink-0 text-base w-6 text-center mr-2"></i> Gestion Heures Hebdo
                        </button>
                    </nav>

                    <div class="pt-4 mt-6 border-t border-slate-100">
                        <button onclick="logout()" class="w-full text-left px-3 py-2 text-xs font-bold text-red-600 hover:bg-red-50 rounded-xl transition flex items-center">
                            <i class="fa-solid fa-power-off w-6 text-center mr-2"></i> Déconnexion
                        </button>
                    </div>
                </aside>

                <!-- DYNAMIC CONTENT VIEW AREA -->
                <div class="flex-1 bg-white rounded-2xl shadow-sm border border-slate-200 p-4 sm:p-6 min-h-[550px] overflow-x-auto">

                    <!-- TAB 1: BULLETINS ET NOTES (ÉTU) -->
                    <div id="tab-bulletin" class="tab-content">
                        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center pb-4 mb-6 border-b border-slate-100 gap-4">
                            <div>
                                <h2 class="text-xl font-bold text-slate-900">Relevé de Notes & Bulletin Automatique</h2>
                                <p class="text-xs text-slate-500">Génération automatique des moyennes semestrielles avec coefficients</p>
                            </div>
                            <div class="flex items-center space-x-2">
                                <select class="bg-slate-50 border border-slate-300 text-xs font-semibold rounded-xl px-3 py-2 outline-none">
                                    <option>Semestre 1 (2025-2026)</option>
                                    <option>Semestre 2 (2025-2026)</option>
                                </select>
                                <button onclick="window.print()" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-3 py-2 rounded-xl shadow transition flex items-center">
                                    <i class="fa-solid fa-download mr-1.5"></i> Imprimer Bulletin
                                </button>
                            </div>
                        </div>

                        <!-- Grades Table -->
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse text-xs">
                                <thead>
                                    <tr class="bg-slate-100 text-slate-700 uppercase font-bold border-b border-slate-200">
                                        <th class="p-3">Matière / Unité d'Enseignement</th>
                                        <th class="p-3 text-center">Coeff</th>
                                        <th class="p-3 text-center">Note CC (/20)</th>
                                        <th class="p-3 text-center">Note Examen (/20)</th>
                                        <th class="p-3 text-center">Moyenne Matière</th>
                                        <th class="p-3 text-center">Statut</th>
                                        <th class="p-3 text-center">Action</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100 font-medium">
                                    <tr class="hover:bg-slate-50">
                                        <td class="p-3 font-bold text-slate-800">Électronique de Puissance</td>
                                        <td class="p-3 text-center font-bold">4</td>
                                        <td class="p-3 text-center">15.5</td>
                                        <td class="p-3 text-center">14.0</td>
                                        <td class="p-3 text-center font-bold text-blue-600">14.60</td>
                                        <td class="p-3 text-center"><span class="bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full font-bold">Validé</span></td>
                                        <td class="p-3 text-center">
                                            <button onclick="openReclamationModal('Électronique de Puissance')" class="text-blue-600 hover:underline font-semibold">Réclamer</button>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-slate-50">
                                        <td class="p-3 font-bold text-slate-800">Programmation Microcontrôleurs (ESP32)</td>
                                        <td class="p-3 text-center font-bold">3</td>
                                        <td class="p-3 text-center">17.0</td>
                                        <td class="p-3 text-center">16.5</td>
                                        <td class="p-3 text-center font-bold text-blue-600">16.70</td>
                                        <td class="p-3 text-center"><span class="bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full font-bold">Validé</span></td>
                                        <td class="p-3 text-center">
                                            <button onclick="openReclamationModal('Programmation Microcontrôleurs')" class="text-blue-600 hover:underline font-semibold">Réclamer</button>
                                        </td>
                                    </tr>
                                    <tr class="hover:bg-slate-50">
                                        <td class="p-3 font-bold text-slate-800">Modélisation des Machines Électriques</td>
                                        <td class="p-3 text-center font-bold">3</td>
                                        <td class="p-3 text-center">12.0</td>
                                        <td class="p-3 text-center">13.5</td>
                                        <td class="p-3 text-center font-bold text-blue-600">12.90</td>
                                        <td class="p-3 text-center"><span class="bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full font-bold">Validé</span></td>
                                        <td class="p-3 text-center">
                                            <button onclick="openReclamationModal('Modélisation des Machines Électriques')" class="text-blue-600 hover:underline font-semibold">Réclamer</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Bulletin Summary Card -->
                        <div class="mt-6 bg-slate-900 text-white p-5 rounded-2xl flex flex-col sm:flex-row justify-between items-center gap-4">
                            <div>
                                <p class="text-xs text-slate-400 font-semibold uppercase tracking-wider">Résultat du Semestre 1</p>
                                <p class="text-2xl font-extrabold text-blue-400 mt-0.5">Moyenne Générale : 14.73 / 20</p>
                            </div>
                            <div class="text-right">
                                <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-3 py-1 rounded-lg text-xs font-bold">
                                    Décision : ADMIS (Mention Bien)
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: EMPLOI DU TEMPS ÉTUDIANT -->
                    <div id="tab-edt-etudiant" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Emploi du Temps Hebdomadaire</h2>
                            <p class="text-xs text-slate-500">Planning de vos cours par département</p>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-xs">
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3">
                                <h4 class="font-bold text-slate-800 border-b pb-2 mb-2 text-center bg-slate-200/60 rounded py-1">LUNDI</h4>
                                <div class="bg-blue-100 border-l-4 border-blue-600 p-2 rounded mb-2">
                                    <p class="font-bold text-blue-900">08h00 - 11h00</p>
                                    <p class="text-slate-700 font-semibold">Électronique de Puissance</p>
                                    <p class="text-[10px] text-slate-500">Amphi A • Prof. Faye</p>
                                </div>
                            </div>
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3">
                                <h4 class="font-bold text-slate-800 border-b pb-2 mb-2 text-center bg-slate-200/60 rounded py-1">MARDI</h4>
                                <div class="bg-emerald-100 border-l-4 border-emerald-600 p-2 rounded mb-2">
                                    <p class="font-bold text-emerald-900">11h15 - 13h15</p>
                                    <p class="text-slate-700 font-semibold">TP ESP32 / Microcontrôleurs</p>
                                    <p class="text-[10px] text-slate-500">Labo Informatique 2</p>
                                </div>
                            </div>
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3">
                                <h4 class="font-bold text-slate-800 border-b pb-2 mb-2 text-center bg-slate-200/60 rounded py-1">MERCREDI</h4>
                                <div class="bg-amber-100 border-l-4 border-amber-600 p-2 rounded mb-2">
                                    <p class="font-bold text-amber-900">09h00 - 12h00</p>
                                    <p class="text-slate-700 font-semibold">Machines Électriques</p>
                                    <p class="text-[10px] text-slate-500">Salle 104</p>
                                </div>
                            </div>
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3">
                                <h4 class="font-bold text-slate-800 border-b pb-2 mb-2 text-center bg-slate-200/60 rounded py-1">JEUDI</h4>
                                <div class="bg-purple-100 border-l-4 border-purple-600 p-2 rounded mb-2">
                                    <p class="font-bold text-purple-900">14h00 - 17h00</p>
                                    <p class="text-slate-700 font-semibold">Anglais Technique</p>
                                    <p class="text-[10px] text-slate-500">Salle 202</p>
                                </div>
                            </div>
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3">
                                <h4 class="font-bold text-slate-800 border-b pb-2 mb-2 text-center bg-slate-200/60 rounded py-1">VENDREDI</h4>
                                <div class="bg-rose-100 border-l-4 border-rose-600 p-2 rounded mb-2">
                                    <p class="font-bold text-rose-900">10h00 - 12h00</p>
                                    <p class="text-slate-700 font-semibold">Projet Tutoré</p>
                                    <p class="text-[10px] text-slate-500">Atelier GE</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 3: RÉCLAMATIONS -->
                    <div id="tab-reclamations" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Module de Réclamation de Notes</h2>
                            <p class="text-xs text-slate-500">Suivi et soumission des contestations de notes</p>
                        </div>
                        
                        <!-- List of Reclamations -->
                        <div class="space-y-3 text-xs mb-6">
                            <div class="p-4 rounded-xl border border-amber-200 bg-amber-50/50 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                                <div>
                                    <span class="bg-amber-200 text-amber-800 font-bold px-2 py-0.5 rounded text-[10px] uppercase">En cours d'examen</span>
                                    <h4 class="font-bold text-slate-800 mt-1">Électronique de Puissance - Examen S1</h4>
                                    <p class="text-slate-600">Demande de vérification de report de note sur la partie hacheurs.</p>
                                </div>
                                <span class="text-slate-400 text-[11px]">Soumis le 12 Fév 2026</span>
                            </div>
                        </div>

                        <button onclick="openReclamationModal('')" class="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow transition">
                            <i class="fa-solid fa-plus mr-1.5"></i> Faire une nouvelle réclamation
                        </button>
                    </div>

                    <!-- TAB 4: ALUMNI -->
                    <div id="tab-alumni" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Annuaire des Anciens Étudiants (Alumni)</h2>
                            <p class="text-xs text-slate-500">Réseautage et contacts des diplômés du département</p>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                            <div class="p-4 border border-slate-200 rounded-xl bg-slate-50/50 flex items-start space-x-3">
                                <div class="w-10 h-10 rounded-full bg-slate-800 text-white font-bold flex items-center justify-center text-sm">SD</div>
                                <div class="flex-1">
                                    <h4 class="font-bold text-slate-800 text-sm">Ousmane Sow</h4>
                                    <p class="text-blue-600 font-medium">Ingénieur Systèmes Embarqués @ Senelec</p>
                                    <p class="text-slate-500 mt-1">Promo 2023 • Génie Électrique</p>
                                    <a href="mailto:ousmane.sow@alumni.univ.sn" class="inline-block mt-2 text-blue-600 font-bold hover:underline">
                                        <i class="fa-solid fa-envelope mr-1"></i> ousmane.sow@alumni.univ.sn
                                    </a>
                                </div>
                            </div>
                            <div class="p-4 border border-slate-200 rounded-xl bg-slate-50/50 flex items-start space-x-3">
                                <div class="w-10 h-10 rounded-full bg-slate-800 text-white font-bold flex items-center justify-center text-sm">ND</div>
                                <div class="flex-1">
                                    <h4 class="font-bold text-slate-800 text-sm">Aïssatou Ndiaye</h4>
                                    <p class="text-blue-600 font-medium">Chef de Projet Energies Renouvelables</p>
                                    <p class="text-slate-500 mt-1">Promo 2022 • Génie Électrique</p>
                                    <a href="mailto:aissatou.ndiaye@alumni.univ.sn" class="inline-block mt-2 text-blue-600 font-bold hover:underline">
                                        <i class="fa-solid fa-envelope mr-1"></i> aissatou.ndiaye@alumni.univ.sn
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 5: SAISIE DES NOTES (TEACHER) -->
                    <div id="tab-saisie-notes" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                            <div>
                                <h2 class="text-xl font-bold text-slate-900">Saisie des Notes des Étudiants</h2>
                                <p class="text-xs text-slate-500">Saisie et enregistrement direct des évaluations par classe</p>
                            </div>
                            <button onclick="alert('Notes sauvegardées en base de données !')" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow transition">
                                <i class="fa-solid fa-floppy-disk mr-1.5"></i> Enregistrer les notes
                            </button>
                        </div>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse text-xs">
                                <thead>
                                    <tr class="bg-slate-100 text-slate-700 uppercase font-bold border-b border-slate-200">
                                        <th class="p-3">Étudiant</th>
                                        <th class="p-3">Matricule</th>
                                        <th class="p-3 text-center">Note CC (/20)</th>
                                        <th class="p-3 text-center">Note Examen (/20)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100">
                                    <tr>
                                        <td class="p-3 font-bold text-slate-800">Diallo Amadou Tidiane</td>
                                        <td class="p-3 text-slate-500">ESP-GE-2026-01</td>
                                        <td class="p-3 text-center">
                                            <input type="number" value="15.5" min="0" max="20" class="w-20 px-2 py-1 border border-slate-300 rounded text-center font-bold">
                                        </td>
                                        <td class="p-3 text-center">
                                            <input type="number" value="14.0" min="0" max="20" class="w-20 px-2 py-1 border border-slate-300 rounded text-center font-bold">
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="p-3 font-bold text-slate-800">Sarr Mamadou</td>
                                        <td class="p-3 text-slate-500">ESP-GE-2026-02</td>
                                        <td class="p-3 text-center">
                                            <input type="number" value="13.0" min="0" max="20" class="w-20 px-2 py-1 border border-slate-300 rounded text-center font-bold">
                                        </td>
                                        <td class="p-3 text-center">
                                            <input type="number" value="12.5" min="0" max="20" class="w-20 px-2 py-1 border border-slate-300 rounded text-center font-bold">
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- TAB 6: CONFIG COEFFICIENTS (TEACHER/ADMIN) -->
                    <div id="tab-coefficients" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Configuration des Coefficients</h2>
                            <p class="text-xs text-slate-500">Pondération des unités d'enseignement pour calcul automatique</p>
                        </div>
                        <div class="space-y-3 max-w-lg text-xs">
                            <div class="flex items-center justify-between p-3 bg-slate-50 border rounded-xl">
                                <span class="font-bold text-slate-800">Électronique de Puissance</span>
                                <input type="number" value="4" class="w-16 p-1.5 border border-slate-300 rounded text-center font-bold">
                            </div>
                            <div class="flex items-center justify-between p-3 bg-slate-50 border rounded-xl">
                                <span class="font-bold text-slate-800">Programmation Microcontrôleurs</span>
                                <input type="number" value="3" class="w-16 p-1.5 border border-slate-300 rounded text-center font-bold">
                            </div>
                        </div>
                    </div>

                    <!-- TAB 7: EMPLOI DU TEMPS ENSEIGNANT -->
                    <div id="tab-edt-prof" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Planning de mes Cours</h2>
                            <p class="text-xs text-slate-500">Vos heures d'enseignement programmées pour la semaine</p>
                        </div>
                        <p class="text-xs text-slate-600">Vos cours cette semaine : <strong>12 Heures de CM / TP dispensées.</strong></p>
                    </div>

                    <!-- TAB 8: GESTION EMPLOI DU TEMPS HEBDO (RESPONSABLE) -->
                    <div id="tab-gestion-edt" class="tab-content hidden">
                        <div class="pb-4 mb-6 border-b border-slate-100">
                            <h2 class="text-xl font-bold text-slate-900">Gestion des Emplois du Temps Hebdomadaires</h2>
                            <p class="text-xs text-slate-500">Espace Responsable : Modifier la grille des horaires et salles</p>
                        </div>
                        <p class="text-xs text-slate-600">Sélectionnez une classe pour mettre à jour la grille de la semaine.</p>
                    </div>

                </div>
            </div>
        </section>

    </main>

    <!-- RECLAMATION MODAL -->
    <div id="reclamation-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 relative">
            <button onclick="closeReclamationModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">
                <i class="fa-solid fa-xmark text-xl"></i>
            </button>
            <h3 class="text-lg font-bold text-slate-900 mb-4">Nouvelle Réclamation de Note</h3>
            <form onsubmit="submitReclamation(event)" class="space-y-3 text-xs">
                <div>
                    <label class="block font-bold mb-1">Matière concernée</label>
                    <input id="rec-subject" type="text" required class="w-full p-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">Motif de la réclamation</label>
                    <textarea required rows="4" placeholder="Expliquez en détail votre demande..." class="w-full p-2 border rounded-xl"></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-600 text-white font-bold py-2.5 rounded-xl shadow">Envoyer la réclamation</button>
            </form>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="bg-slate-900 text-slate-400 text-xs py-6 mt-12 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p>© 2026 Plateforme Universitaire de Gestion des Notes & Scolarité. Tous droits réservés.</p>
        </div>
    </footer>

    <!-- JS LOGIC -->
    <script>
        let currentUser = null;
        let currentRole = 'ETUDIANT';

        function openAuthModal(role, tab) {
            currentRole = role;
            document.getElementById('auth-modal').classList.remove('hidden');
            const badge = document.getElementById('auth-badge');
            
            if(role === 'ETUDIANT') {
                badge.innerText = "Espace Étudiant";
                badge.className = "inline-block px-3 py-1 text-xs font-bold rounded-full mb-2 uppercase bg-blue-100 text-blue-700";
            } else {
                badge.innerText = "Espace Enseignant / Admin";
                badge.className = "inline-block px-3 py-1 text-xs font-bold rounded-full mb-2 uppercase bg-emerald-100 text-emerald-700";
            }

            switchAuthTab(tab);
        }

        function closeAuthModal() {
            document.getElementById('auth-modal').classList.add('hidden');
        }

        function switchAuthTab(tab) {
            const loginForm = document.getElementById('login-form');
            const regForm = document.getElementById('register-form');
            const loginBtn = document.getElementById('tab-login-btn');
            const regBtn = document.getElementById('tab-register-btn');

            if(tab === 'login') {
                loginForm.classList.remove('hidden');
                regForm.classList.add('hidden');
                loginBtn.className = "flex-1 py-2 text-xs font-bold rounded-lg transition bg-white text-slate-800 shadow-sm";
                regBtn.className = "flex-1 py-2 text-xs font-bold rounded-lg transition text-slate-500";
            } else {
                loginForm.classList.add('hidden');
                regForm.classList.remove('hidden');
                regBtn.className = "flex-1 py-2 text-xs font-bold rounded-lg transition bg-white text-slate-800 shadow-sm";
                loginBtn.className = "flex-1 py-2 text-xs font-bold rounded-lg transition text-slate-500";
            }
        }

        function handleLogin(e) {
            e.preventDefault();
            const name = currentRole === 'ETUDIANT' ? 'Amadou Tidiane Diallo' : 'Prof. Ousmane Faye';
            loginUser(name, currentRole);
        }

        function handleRegister(e) {
            e.preventDefault();
            const nom = document.getElementById('reg-nom').value;
            const prenom = document.getElementById('reg-prenom').value;
            loginUser(`${prenom} ${nom}`, currentRole);
        }

        function loginUser(name, role) {
            currentUser = { name, role };
            closeAuthModal();

            // Hide Landing, Show Dashboard
            document.getElementById('landing-section').classList.add('hidden');
            document.getElementById('dashboard-section').classList.remove('hidden');

            // Update UI User Pill
            document.getElementById('user-pill').classList.remove('hidden');
            document.getElementById('user-display-name').innerText = name;
            document.getElementById('user-display-role').innerText = role;

            document.getElementById('menu-user-name').innerText = name;
            document.getElementById('menu-user-role').innerText = role === 'ETUDIANT' ? 'Étudiant' : 'Enseignant / Admin';
            document.getElementById('avatar-initials').innerText = name.split(' ').map(n=>n[0]).join('');

            // Toggle Sidebar Menus
            if(role === 'ETUDIANT') {
                document.getElementById('student-menu').classList.remove('hidden');
                document.getElementById('teacher-menu').classList.add('hidden');
                switchTab('tab-bulletin');
            } else {
                document.getElementById('student-menu').classList.add('hidden');
                document.getElementById('teacher-menu').classList.remove('hidden');
                switchTab('tab-saisie-notes');
            }
        }

        function logout() {
            currentUser = null;
            document.getElementById('user-pill').classList.add('hidden');
            document.getElementById('dashboard-section').classList.add('hidden');
            document.getElementById('landing-section').classList.remove('hidden');
        }

        function showSection(sectionId) {
            if(sectionId === 'landing-section') {
                document.getElementById('landing-section').classList.remove('hidden');
                document.getElementById('dashboard-section').classList.add('hidden');
            }
        }

        function switchTab(tabId) {
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
            // Remove active classes on buttons
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active-nav'));

            // Show current tab
            document.getElementById(tabId).classList.remove('hidden');
            const activeBtn = document.getElementById(`btn-${tabId}`);
            if(activeBtn) activeBtn.classList.add('active-nav');
        }

        function openReclamationModal(subjectName) {
            document.getElementById('reclamation-modal').classList.remove('hidden');
            if(subjectName) {
                document.getElementById('rec-subject').value = subjectName;
            }
        }

        function closeReclamationModal() {
            document.getElementById('reclamation-modal').classList.add('hidden');
        }

        function submitReclamation(e) {
            e.preventDefault();
            alert('Votre réclamation a été transmise avec succès au responsable pédagogique !');
            closeReclamationModal();
        }
    </script>
</body>
</html>
"""

os.makedirs("github_test", exist_ok=True)
with open("github_test/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file written successfully.")
