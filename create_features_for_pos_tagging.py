# how to run the code
# python3 create_features_for_pos_tagging_on_raw_sentences.py.py --input Input_File_Path --output Output_File_Path
# put all the files which you want to POS Tag (test) in a folder, input should be a folder
import argparse
import os


def read_file_and_find_features(file_path):
    '''
    :param file_path: File Path contains the raw file which you want to tag
    :return features: Features of all tokens for each sentence combined for all the sentences for all the files
    '''
    features_string = ''
    with open(file_path, 'r', encoding='utf-8') as file_read:
        lines_read = file_read.readlines()
        features_string += find_features_from_sentences(lines_read)
        return features_string


def find_features_from_sentences(sentences):
    '''
    :param sentences: Sentences read from file
    :return features: Features of all tokens for each sentence combined for all the sentences
    '''
    prefix_len = 4
    suffix_len = 7
    features = ''
    for sentence in sentences:
        sentence_features = ''
        if sentence.strip():
            tokens_split = [token for token in sentence.strip().split() if token.strip()]
            for token in tokens_split:
                sentence_features += token + '\t'
                for i in range(1, prefix_len + 1):
                    sentence_features += affix_feats(token, i, 0) + '\t'
                for i in range(1, suffix_len + 1):
                    sentence_features += affix_feats(token, i, 1) + '\t'
                sentence_features = sentence_features + 'LESS\n' if len(token) <= 4 else sentence_features + 'MORE\n'
        if sentence_features.strip():
            features += sentence_features + '\n'
    return features


def affix_feats(token, length, type_aff):
    '''
    :param line: extract the token and its corresponding suffix list depending on its length
    :param token: the token in the line
    :param length: length of affix
    :param type: 0 for prefix and 1 for suffix
    :return suffix: returns the suffix
    '''
    if len(token) < length:
        return 'NULL'
    else:
        if type_aff == 0:
            return token[:length]
        else:
            return token[len(token) - length:]


def write_text_to_file(out_path, data):
    '''
    :param out_path: Enter the path of the output file
    :param data: Enter the token features of sentence separated by a blank line
    :return: None
    '''
    with open(out_path, 'w+', encoding='utf-8') as fout:
        fout.write(data + '\n')
        fout.close()


def main():
    '''
    Pass arguments and call functions here.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='inp', help="Add the input file path")
    parser.add_argument('--output', dest='out', help="Add the output file where the features will be saved")
    args = parser.parse_args()
    features = read_file_and_find_features(args.inp)
    write_text_to_file(args.out, features)


if __name__ == '__main__':
    main()
