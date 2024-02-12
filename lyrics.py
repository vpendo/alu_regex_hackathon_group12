import re

# Different song lyrics
custom_lyrics = """[Verse 1] I took a walk around the world to
Ease my troubled mind
[Verse 2] I left my body lying somewhere
In the sands of time
[Verse 3] But I watched the world float
To the dark side of the moon
[Outro] I feel there's nothing I can do"""

# Regex pattern to match song lyrics
custom_lyrics_pattern = re.compile(r'\[Verse \d+\].+')

# Test to see if pattern matches the custom lyrics
if len(custom_lyrics_pattern.findall(custom_lyrics)) != 0:
    print(f"Matches: {custom_lyrics_pattern.findall(custom_lyrics)}")
else:
    print(f"The custom lyrics have no matches")
