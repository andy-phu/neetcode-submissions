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
            # for t in self.time_map[key]:
            #     if t.timestamp == timestamp:
            #         return t.value
            #     elif t.timestamp > recent_time and t.timestamp <= timestamp:
            #         recent_time = t.timestamp 
            #         recent_val = t.value 
            arr = self.time_map[key]

            l,r = 0, len(arr) - 1


            while l<=r:
                mid = (l+r) // 2
                mid_arr = arr[mid]
                if mid_arr.timestamp <= timestamp:
                    recent_val = mid_arr.value
                    recent_time = mid_arr.timestamp
                    l = mid + 1 
                elif mid_arr.timestamp > timestamp:
                    r = mid -1 

        
            return recent_val
        else:
            return ""
            
