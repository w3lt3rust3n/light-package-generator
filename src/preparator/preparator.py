class Preparator:
    LPG_DIR = ".lpg/"
    CONFIG_DIR = ".lpg/config"
    
    def __init__(self, lang):
        self.lang = lang

    def __load_conf_file(self):
        pass
    
    def init_preparator(self, lang):
        print("Hello from init_preparator")