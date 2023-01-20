# Language Detector for Uzbek

This language detector recognizes the following languages:

- Uzbek Latin
- Uzbek Cyrillic
- English
- Deutch
- Spanish
- Russian
- Arabic
- French
- Italian
- Other (more than 50 languages labeled as `oth`)

We don't think that one needs to recognize that many languages using our library.

## Training and evaluation

For training, we used the following script:

```shell
>> fasttext supervised -input train.txt -output langdetect -dim 16 -minn 2 -maxn 4 -loss hs
```

For evaluation:

```shell
>> fasttext test langdetect.bin valid.txt
```

## Results

The precision of the model is 99.3%, the recall is 99.3%.
