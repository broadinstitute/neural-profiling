import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from pycytominer import aggregate, annotate, normalize, feature_select, cyto_utils
from cytominer_eval import evaluate
from cytominer_eval.transform import metric_melt
from sklearn.decomposition import PCA

def prec_mean(res_pre):
    pr_av = []
    for k in res_pre.k.unique():
        pr_av.append(res_pre.query("k==@k").mean().tolist())
    res = pd.DataFrame(pr_av, columns=["k", "precision", "recall"])
    return res

def hitk_prep(res):
    score = [x/len(res[0]) for x in res[1].values()]
    return score


class evaluation():


    def __init__(self, df, meta_path = None, prefix = 'eff', features = None, meta_features = None, top_moa = 20, verbose = False):
        self.df = df
        self.prefix = prefix

        if meta_path == None:
            meta_path = '/Users/mbornhol/git/neural-profiling/pre-trained/data-prep/02_index_preperation/repurposing_info_external_moa_map_resolved.tsv'
        self.df_meta = pd.read_csv(meta_path, sep='\t')
        self.df_meta = self.df_meta[['broad_sample', 'moa']]
        self.df_meta.rename(columns={'broad_sample': 'Metadata_broad_sample', 'moa': 'Metadata_moa'}, inplace=True)

        if features == None:
            self.features = [f for f in self.df.columns if f.startswith(self.prefix)]
            print('{} features were identified'.format(len(self.features)))
        else:
            self.features = features

        if meta_features == None:
            self.meta_features = [feat for feat in self.df.columns if feat not in self.features]
        else:
            self.meta_features = meta_features

        self.top_moa = self.df.Metadata_moa.value_counts()[1:top_moa].keys().tolist()
        if verbose:
            print("Succesfully initalized your data")
            print(self.df.head())
            print('List of Metadata features:\n', self.meta_features)


    def norm_agg(self, method = 'spherize'):
        if method != None:
            normalized = normalize(
                profiles=self.df,
                features=self.features,
                samples="Metadata_broad_sample == 'DMSO'",
                method=method,
                output_file='none'
            )
        else:
            normalized = self.df

        agg = aggregate(
            normalized,
            strata=["Metadata_broad_sample"],
            features=self.features
        )

        consensus = pd.merge(agg, self.df_meta, how='left', on=['Metadata_broad_sample'])

        return consensus



    def eval(self, con, operation = 'enrichment', eval_range = 'standard'):
        if operation == 'precision_recall':
            con = con[con["Metadata_broad_sample"] != 'DMSO']
            if eval_range == 'standard':
                eval_range = [5, 10, 15, 20, 25, 30, 40, 50]
        elif operation == 'enrichment':
            if eval_range == 'standard':
                eval_range = np.arange(0.995, 0.96, -0.005)
        elif operation == 'hitk':
            con = con[con["Metadata_broad_sample"] != 'DMSO']
            if eval_range == 'standard':
                eval_range = list(np.arange(0,101,1))
        else:
            print('error input must be one of [precision_recall, enrichment, hitk]')
            return None

        if con.shape[0] > 2000:
            print("dude that gonna take long")
            print(con.shape)

        res = evaluate(
            profiles=con,
            features=self.features,
            meta_features=['Metadata_broad_sample', "Metadata_moa"],
            replicate_groups=["Metadata_moa"],
            groupby_columns=['Metadata_broad_sample'],
            operation=operation,
            similarity_metric="pearson",
            precision_recall_k=eval_range,
            enrichment_percentile=eval_range,
            hitk_percent_list=eval_range
        )

        # if operation == 'precision_recall':
        #     top_prc = res[res['Metadata_moa'].isin(self.top_moa)].reset_index(drop=True)
        #     pr_av = []
        #     for k in top_prc.k.unique():
        #         pr_av.append(top_prc.query("k==@k").mean().tolist())
        #     res = pd.DataFrame(pr_av, columns=["k", "precision", "recall"])
        # if operation == 'hitk':
        #     size = len(self.df)
        #     ls = list(res[1].values())
        #     res = (res[0], [x/size for x in ls])
        return res

