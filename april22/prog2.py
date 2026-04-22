class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        
        parts = duration.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        
        self.seconds = minutes * 60 + seconds

    def get_duration(self):
        m = self.seconds // 60
        s = self.seconds % 60
        return str(m) + ":" + str(s).zfill(2)

    def __str__(self):
        return self.title + " by " + self.artist + " [" + self.get_duration() + "]"
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def total_duration(self):
        total = 0
        for t in self.tracks:
            total += t.seconds
        
        m = total // 60
        s = total % 60
        return str(m) + ":" + str(s).zfill(2)

    def longest_track(self):
        longest = self.tracks[0]
        
        for t in self.tracks:
            if t.seconds > longest.seconds:
                longest = t
        
        return longest

    def shortest_track(self):
        shortest = self.tracks[0]
        
        for t in self.tracks:
            if t.seconds < shortest.seconds:
                shortest = t
        
        return shortest

    def average_duration(self):
        total = 0
        for t in self.tracks:
            total += t.seconds
        
        avg = total // len(self.tracks)
        m = avg // 60
        s = avg % 60
        
        return str(m) + ":" + str(s).zfill(2)

    def tracks_under(self, sec):
        result = []
        
        for t in self.tracks:
            if t.seconds < sec:
                result.append(t.title)
        
        return result

    def summary(self):
        print(self.name + " | " + str(len(self.tracks)) + " tracks | Total: " 
              + self.total_duration() + " | Avg: " + self.average_duration())
tracks = [
  Track("Blinding Lights", "The Weeknd", "3:20"),
  Track("Levitating", "Dua Lipa", "3:23"),
  Track("Stay", "Kid LAROI", "2:21"),
  Track("Peaches", "Justin Bieber", "3:18"),
  Track("Good 4 U", "Olivia Rodrigo", "2:58"),
]

playlist = Playlist("Evening Vibes")

for t in tracks:
    playlist.add(t)

print(tracks[0])
print(tracks[0].seconds)

print(playlist.total_duration())
print(playlist.longest_track())
print(playlist.shortest_track())
print(playlist.average_duration())
print(playlist.tracks_under(200))
playlist.summary()