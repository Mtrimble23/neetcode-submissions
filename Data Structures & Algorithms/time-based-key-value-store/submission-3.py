class TimeMap:

    def __init__(self):
        # store key regularlly with tuple as value 
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            self.my_map[key].append((timestamp, value))
        else:
            self.my_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map:
            return ""

        val = self.my_map[key]

        for i in range(len(val) - 1, -1, -1):
            if val[i][0] <= timestamp:
                return val[i][1]

        return ""