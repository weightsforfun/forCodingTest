from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import confusion_matrix,accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import roc_curve, precision_recall_curve
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
iris = load_breast_cancer()
X = iris.data
y = iris.target

# 데이터 분할하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13,stratify=y)    

# 평가할 모델들 불러오고 기본 설정
models = {
    'Logistic Regression': LogisticRegression(random_state=13,solver='liblinear'),
    'Decision Tree': DecisionTreeClassifier(random_state=13,max_depth=3),
    'Random Forest': RandomForestClassifier(random_state=13,n_jobs=1,n_estimators=100),
    'Light GBM': LGBMClassifier(n_estimators=1000,num_leaves=64,n_jobs=-1,boost_from_average=False)
}


    
# 모델로부터 값들 가져오기
def get_clf_eval(y_test,pred):
    acc = accuracy_score(y_test, pred)
    pre = precision_score(y_test, pred)
    re = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    auc = roc_auc_score(y_test, pred)
    return acc,pre,re,f1,auc

# 값 출력하기
def print_clf_eval(y_test,pred):
    confusion=confusion_matrix(y_test,pred)
    acc,pre,re,f1,auc=get_clf_eval(y_test,pred)
    print("=> 오차행렬")
    print(confusion)
    print("===========")
    print('정확도 : {0:.4f}, 정밀도: {1:.4f}'.format(acc,pre))
    print('재현율: {0:.4f}, F1:{1:.4f}, AUC:{2:.4f}'.format(re,f1,auc))
# 각 모델들 학습시켜 값 받기
def get_result(model,X_train, y_train,X_test,y_test):
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    return get_clf_eval(y_test,pred)

# 결과들 표에 정리
def get_result_pd(models,X_train,y_train,X_test,y_test):
    col_names=["accuracy","precision","recall","f1","roc_auc"]
    tmp=[]
    for key in models:
        tmp.append(get_result(models[key],X_train,y_train,X_test,y_test))
    return pd.DataFrame(tmp,columns=col_names,index=list(models.keys()))

# results=get_result_pd(models,X_train,y_train,X_test,y_test)
# results

# 선택한 모델의 ROC Curve와 Precision-Recall Curve 출력
def draw_roc_curve_recall_curve(model,X_test,y_test):
    plt.figure(figsize=(10,10))
    pred=models[model].predict_proba(X_test)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, pred)
    precision, recall, thresholds = precision_recall_curve(y_test, pred)
    
    
    plt.plot(fpr, tpr, label='ROC Curve '+ model)
    plt.plot(recall, precision, label='Precision-Recall Curve '+ model)
    plt.plot([0,1],[0,1],'k--',label='random quess')
    plt.title('ROC')
    plt.legend()
    plt.grid()
    plt.show()

for model_name, model in models.items():
    model.fit(X_train, y_train)
# draw_roc_curve_recall_curve('Random Forest',X_test,y_test)

# GridSearchCV를 사용한 성능 개선 (Decision Tree)
def get_result_with_advancedModel(models,X_train,y_train,X_test,y_test):
    col_names=["accuracy","precision","recall","f1","roc_auc"]
    tmp=[]
    for key in models:
        tmp.append(get_result(models[key],X_train,y_train,X_test,y_test))
    
    # grid_search 를 이용한 random forest 성능 개선
    param_grid = {'max_depth':[3,5,7], 'min_samples_split':[2,3]}
    grid_search = GridSearchCV(models['Decision Tree'], param_grid=param_grid, cv=3,refit=True)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_

    y_pred = best_model.predict(X_test)
    args=get_clf_eval(y_test,y_pred)
    tmp.append(args)
    
    return pd.DataFrame(tmp,columns=col_names,index=list(models.keys())+["Advanced Decision Tree"])
    

# ad_results=get_result_with_advancedModel(models,X_train,y_train,X_test,y_test)
# ad_results


#  Feature Importance 확인
importance = models["Decision Tree"].feature_importances_
feature_names = iris.feature_names

plt.figure(figsize=(10, 6))
plt.barh(feature_names, importance)
plt.xlabel('Feature Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.show()
