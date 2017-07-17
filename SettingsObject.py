class SettingsObject(object):

    def __init__(self, dict = None, deserialize=None):
        self.configDict = dict
        if(deserialize != None):
            import json
            self.configDict = json.loads(deserialize)

    def serialize(self):
        import json
        return json.dumps(self.configDict)

    def get_dbname(self):
        return str(self.configDict.get("db_name")[0])

    def get_threads_number(self):
        return int(self.configDict.get("threads")[0])

    def get_min_idaudio(self):
        return int(self.configDict.get("min_idaudio")[0])

    def get_max_idaudio(self):
        return int(self.configDict.get("max_idaudio")[0])

    def get_path_music(self):
        return str(self.configDict.get("path_music")[0])

    def get_m2o_reloaded_url(self):
        return str(self.configDict.get("m2o_reloaded_url")[0])

    def get_m2o_player_url(self):
        return str(self.configDict.get("m2o_player_url")[0])

    def get_db_engine(self):
        return str(self.configDict.get("db_engine")[0])

    def get_station_name(self):
        return str(self.configDict.get("station_name")[0])

    def get_base_url_muoversiaroma(self):

        return str(self.configDict.get("base_url_muoversiaroma")[0])

    def __str__(self):
        string = "Configuration:\n"
        for (key,value) in self.configDict.iteritems() :
            string += key + " : " + str(value) + "\n"
        string += "End Of Configuration\n"
        return string

    def printAll(self):
        print self
