from recas.recipes import recipe
from recas.tools import bash_helper
from recas.tools import twitter

class iSarcasm(recipe.Recipe):

    license = 'Published publicly for research purposes.'
    authors = ['Silviu Vlad Oprea', 'Walid Magdy']
    paper = ('iSarcasm: A Dataset of Intended Sarcasm','https://arxiv.org/pdf/1911.03123.pdf')
    url = 'https://github.com/silviu-oprea/isarcasm'

    corpus_folder = "sarkasm_iSarkasm"

    def prepare(self):
        bash_helper.mkdir(self.corpus_folder)
        url = 'https://raw.githubusercontent.com/silviu-oprea/isarcasm/master/isarcasm.tsv'
        # download TSV with header:
        # tweet_id sarcasm_label sarcasm_type
        bash_helper.download_file(url, self.corpus_folder, "original.tsv")
        
        tsv = bash_helper.read_tsv(self.corpus_folder, "original.tsv")
        
        final = [tsv[0]] # header
        final[0].append("tweet")

        idlist = []
        for il in tsv[1:]:
            idlist.append(il[0])

        tweets = twitter.get_tweets_bulk(idlist)
        deleted = 0

        for il in tsv[1:]:
            tweet_id = int(il[0])
            if tweet_id not in tweets:
                print("{} tweet deleted".format(tweet_id))
                deleted += 1
                continue
            line = il + [tweets[tweet_id]]
            final.append(line)
        
        print("Total deleted tweets {}".format(deleted))
        bash_helper.write_tsv(final, self.corpus_folder, "final.tsv")


