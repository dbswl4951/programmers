def chageMelody(melody):
    melody=melody.replace('A#','a')
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    return melody

def solution(m, musicinfos):
    m=chageMelody(m)
    result=None
    dic=dict()
    for musicinfo in musicinfos:
        start,end,title,melody=musicinfo.split(',')
        startTime=start.split(':')
        endTime=end.split(':')
        time=int(endTime[0])*60+int(endTime[1])-int(startTime[0])*60-int(startTime[1])
        melody=chageMelody(melody)
        melody=melody*(time//len(melody))+melody[:time%len(melody)]
        dic[melody]=title

    for song in dic.keys():
        if m in song:
            if result==None: result=song
            elif len(result)<len(song): result=song
    if result!=None:
        return dic[result]
    return '(None)'

#print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
#print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#print(solution('ABBC#F#',['12:10,12:13,HI,ABBC#F#']))