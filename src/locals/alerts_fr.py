from src.constants.alert_codes import *

fr = {}

default = "Une erreur est survenue lors du traitement de votre " \
          "demande, merci de contacter kingbee.root@gmail.com " \
          "si l'erreur persiste."

errors = {
    SQL_PROCESSING_ERROR: default,
    USER_NOT_FOUND_ERROR: "Cet utilisateur n'existe pas",
    INCORRECT_PASSWORD_ERROR: "Le mot de passe fournit est incorrect",
    USER_ALREADY_EXISTS_ERROR: "Cet utilisateur existe déjà",
    EMAIL_ALREADY_EXISTS_ERROR:" Cet email est déjà utilisé",
}



successes = {
    LOGIN_SUCCESS: ("Bonjour !", "Vous êtes connecté"),
    REGISTER_SUCCESS: ("Bienvenue !", "Vous êtes bien enregistré"),
    PASSWORD_RESET_SUCCESS: ("", "Votre mot de passe a bien été réinitialisé"),
    NEW_PARAMETER_SUCCESS: ("", "Nouveau paramètre ajouté avec succés"),
    NEW_BEEHOUSE_SUCCESS: ("", "Ruche créée avec succés !"),
    NEW_BEEKEEPER_SUCCESS: ("", "Apiculteur créé avec succés !"),
    MODIFICATION_SUCESS: ("", "Modification faites avec succés !"),
    ACTION_PLANIFICATION_SUCCESS: ("", "Action planifiée avec succés !"),
    ACTION_SOLVED_SUCCESS: ("", "Action résolue avec succés !"),
    DELETION_SUCCESS: ("", "Suppression faites avec succés !"),
}