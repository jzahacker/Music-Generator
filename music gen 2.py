import random

class Song:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

class Album:
    def __init__(self, title, songs):
        self.title = title
        self.songs = [Song(song) for song in songs]

    def __repr__(self):
        return self.title

class Artist:
    def __init__(self, name, albums):
        self.name = name
        self.albums = [Album(album['title'], album['songs']) for album in albums]

    def __repr__(self):
        return self.name

class RandomSongGenerator:
    def __init__(self, artists):
        self.artists = [Artist(artist['name'], artist['albums']) for artist in artists]

    def get_random_song(self):
        artist = random.choice(self.artists)
        album = random.choice(artist.albums)
        song = random.choice(album.songs)
        return f"Artist:{artist.name}Album:{album.title}Song:{song}"



artists_data = {
    "Nicki Minaj": {
        "Pink Friday": ["I'm the Best", "Roman's Revenge", "Did It On'em", "Right Thru Me", "Fly", "Save Me", "Moment 4 Life", "Check It Out", "Blazin'", "Here I Am", "Dear Old Nicki", "Your Love", "Last Chance", "Super Bass", "Blow Ya Mind", "Muny", "Catch me", "Girls Fall Like Dominoes", "BedRock"],
        "Pink Friday: Roman Reloaded": ["Up in Flames", "Freedom", "Hell Yeah", "High School", "I'm Legit", "I Endorse These Str*ppers", "The Boys", "Va Va Voom", "Roman Holiday", "C*me On a Cone", "I Am Your Leader", "Beez in the Trap","HOV Lane", "Roman Reloaded", "Champion", "Right By My Side", "S*x in the Lounge", "Starships", "Pound the Alarm", "Whip it","Automatic","Beautiful Sinner","Marilyn Monroe","Young Forever","Fire Burns","Gun Shot","Stupid H*e"],
        "The Pinkprint": ["All Things Go", "I Lied", "The Crying Game","Get On Your Knees", "Feeling Myself", "Only", "Want Some More", "Four Door Aventador", "Favorite", "Buy a Heart", "Trini Dem Girls", "Anaconda", "The Night Is Still Young", "Pills N Potions", "Bed of Lies", "Grand Piano","Big Daddy", "Shanghai","Win Again", "Truffle Butter", "Mona Lisa", "Put you In a Room","Wamables"],
        "Queen": ["Ganja Burn", "Majesty", "Barbie Dreams", "Rich S*x","Hard White", "Bed", "Thought I Knew You", "Run & Hide", "Chun Swae", "Chun-Li", "LLC", "Good Form", "Nip Tuck", "2 Lit 2 Late Interlude", "Come See About Me", "Sir", "Miami", "Coco Chanel", "Inspirations Outro"],
        "Pink Friday 2": ["Are You Gone Already", "Barbie Dangerous", "FTCU", "Beep Beep", "Fallin 4 U", "Let Me Calm Down", "RNB", "Pink Birthday", "Needle", "Cowgirl","Everyday", "Big Difference", "Red Ruby Da Sleeze", "Forward From Trini", "Pink Friday Girls", "Super Freaky Girl", "Bahm Bahm", "My Life", "Nicki Hendrix", "Blessings", "Last Time I Saw You", "Just The Memories", "Love Me Enough", "Press Play"]
    },
    "Ariana Grande": {
        "Yours Truly": ["Honeymoon Avenue", "Baby I", "Right There", "Tattooed Heart", "Lovin' It", "Piano", "Daydreamin'", "The Way", "You'll Never Know", "Almost Is Never Enough", "Popular Song", "Better Left Unsaid"],
        "My Everything": ["Intro", "Problem", "One Last Time", "Why Try", "Break Free", "Best Mistake", "Be My Baby", "Break Your Heart Right Back", "Love Me Harder", "Just A Little Bit Of Your Heart", "Hands on Me", "My Everything","Bang Bang", "Only 1", "You Don't Know Me"],
        "Dangerous Woman":["Moonlight", "Dangerous Woman", "Be Alright","Into You", "Side To Side", "Let Me Love You", "Greedy", "Leave Me Lonely", "Everyday", "Sometimes", "I Don't Care", "Bad Decisions", "Touch It", "Knew Better/Forever Boy", "Thinking Bout You"],
        "Sweetener":["raindrops", "blazed", "the light is coming", "R.E.M","God is a woman", "sweetener", "successful", "everytime", "breathin", "no tears left to cry", "borderline", "better off", "goodnight n go", "pete davidson", "get well soon"],
        "thank u, next": ["imagine", "needy", "NASA", "bloodline", "fake smile", "bad idea", "make up", "ghostin","in my head", "7 rings", "thank u, next", "break up with your girlfriend, i'm bored"],
        "Positions": ["shut up", "34+35", "motive", "just like magic", "off the table", "six thirty", "safety net", "my hair", "nasty", "west side", "love language", "positions", "obvious", "pov", "someone like u", "test drive","worst behaviour", "main thing"],
        "eternal sunshine":["intro (end of the world)", "bye", "don't wanna break up again", "Saturn Returns Interlude", "eternal sunshine", "supernatural", "true story", "the boy is mine", "yes, and?","we can't be friends (wait for your love)", "i wish i hated you", "imperfect for you", "ordinary things"]

    },
    "Doja Cat": {
        "Amala": ["Go To Town", "Cookie Jar", "Roll With Us", "Wine Pon You", "Fancy", "Wild Beach", "Morning Light", "Candy", "Game'", "Casual", "Down Low", "Body Language", "All Nighter", "Juicy", "Tia Tamera", "MOOO!"],
        "Hot Pink": ["Cyber S*x", "FWon't Bite", "Rules", "Bottom B*tch", "Say So", "Like That", "Talk Dirty", "Addiction", "Streets", "Shine", "Better Than Me","Juicy feat. Tyga)", "Say So (feat. Nicki Minaj)"],
        "Planet Her":["Woman", "Naked", "Payday","Get into It (Yuh)", "Need To Know", "I Don't Do Drugs", "Love To Dream", "You Right", "Been Like This", "Options", "Ain't Shit", "Imagine", "Alone", "Kiss Me More", "You Right (Extended) Feat. The Weeknd", "Up And Down","Tonight", "Ride","Why Why"],
        "Scarlet":["ACKNOWLEDGE ME", "DISRESPECTFUL", "URRRGE!!!!!!!!!!!", "OKLOSER","MASC", "P*SS", "HEADHIGH", "Paint The Towen Red", "Demons", "Wet V*gina", "F**k The Girls (FTG)", "Ouchies", "97", "Gun", "Go Off", "Shutcho", "Agora Hills", "Can't Wait", "Often", "Love Life", "Skull And Bones", "Attention", "Balut", "WYM Freestyle"],
    }
}

generator = RandomSongGenerator(artists_data)
print(generator.get_random_song())