class KeyTime:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp
    


class TimeMap:
    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        kt = KeyTime(value, timestamp)
        self.time_map[key].append(kt)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            recent_time = self.time_map[key][0].timestamp
            recent_val = self.time_map[key][0].value

            if recent_time > timestamp:
                return ""
            for t in self.time_map[key]:
                if t.timestamp == timestamp:
                    return t.value
                elif t.timestamp > recent_time and t.timestamp <= timestamp:
                    recent_time = t.timestamp 
                    recent_val = t.value 
            
        
            return recent_val
        else:
            return ""
            
