from collections import defaultdict

def solution(m, musicinfos):
    answer = "(None)"
    
    songList = defaultdict(list)
    for music in musicinfos :
        stime,etime,title,melody = music.split(",")
        stime = stime.split(":")
        etime = etime.split(":")
        time = ((int(etime[0])*60) + int(etime[1]))  - ((int(stime[0])*60) + int(stime[1]))
        songList[title].append(time+1)
        songList[title].append(songSplit(melody))
        
    songTime = 0
    for k,v in songList.items() :
        mSong = songSplit(m)
        song = []
        if v[0] < len(v[1]) :
            song = v[1][:v[0]]
        else :
            song = v[1]*v[0]
        
        for i in range(len(song)) :
             if( mSong[0] == song[i] and ((i+len(mSong)) <= len(song)) ) :
                    if mSong == song[i:i+len(mSong)] :
                        if songTime < v[0] :
                            answer = k
                            songTime = v[0]
                            break
    return answer

def songSplit(song) :
    tmp = []
    for s in song :
        if(s == "#") :
            t = tmp.pop()
            tmp.append(t+s)
        else :
            tmp.append(s)
    return tmp