import os

# CTM stands for time-marked conversation file and 
#contains a time-aligned phoneme transcription of the 
#utterances. Its format is:
# utt_id channel_num start_time phone_dur phone_id
#sox input output trim <start> <duration>

with open('instances.txt') as f:
    n=0
    for line in f.readlines():
        x = line.strip().split()
        utt_id = x[0]
        spk_id = utt_id[:15]
        start_time = x[2]
        dur = x[3]
        if n<10:
            num = "0"+str(n)
        else:
            num = str(n)
        os.system('[ -d ./outputaudio ] || mkdir -p "outputaudio"')
        os.system(f'sox ./corpus/data/wav/{spk_id}/{utt_id}.wav ./outputaudio/wave{num}.wav trim {start_time} {dur}')
        n += 1