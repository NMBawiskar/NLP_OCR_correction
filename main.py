import nlpaug.augmenter.char as nac

dataset = load_dataset('csv', data_files={'train': ['data/nl_unshuffled_train_100_000.csv'], 'test': 'data/nl_unshuffled_test_10_000.csv'})