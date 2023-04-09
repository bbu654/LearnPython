import io
import pathlib
import os

albumTitle = ""
artist = ""
trackname = ""
albumTitl = ""
artis = ""
tracknam = ""
playlisttime = 0
numlines = 0
# PYTHON: file read and write loop recipe cookbook
Path = "C:/Users/Brice/source/Resources/spotifyLedBeatleTracks2023-04-06.txt"
nameString = '"name":'

with open(Path, "r+") as f:
    content = f.readlines()

with open("C:/Users/Brice/source/Resources/newfile.txt", "w") as g:

    # Loop through every line of text we've already read from
    # the first file.
    for line in content:

        # Also, check if the line contains the <searchString> string.
        # If it does, write the "Name" and "Direction [whatever]" line.
        # if nameString in line:
        releaseDate = ""
        releaseDat = ""
        playable = ""
        oldline = line.split(sep=",")
        numofname = 0
        for literal in oldline:
            if nameString in literal:
                numofname += 1
                if numofname == 1:
                    albumTitl = literal.strip()
                    albumTitle = albumTitl.replace("name", "album")
                elif numofname == 2:
                    artis = literal.strip()
                    artist = artis.replace("name", "group")
                elif numofname == 4:
                    tracknam = literal.strip()
                    trackname = tracknam.replace("name", "track")
            if "release_date" in literal and len(releaseDate) == 0:
                releaseDat = literal.strip()
                # "release_date": "
                # 12345678901234567
                releaseDate = releaseDat[17:-1]
            if '"duration_ms": ' in literal:
                # 234567890123456
                durationA = literal.strip()
                duration = durationA.replace('"duration_ms": ', "")
                playlisttime += int(duration)
            if 'is_playable": true' in literal:
                playable = "Playable"

        newline = (
            f"{trackname}!{artist}!{albumTitle}@{releaseDate}#{duration}${playable}"
        )
        if len(newline) > 4:
            # Write the line to the new file
            # g.write(oldline)
            lineseparator = "\n"  # os.linesep
            numlines += 1
            g.write(f"{newline}{lineseparator}")
    g.write(
        f"h:m:s={(int(playlisttime/(1000*60*60))%24)}:{int((playlisttime/(1000*60))%60)}:{int((playlisttime/1000)%60)}={playlisttime}, in millisec. {numlines=}"
    )
