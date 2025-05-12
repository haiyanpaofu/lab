import matplotlib.pyplot as plo
import seaborn as ses
from statsmodels.datasets import china_smoking
 
#load_pandas()方法 这是 statsmodels 库中加载数据集
#的标准方法。
data=china_smoking.load_pandas().data
#函数reset_index()的作用 重置Dataframe的索引，自定义
data = data.reset_index()

data['Location_Group'] = data['Location'].apply(
    lambda x: 'A-R' if x[0].upper() <= 'R' else 'S-Z')

plo.figure(figsize=(12, 7))
ses.scatterplot(
    data=data,
    x='smoking_yes_cancer_yes',
    y='smoking_no_cancer_yes', 
    hue='Location_Group',
    palette=['navy', 'crimson'],
    s=80,
    edgecolor='black')

plo.title("smoking and cancer of china", fontsize=16)
plo.xlabel("smoking csuses cancer", fontsize=12)
plo.ylabel("without smoking and cancer", fontsize=12)
plo.grid(linestyle='--', alpha=0.5)
plo.show()