# Spongebob Caser

## Intro

This python program, when given a text input, converts the text into the "Spongebob case" see [here](https://i0.kym-cdn.com/photos/images/original/001/253/025/34d.jpg) for an example.

The input is case-insensitive, and all punctuation is ignored. The text is parsed word by word.

## Specifications
I created a few rules for the Spongebob case to follow, in order to improve humor, zaniness and readability.

### Starting with lowercase
Each word starts with a lowercase letter just because I think it's funnier. For example, there's
> DoN't Do ThAT

vs
> dOn'T dO tHaT

I believe it's fair to assert that the second is objectively more hilarious.

### `I` and `l` confusion
Originally, I wasn't satisfied with just having every other letter be capitalized, because it created confusion between the capitol "I" and the lowercase "l" in non-monospaced fonts. For example, by sponge-casing the word "lillypad" looks something like this:
> lIlLyPaD

Awful, I know. Or this alternative, if starting with a capital
> LiLlyPad

Better, but still not ideal. For this reason I created the following rules: that every `i` must be kept lowercase and that every `l` must be kept uppercase

However, because of the possibility of a word to have little to no capital letters due to the starting-lowercase rule (ex: "limit" or "fitNeSs"), I added the rule that the letter after any `i` should be capitalized, despite the other rules, provided this letter is also not an `i`

### All Rules
The Spongebob Casing Laws are the following (Later rules trump earlier rules)

1. Each word must begin with a lowercase letter, and alternates "lowercase-uppercase" until a word break is found.
2. Each `l` must be kept uppercase.
3. Each letter after an `i` must be capitalized.
4. Each  `i` must be kept lowercase 