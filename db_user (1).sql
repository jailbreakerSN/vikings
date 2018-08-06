-- phpMyAdmin SQL Dump
-- version 4.1.4
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Lun 06 Août 2018 à 11:56
-- Version du serveur :  5.6.15-log
-- Version de PHP :  5.5.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `db_user`
--

-- --------------------------------------------------------

--
-- Structure de la table `alembic_version`
--

CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('64847a82e6ad');

-- --------------------------------------------------------

--
-- Structure de la table `est_cree_user`
--

CREATE TABLE IF NOT EXISTS `est_cree_user` (
  `id_Utilisateur` int(11) NOT NULL,
  `id_Projet` int(11) NOT NULL,
  `date_creation_est_Cree_User` date NOT NULL,
  PRIMARY KEY (`id_Utilisateur`,`id_Projet`,`date_creation_est_Cree_User`),
  KEY `ix_est_cree_user_id_Projet` (`id_Projet`),
  KEY `ix_est_cree_user_id_Utilisateur` (`id_Utilisateur`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `est_cree_user`
--

INSERT INTO `est_cree_user` (`id_Utilisateur`, `id_Projet`, `date_creation_est_Cree_User`) VALUES
(1, 1, '2018-06-06'),
(3, 2, '0000-00-00'),
(3, 3, '2018-06-11'),
(3, 5, '2018-07-04');

-- --------------------------------------------------------

--
-- Structure de la table `est_mene_user`
--

CREATE TABLE IF NOT EXISTS `est_mene_user` (
  `id_Utilisateur` int(11) NOT NULL,
  `id_Projet` int(11) NOT NULL,
  PRIMARY KEY (`id_Utilisateur`,`id_Projet`),
  KEY `ix_est_mene_user_id_Utilisateur` (`id_Utilisateur`),
  KEY `ix_est_mene_user_id_Projet` (`id_Projet`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `est_mene_user`
--

INSERT INTO `est_mene_user` (`id_Utilisateur`, `id_Projet`) VALUES
(1, 1),
(2, 1),
(3, 1),
(3, 3),
(3, 5);

-- --------------------------------------------------------

--
-- Structure de la table `etape`
--

CREATE TABLE IF NOT EXISTS `etape` (
  `id_Etape` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `objectif` varchar(255) DEFAULT NULL,
  `importance` int(11) DEFAULT NULL,
  `code_Etape` text,
  `valide_Etape` tinyint(1) DEFAULT NULL,
  `version_Etape` varchar(30) DEFAULT NULL,
  `id_Langage` int(11) DEFAULT NULL,
  `id_Projet` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Etape`),
  KEY `ix_etape_id_Langage` (`id_Langage`),
  KEY `ix_etape_id_Projet` (`id_Projet`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Contenu de la table `etape`
--

INSERT INTO `etape` (`id_Etape`, `nom`, `objectif`, `importance`, `code_Etape`, `valide_Etape`, `version_Etape`, `id_Langage`, `id_Projet`) VALUES
(1, 'Extraction Données Test', 'Nous allons dans un premier temps fixer les utilisateurs dont les données vont constituer notre jeu de test', 10, 'create table algorithmisation.subset_of_cdr_larger as select distinct M.caller_msisdn from (select S.caller_msisdn, T.region from algorithmisation.cdr_datas S left join algorithmisation.antennas T on (S.ms_location=T.id_cellule) where region="Dakar") M where rand()<=0.1 distribute by rand() sort by rand() limit 100000";', 0, '1.0', 1, 1),
(2, 'Extraction données  Novembre', 'Définir les données des utilisateurs concernés pour le mois de Novembre', 10, 'create table algorithmisation.subset_of_cdr_November as select * from algorithmisation.cdr_datas where caller_msisdn in table algorithmisation.subset_of_cdr_larger ";\r\n', 0, '1.0', 1, 1),
(3, 'Extraction données de Juin', 'Définir les données des utilisateurs concernés pour le mois de', 10, 'create table algorithmisation.subset_of_cdr_July as select * from algo_july.cdr_datas where caller_msisdn in table algorithmisation.subset_of_cdr_larger ";', 0, '1.0', 1, 1),
(4, 'Acquisition et prétraitement des données', 'Extraction et pre processing des données cdr', 5, NULL, 0, '1.0', 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `langage`
--

CREATE TABLE IF NOT EXISTS `langage` (
  `id_Langage` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_Langage`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `langage`
--

INSERT INTO `langage` (`id_Langage`, `nom`) VALUES
(1, 'Hive'),
(2, 'Scala');

-- --------------------------------------------------------

--
-- Structure de la table `projet`
--

CREATE TABLE IF NOT EXISTS `projet` (
  `id_Projet` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `description_Projet` text,
  PRIMARY KEY (`id_Projet`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Contenu de la table `projet`
--

INSERT INTO `projet` (`id_Projet`, `nom`, `description_Projet`) VALUES
(1, 'Mouvement de Population', 'Ce projet a pour objectif principal de mettre en place un process de détermination de mouvement de population à travers les données CDR (Call Detail Record). Par un procédé d''extraction et d''application de divers algorithmes sur les données d''appels de mois différents, nous allons essayer d''établir les mouvements de populations enregistrés au cours de ces périodes.'),
(2, 'Taux d''alphabétisation', 'Ce projet à pour objectif de faire une corrélation entre les données d''appels et le taux d''alphabétisation d''une ville grâce au nombre de SMS envoyés dans cette zone. '),
(3, 'Taux de Natalité', 'Ce projet a pour ambition de mettre en place un algorithme qui permettra de déterminer à partir des données CDR le taux de natalité d''une zone donnée.'),
(5, 'Etude de la propagation de Ebola', 'L''objet de ce projet est de faire une analyse et traitement des données CDR pour essayer de trouver une corrélation entre les mouvements de population et la propagation de la maladie d''Ebola');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id`, `username`, `email`, `password`, `firstname`, `lastname`) VALUES
(1, 'Jailbreaker', 'dameleprinc@gmail.com', 'pbkdf2:sha256:50000$ZfbnOxAF$79c51a5ab7a69d5fed71e2a57740814807e77f5c065a906decad5662c2e900a3', 'Fallou', 'Dieng'),
(2, 'Mseesay', 'mseesay024@gmail.com', 'pbkdf2:sha256:50000$6WDUd1J6$f153568b14ef2278ff8934ce77b026c06393cd2db954bb679fb4211e2ce94b7e', 'Mamadou', 'Cisse'),
(3, 'JailbreakerSN', 'dameleprince@gmail.com', 'pbkdf2:sha256:50000$lgmkEwyk$cb74e69c86119b1d8f485baef46dab7f6f0d06e259ded3b0ceb31ae1e1545aec', 'Dame', 'NDIAYE');

-- --------------------------------------------------------

--
-- Structure de la table `variable_env`
--

CREATE TABLE IF NOT EXISTS `variable_env` (
  `id_Variable_Env` int(11) NOT NULL AUTO_INCREMENT,
  `libelle_Variable_Env` varchar(30) DEFAULT NULL,
  `valeur_Variable_Env` varchar(255) DEFAULT NULL,
  `id_Etape` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Variable_Env`),
  KEY `ix_variable_env_id_Etape` (`id_Etape`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
