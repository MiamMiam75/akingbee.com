from src.constants.alert_codes import *

fr = {}

default = "An error has happened while processing your request.\n" \
          "Thank you to contact kingbee.root@gmail.com " \
          "if this keep happening"

errors = {
    SQL_PROCESSING_ERROR: default,
    USER_NOT_FOUND_ERROR: "This user does not exist",
    INCORRECT_PASSWORD_ERROR: "The provided password is incorrect",
    USER_ALREADY_EXISTS_ERROR: "This user already exists",
    EMAIL_ALREADY_EXISTS_ERROR:" This emails is already used",
}



successes = {
    LOGIN_SUCCESS: ("Hello !", "You are connected"),
    REGISTER_SUCCESS: ("Welcome !", "You have been succesffully registered !"),
    PASSWORD_RESET_SUCCESS: ("", "You password has been successfully reseted !"),
    NEW_PARAMETER_SUCCESS: ("", "New parameter successfully added !"),
    NEW_BEEHOUSE_SUCCESS: ("", "Beehouse successfully created !"),
    NEW_BEEKEEPER_SUCCESS: ("", "Beekeeper successfully created !"),
    MODIFICATION_SUCESS: ("", "Modification successfully done !"),
    ACTION_PLANIFICATION_SUCCESS: ("", "Action planified with success !"),
    ACTION_SOLVED_SUCCESS: ("", "Action résolue avec succés !"),
    DELETION_SUCCESS: ("", "Suppression faites avec succés !"),
}