import requests

class Gotify:
    def __init__(self, config):
        self.name = config.get_name().split()[-1]
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object('gcode')     

        # configuration
        self.token = config.get('token')
        self.endpoint = config.get('endpoint')
        self.protocol = config.get('protocol')
        self.verify = config.get('verify', True)

        self.headers = {
            'Content-Type': 'application/json'
        }
        self.url = self.protocol + '://' + self.endpoint + '/message?token=' + self.token

        # Register commands
        self.gcode.register_command(
            "GOTIFY_SEND", 
            self.cmd_GOTIFY_SEND, 
            desc=self.cmd_GOTIFY_SEND_help)

    cmd_GOTIFY_SEND_help = "Sending message to Gotify server"
    def cmd_GOTIFY_SEND(self, params):
        message = params.get('MSG', '')
        title = params.get('TITLE', '')
        priority = params.get('PRIORITY', 5)

        # Priorities
        # 0 - Silent push
        # 5 - Audiable push

        if message == '':
            self.gcode.respond_info('Klipper Push Notification module for Gotify.\nUSAGE: GOTIFY_SEND MSG="message" TITLE="title" PRIORITY="priority (Audiable 5 (Default), Silent 0)"')
            return

        self.gcode.respond_info("Sending message: " + title + " - " + message)

        data = {
            'priority': priority,
            'title': title,
            'message': message
        }

        try:
            verify = self.verify if self.protocol == 'https' else False
            response = requests.post(url=self.url, headers=self.headers, json=data, verify=verify)
            self.gcode.respond_info(str(response.text))
        except requests.exceptions.ConnectionError as e:
            raise self.gcode.error("Gotify: Connection Error " + str(e))

def load_config(config):
    return Gotify(config)