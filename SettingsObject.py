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

    def get_db_user(self):
        return str(self.configDict.get("db_user")[0])

    def get_db_password(self):
        return str(self.configDict.get("db_password")[0])

    def get_db_ip(self):
        return str(self.configDict.get("db_ip")[0])

    def get_min_port(self):
        return str(self.configDict.get("min_port")[0])

    def get_max_port(self):
        return str(self.configDict.get("max_port")[0])

    def get_event_ids(self):
        return self.configDict.get("event_ids")

    def get_station_name(self):
        return str(self.configDict.get("station_name")[0])

    def get_base_url_muoversiaroma(self):
        return str(self.configDict.get("base_url_muoversiaroma")[0])

    def get_interval_second_log(self):
        return int(self.configDict.get("interval_second_log")[0])

    def get_threshold_min(self):
        return int(self.configDict.get("threshold_min")[0])

    def get_threshold_max(self):
        return int(self.configDict.get("threshold_max")[0])

    def get_begin_simulation(self):
        import datetime
        return datetime.datetime.strptime(self.configDict.get("begin_simulation")[0], "%Y-%m-%d/%H:%M:%S")

    def get_end_simulation(self):
        import datetime
        return datetime.datetime.strptime(self.configDict.get("end_simulation")[0], "%Y-%m-%d/%H:%M:%S")

    def get_sampling_rate(self):
        return int(self.configDict.get("sampling_rate")[0])

    def get_verbosity(self):
        return int(self.configDict.get("verbosity")[0])

    def get_pause_duration(self):
        return int(self.configDict.get("pause_duration")[0])

    def get_bus_buffer(self):
        return int(self.configDict.get("bus_buffer")[0])

    def __str__(self):
        string = "Configuration:\n"
        for (key,value) in self.configDict.iteritems() :
            string += key + " : " + str(value) + "\n"
        string += "End Of Configuration\n"
        return string

    def printAll(self):
        print self
