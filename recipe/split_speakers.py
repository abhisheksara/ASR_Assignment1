import os, sys

with open("exp/tri1/decode_test/scoring/test_filt.txt","r") as f:
    speakers = []
    lines = f.read().splitlines()
    for line in lines:
        speaker = line.strip().split()[0][:15]
        speakers.append(speaker)
    speakers = list(set(speakers))

    for speaker in speakers:
        with open(f"exp/tri1/decode_test/scoring/{speaker}_filt.txt","a") as f2:
            for line in lines:
                cur_speaker = line.strip().split()[0][0:15]
                if cur_speaker == speaker:
                    f2.write(line+"\n")
    print([f"{speaker}_filt.txt" for speaker in speakers])
