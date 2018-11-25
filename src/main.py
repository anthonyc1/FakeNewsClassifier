import pandas as pd
import stopwordsRemoval



def main():
    df = pd.read_csv("../rsrc/news_dataset.csv")
    print("orginal:", df.content[0])
    df5 = df.head(2)
    print(df5)
    df_new = stopwordsRemoval.removeStopwordsInDF(df5, ColumnName="content", removeCapitalizedStopwords=True)
    print("output", df_new.content[1])


if __name__ == "__main__":
    main()
