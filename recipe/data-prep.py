import os

CUR_DIR = os.getcwd()
DATA_DIR = r"corpus/data"

TRANSCRIPTIONS_FILE = r"corpus/data/transcriptions.txt"
DATAINFO_FILE = r"corpus/data/data-info.txt"

train_speakers = []
test_speakers = []
truetest_speakers = []

with open(DATAINFO_FILE,'r') as f:
    for line in f.readlines():
        words = line.strip().split()
        if words[0]=="train":
            for speaker in words[1:]:
                train_speakers.append(speaker)
        elif words[0]=="test":
            for speaker in words[1:]:
                test_speakers.append(speaker)
        elif words[0]=="truetest":
            for speaker in words[1:]:
                truetest_speakers.append(speaker)
        else:
            print("oops")
    print(f"There are {len(train_speakers)} speakers in the training set, {len(test_speakers)} speakers in the test set, {len(truetest_speakers)} speakers in the truetest set,")

#creating directories of train, test, truetest
os.mkdir(os.path.join(DATA_DIR,r"train"))
os.mkdir(os.path.join(DATA_DIR,r"test"))
os.mkdir(os.path.join(DATA_DIR,r"truetest"))

TRAIN_TEXT_FILE = os.path.join(DATA_DIR,r"train/text")
TEST_TEXT_FILE = os.path.join(DATA_DIR,r"test/text")
TRUETEST_TEXT_FILE = os.path.join(DATA_DIR,r"truetest/text")

TRAIN_UTT2SPK_FILE = os.path.join(DATA_DIR,r"train/utt2spk")
TEST_UTT2SPK_FILE = os.path.join(DATA_DIR,r"test/utt2spk")
TRUETEST_UTT2SPK_FILE = os.path.join(DATA_DIR,r"truetest/utt2spk")

#Create utt2spk and text files
with open(TRANSCRIPTIONS_FILE,'r') as in_file, open(TRAIN_TEXT_FILE, 'w') as train_text, open(TEST_TEXT_FILE, 'w') as test_text, open(TRUETEST_TEXT_FILE, 'w') as truetest_text, open(TRAIN_UTT2SPK_FILE, 'w') as train_utt2spk, open(TEST_UTT2SPK_FILE, 'w') as test_utt2spk, open(TRUETEST_UTT2SPK_FILE, 'w') as truetest_utt2spk:
    count = 0
    for line in in_file.readlines():
        words = line.strip().split()
        utt_id = words[0]
        spk_id = utt_id[:15]
        text_line = line
        utt2spk_line = ' '.join([utt_id,spk_id])+'\n'
        if spk_id in train_speakers:
            train_text.write(line)
            train_utt2spk.write(' '.join([utt_id,spk_id])+'\n')
        elif spk_id in test_speakers:
            test_text.write(line)
            test_utt2spk.write(utt2spk_line)
        elif spk_id in truetest_speakers:
            truetest_text.write(line)
            truetest_utt2spk.write(utt2spk_line)
        else:
            print("Speaker ID does not match")
        count+=1
    print(f"There are {count} number of utterances")
    print("Text, utt2spk files created for train, test and truetest sets")

WAV_FOLDER_PATH = os.path.join(DATA_DIR, r"wav")

TRAIN_WAV_FILE = os.path.join(DATA_DIR,r"train/wav.scp")
TEST_WAV_FILE = os.path.join(DATA_DIR,r"test/wav.scp")
TRUETEST_WAV_FILE = os.path.join(DATA_DIR,r"truetest/wav.scp")

with open(TRAIN_WAV_FILE, 'w') as train_wav, open(TEST_WAV_FILE, 'w') as test_wav, open(TRUETEST_WAV_FILE, 'w') as truetest_wav:
    for wav_spk_id in os.listdir(WAV_FOLDER_PATH):
        wav_spk_path = os.path.join(WAV_FOLDER_PATH,wav_spk_id)
        for wav_file in os.listdir(wav_spk_path):
            wav_file_path = os.path.join(wav_spk_path, wav_file)
            if wav_spk_id in train_speakers:
                train_wav.write(' '.join([wav_file.rsplit('.', 1)[0], wav_file_path])+'\n')
            elif wav_spk_id in test_speakers:
                test_wav.write(' '.join([wav_file.rsplit('.', 1)[0], wav_file_path])+'\n')
            elif wav_spk_id in truetest_speakers:
                truetest_wav.write(' '.join([wav_file.rsplit('.', 1)[0], wav_file_path])+'\n')
            else:
                print("Speaker ID in wav not found")
    print("Wave file created for train, test, truetest")
