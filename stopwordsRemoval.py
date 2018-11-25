import pandas as pd

uncapitalize = lambda s: s[:1].lower() + s[1:] if s else ''


def striplist(l):
    return [x.strip() for x in l]


def removeStopwords(text):
    from gensim.parsing.preprocessing import remove_stopwords
    # for element in textCol:
    return remove_stopwords(text)


def removeStopwordsIncludeCapitalized(text):
    # print("orginal:", text)
    from gensim.parsing.preprocessing import remove_stopwords
    import re
    # print(text)
    sentences = list(filter(None, re.split("[.!?]", text)))
    # print("\naftersplit: ", sentences)
    # print(len(sentences))
    sentences = striplist(sentences)
    sentences_new = list(map(uncapitalize, sentences))
    # print("\nafter strip: ", sentences_new)
    text_new = " ".join(sentences_new)
    return remove_stopwords(text_new)


def removeStopwordsInDF(df, ColumnName="text", removeCapitalizedStopwords=False):
    if (removeCapitalizedStopwords):
        df[ColumnName] = df[ColumnName].apply(removeStopwordsIncludeCapitalized)
    else:
        df[ColumnName] = df[ColumnName].apply(removeStopwords, removeCapitalizedStopwords)
    # for element in textCol:
    return df


if __name__ == "__main__":
    df = pd.read_csv("../rsrc/news_dataset.csv")
    print("orginal:", df.content[0])
    df5 = df.head(2)
    df_new = removeStopwordsInDF(df5, ColumnName="content", removeCapitalizedStopwords=True)
    print("output:", df_new.content[0])
