def refine_sharp(notes):
    return notes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def get_length(start_time, end_time):
    start_hour, start_minute = [int(x) for x in start_time.split(':')]
    end_hour, end_minute = [int(x) for x in end_time.split(':')]

    return (end_hour - start_hour) * 60 + (end_minute - start_minute)


def solution(m, musicinfos):
    refined = []

    for music_info in musicinfos:
        start_time, end_time, name, notes = music_info.split(',')
        played_length = get_length(start_time, end_time)
        played_notes = refine_sharp(notes)

        while len(played_notes) < played_length:
            played_notes += played_notes
        played_notes = played_notes[0: played_length]
        refined.append([name, played_length, played_notes])

    refined.sort(key=lambda x: x[1], reverse=True)

    remove_sharp_m = refine_sharp(m)

    for info in refined:
        if remove_sharp_m in info[2]:
            return info[0]

    return "(None)"
