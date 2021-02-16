import os
import sys

# CTM stands for time-marked conversation file and 
#contains a time-aligned phoneme transcription of the 
#utterances. Its format is:
# utt_id channel_num start_time phone_dur phone_id
#sox input output trim <start> <duration>

phrase = str(sys.argv[1])   #phrase to look for
phrase_words = list(phrase.split())

cur_match_ind = 0
with open("./exp/tri1/ctm") as f:
    instances = []
    for line in f.readlines():
        line = line.strip().split()
        utt_id = line[0]
        spk_id = utt_id[:15]
        start_time = float(line[2])
        dur = float(line[3])
        word = line[4]

        if cur_match_ind == len(phrase_words):#phrase found
            phrase_dur = phrase_end_time-phrase_start_time
            instance = (phrase_spk_id, phrase_utt_id, phrase_start_time, phrase_dur)
            instances.append(instance)
            cur_match_ind = 0               #search for another instance
            continue

        elif word == phrase_words[cur_match_ind]:
            if cur_match_ind==0:
                phrase_start_time = start_time
                phrase_dur = dur
                phrase_utt_id = utt_id
                phrase_spk_id = spk_id    
                cur_match_ind += 1
                phrase_end_time = start_time+dur
            else:
                if utt_id == phrase_utt_id: #the word belongs to the same utterance
                    cur_match_ind += 1
                    phrase_end_time = start_time+dur
                else:
                    cur_match_ind = 0
        else:
            cur_match_ind = 0

n = 0          
for intance in instances:
    (phrase_spk_id, phrase_utt_id, phrase_start_time, phrase_dur) = instance
    #print(instance)
    if n<10:
        num = f'0{n}'
    else:
        num = f'{n}'
    os.system('[ -d ./outputaudio ] || mkdir -p "outputaudio"')
    os.system(f'sox ./corpus/data/wav/{phrase_spk_id}/{phrase_utt_id}.wav ./outputaudio/wave{num}.wav trim {phrase_start_time} {phrase_dur}')
    n += 1