class plotting():
    def accuracy(title, index1, label_1, index2 = None, label_2 = None, index3 = None, label_3 = None,):
        plt.style.use({'figure.facecolor': 'white'})
        plt.rcParams.update({'font.size': 15})
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title(title)
        plt.xlabel('epoch')
        ax2 = ax.twinx()

        acc_path = '/Users/mbornhol/git/neural-profiling/training/results/accuracy/'
        acc1 = pd.read_csv(acc_path + index1 + '.csv')
        ax.plot(acc1['loss'], 'r-', label=label_1)
        ax2.plot(acc1['acc'], 'r', linestyle='dashdot')
        ax2.plot(acc1['val_acc'], 'r', linestyle='dashed')

        if index2 != None:
            acc2 = pd.read_csv(acc_path + index2 + '.csv')
            ax.plot(acc2['loss'], 'g-', label=label_2)
            ax2.plot(acc2['acc'], 'g', linestyle='dashdot')
            ax2.plot(acc2['val_acc'], 'g', linestyle='dashed')

        if index3 != None:
            acc3 = pd.read_csv(acc_path + index3 + '.csv')
            ax.plot(acc3['loss'], 'b-', label=label_3)
            ax2.plot(acc3['acc'], 'b', linestyle='dashdot')
            ax2.plot(acc3['val_acc'], 'b', linestyle='dashed')
        

        ax.legend(loc='right', shadow=True)
        ax.set_ylabel('loss')
        ax2.set_ylabel('acc')
        plt.show()

    def accuracy_noloss(title, index1, label_1, index2=None, label_2=None, index3=None, label_3=None, ):
        plt.style.use({'figure.facecolor': 'white'})
        plt.rcParams.update({'font.size': 15})
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title(title)
        plt.xlabel('epoch')

        acc_path = '/Users/mbornhol/git/neural-profiling/training/results/accuracy/'
        acc1 = pd.read_csv(acc_path + index1 + '.csv')
        ax.plot(acc1['acc'], 'r', label=label_1)
        ax.plot(acc1['val_acc'], 'r', linestyle='dashed')

        if index2 != None:
            acc2 = pd.read_csv(acc_path + index2 + '.csv')
            ax.plot(acc2['acc'], 'g', label=label_2)
            ax.plot(acc2['val_acc'], 'g', linestyle='dashed')

        if index3 != None:
            acc3 = pd.read_csv(acc_path + index3 + '.csv')
            ax.plot(acc3['acc'], 'b', label=label_3)
            ax.plot(acc3['val_acc'], 'b', linestyle='dashed')

        ax.legend(loc='right', shadow=True)
        ax.set_ylabel('accuracy')
        plt.show()

    def prec_recall(title, fontsize, index1, label_1, index2 = "None", label_2 = None, index3 = "None", label_3 = None,):
        plt.style.use({'figure.facecolor':'white'})
        plt.rcParams.update({'font.size': 16})
        fig, ax = plt.subplots(figsize=(9,7))
        plt.title(title)
        ax2 = ax.twinx()
        ax.set_xlabel("k")
        ax.set_ylabel('Precision')
        ax2.set_ylabel('Recall')

        lns1 = ax.plot(index1["k"], index1["precision"], marker=".", color="r", label=f'{label_1} precision')
        lns2 = ax2.plot(index1["k"], index1["recall"], marker=".", linestyle='dashed', color="r",
                        label=f'{label_1} recall')
        lns = lns1 + lns2

        if str(index2) != "None":
            lns3 = ax.plot(index2["k"], index2["precision"], marker=".", color="g", label=f'{label_2} precision')
            lns4 = ax2.plot(index2["k"], index2["recall"], marker=".", linestyle='dashed', color="g",
                            label=f'{label_2} recall')
            lns = lns1 + lns2 + lns3 + lns4

        if str(index3) != "None":
            lns5 = ax.plot(index3["k"], index3["precision"], marker=".", color="b", label=f'{label_3} precision')
            lns6 = ax2.plot(index3["k"], index3["recall"], marker=".", linestyle='dashed', color="b",
                            label=f'{label_3} recall')
            lns = lns1 + lns2 + lns3 + lns4 + lns5 + lns6

        # lns = lns1+lns2+lns3+lns4+lns5+lns6
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, loc='right', prop={'size': fontsize}, shadow=True, bbox_to_anchor=(1,0.4))

        plt.show()

    def enrichment(title, index1, label_1, index2 = "None", label_2 = None, index3 = "None", label_3 = None,):
        plt.style.use({'figure.facecolor':'white'})
        plt.rcParams.update({'font.size': 16})
        fig, ax = plt.subplots(figsize=(10,7))
        plt.title(title)

        plt.plot(100*index1["enrichment_percentile"][:5], index1["ods_ratio"][:5], marker="o", color="r", label = label_1)
        if str(index2) != "None":
            plt.plot(100*index2["enrichment_percentile"][:5], index2["ods_ratio"][:5], marker="o", color="g", label = label_2)
        if str(index3) != "None":
            plt.plot(100*index3["enrichment_percentile"][:5], index3["ods_ratio"][:5], marker="o", color="b", label = label_3)
        plt.ylabel('odds ratio')
        plt.xlabel('percentile %')
        plt.xticks(np.arange(99.5, 97, -0.5))
        ax.invert_xaxis()
        plt.legend(loc = 'upper right', shadow=True)
        plt.show()

    def hitk(title, index1, label_1, index2="None", label_2=None, index3="None", label_3=None, ):
        plt.style.use({'figure.facecolor': 'white'})
        plt.rcParams.update({'font.size': 16})
        fig, ax = plt.subplots(figsize=(10, 7))
        plt.title(title)
        plt.plot(index1, color="r", label=label_1)
        if str(index2) != "None":
            plt.plot(index2, color="g", label=label_2)
        if str(index3) != "None":
            plt.plot(index3, color="b", label=label_3)

        plt.ylabel('Normed accumulated score')
        plt.xlabel('% of neighbors')
        plt.legend(loc='upper right', shadow=True)
        plt.show()
